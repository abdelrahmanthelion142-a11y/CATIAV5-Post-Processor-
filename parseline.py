import json
import re
import math

class Myparseline:
    lsmovement=""
    lsplane=""
    lstiprotation=""
    lsrotation=""
    lstipfedrejt=""
    lssklop=""
    koord_x = 0
    koord_y = 0
    koord_z = 0
    ls_x = 0
    ls_y = 0
    ls_z = 0
    ls_i=0
    ls_j=0
    ls_k=0
    D=0

    
    
    def __init__(self):
        self.lsmovement=""
        self.lsplane=""
        self.lstiprotation=""
        self.lsrotation=""
        self.lstipfedrejt=""
        self.lssklop=""
        self.koord_x = 0
        self.koord_y = 0
        self.koord_z = 0
        self.ls_x = 0
        self.ls_y = 0
        self.ls_z = 0
        self.ls_i = 0
        self.ls_j = 0
        self.ls_k = 0
        self.D = 0
        
        with open("bible1.json", "r", encoding="utf-8") as f:
            self.commands = json.load(f)

    def parseline(self, line):
     
        if "CIRCLE" in line:
            elements = line.split(" ","/",",")
            centar_x = elements[3].strip()
            centar_y = elements[4].strip()
            centar_z = elements[5].strip()
            radius = elements[6].strip()
            centar2_x = elements[9].strip()
            centar2_y = elements[10].strip()
            centar2_z = elements[11].strip()
            kraj_x = elements[12].strip()
            kraj_y = elements[13].strip()
            kraj_z = elements[14].strip()

            if centar_x!=centar2_x or centar_y!=centar2_y or centar_z!=centar2_z:
                print(f"Provjeriti {line} centri se ne poklapaju")
            else:
                print(end="")
            
            if self.ls_plane == "G18":
                vektor2_x=self.ls_x-centar_x
                vektor2_z=self.ls_z-centar_z
                D=self.ls_i*vektor2_y-vektor2_x*self.ls_k
                if D<0:
                    print("Desno")
                elif D>0:
                    print("Lijevo")
                else:
                    print("Provjeriti koord " + line)
            elif self.ls_plane == "G17":
                vektor2_y=self.ls_y-centar_y
                vektor2_x=self.ls_x-centar_x
                D=self.ls_i*vektor2_y-vektor2_x*self.ls_j
                if D<0:
                    print("Desno")
                elif D>0:
                    print("Lijevo")
                else:
                    print("Provjeriti koord " + line)
            elif self.ls_plane == "G19":
                vektor2_y=self.ls_y-centar_y
                vektor2_z=self.ls_z-centar_z
                D=self.ls_j*vektor2_z-vektor2_y*self.ls_k
                if D<0:
                    print("Desno")
                elif D>0:
                    print("Lijevo")
                else:
                    print("Provjeriti koord " + line)
            else:
                print(f"Provjeriti ravninu: {line}")
            
        elif "/" in line:
            elements = line.split("/")
            command = elements[0].strip()
            
            
            if command == "GOTO":
                coords = elements[1].strip().split(",")
                x = coords[0].strip()
                y = coords[1].strip()
                z = coords[2].strip()
                
                if y==self.ls_y:
                    ravnina="G18"
                    if x==self.ls_x:
                        self.koord_x=""
                    else:
                        self.koord_x=(f"X{x}")
                    if z==self.ls_z:
                        self.koord_z=""                    
                    else:
                        self.koord_z=(f"Z{z}")
                        
                elif x!=self.ls_x:
                    ravnina="G17"
                    if x==self.ls_x:
                        self.koord_x=""
                    else:
                        self.koord_x=(f"X{x}")
                    if y==self.ls_y:
                        self.koord_y=""
                    else:
                        self.koord_y=(f"Y{y}")
                        
                elif z!=self.ls_z:
                    ravnina="G19"
                    if y==self.ls_y:
                        self.koord_y=""
                    else:
                        self.koord_y=(f"Y{y}")
                    if z==self.ls_z:
                        self.koord_z=""                    
                    else:
                        self.koord_z=(f"Z{z}")
                else:
                    print(f"Provjeriti koordinate: {line}")
                           
   
                if self.lsplane != ravnina:
                    print(ravnina, end=" ")
                    self.lsplane=ravnina                  
                else:
                    print(end="")  
                print(self.koord_x, self.koord_y, self.koord_z)
                self.ls_x=x
                self.ls_y=y
                self.ls_z=z
                
            elif command =="SPINDL":
                spindlDT = elements[1].strip().split(",")
                num = spindlDT[0].strip()
                tip = spindlDT[1].strip()
                rotation = spindlDT[2].strip()
                
                if tip == "SFM":
                    tipfedrejt=("G96 ")
                elif tip == "RPM":
                    tipfedrejt=("G97 ")
                else:
                    print(f"Provjeriti tip vrijednosti(spm ili rpm): {line}")
                    
                if self.lstiprotation != tipfedrejt:
                    print(tipfedrejt, end=" ")
                    self.lstiprotation=tipfedrejt
                else:
                    print(end="")
                    
                if rotation == "CLW":
                    smjervrtnje=("M3 ")
                elif rotation == "CCLW":
                    smjervrtnje=("M4 ")
                else:
                    print(f"Provjeriti treću vrijednost (smjer vrtnje): {line}")
                    
                if self.lsrotation != smjervrtnje:
                    print(smjervrtnje, end=" ")
                    self.lsrotation=smjervrtnje
                else:
                    print(end="")
                print("S"+num)
                
            elif command == "FEDRAT":
                feed = elements[1].strip().split(",")
                numf = feed[0].strip()
                vrstaf = feed[1].strip()
                
                if vrstaf == "MMPR":
                    fedrejt=("G95")   
                elif vrstaf == "MMPM":  
                    fedrejt=("G94")
                else:
                    print(f"Provjeriti feedrate vrijednost: {line}")
                    
                if self.lstipfedrejt != fedrejt:
                    print(fedrejt, end=" ")
                    self.lstipfedrejt=fedrejt
                else:
                    print(end="")
                    
                movement="G1"
                
                if self.lsmovement != movement:
                        print(movement, end=" ")
                        self.lsmovement=movement
                else:
                        print(end="")
                
                print("F"+numf)
                
            elif command == "TPRINT":
                izbor_alat = elements[1].strip().split(",")
                sklop = izbor_alat[0].strip()
                drzac = izbor_alat[1].strip()
                ostrica = izbor_alat[2].strip()
                
                if self.lssklop != sklop:
                    print(f"T={sklop}")
                    self.lssklop=sklop
                else:
                    print(end="")
                
            elif command == "SWITCH" or command == "LOADTL" or command == "CUTTER" or command == "TOOLNO" or command == "INTOL" or command =="OUTTOL":
                print(end="")
            
            elif command == "INDIRV":
                vektor = elements[1].strip().split(",")
                self.ls_i=vektor[0].strip()
                self.ls_j=vektor[1].strip()
                self.ls_k=vektor[2].strip()
               
            else:
                    print(f"#Neispravna linija: {line}")
        
        elif "$$ OPERATION NAME :" in line:
            opname = line.split(":")
            opname1 = opname[0].strip()
            opname2 = opname[1].strip()
            
            if "Tool" in opname2:
                print(end="")
            else:
                print(f"#{opname2}")
                
        elif "RAPID" in line:
            if lsmovement != "G0":
                print("G0 ")
                lsmovement="G0"
            else:
                print(end="")
            
        elif "FINI" in line:
            print(" G18 G1 X40 Z90\n M30")
            
        elif "PARTNO" in line:
            print("G55" + "\n" + "DIAMOF" + "\n" + "#DEFINIRATI SIROVAC")
        
        elif "$$" in line:
            print(end="")
        else:
            print("Provjeriti: " + line)
      