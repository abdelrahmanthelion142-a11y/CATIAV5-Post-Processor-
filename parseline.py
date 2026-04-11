import json
lsmovement=""
lsplane=""
lstiprotation=""
lsrotation=""
lstipfedrejt=""
lssklop=""



class parseline:
    def __init__(self):
        # Učitati biblioteku naredbi iz json tablice: bible1.json
        with open("bible1.json", "r", encoding="utf-8") as f:
            self.commands = json.load(f)

    def parseline(self, line):
        global lsmovement
        global lsplane
        global lstiprotation
        global lsrotation
        global lstipfedrejt
        global lssklop
        if "/" in line:
            elements = line.split("/")
            command = elements[0].strip()
            
            if command == "GOTO":
                coords = elements[1].strip().split(",")
                x = coords[0].strip()
                y = coords[1].strip()
                z = coords[2].strip()
                if float(y) == 0:
                    ravnina="G18"
                    kretanje="G1"
                    koord=(f"X{x} Z{z}")
                    
                elif float(x) != 0:
                    ravnina="G17"
                    kretanje="G1"
                    koord=(f"X{x} Y{y}")
                    
                elif float(z) != 0:
                    ravnina="G19"
                    kretanje="G1"
                    koord=(f"X{x} Y{y}")
         
                else:
                    print(f"Provjeriti koordinate: {line}")
                    return
                
                if lsmovement != kretanje:
                    print(kretanje, end=" ")
                    lsmovement=kretanje
                else:
                    print(end="")
                
                if lsplane != ravnina:
                    print(ravnina, end=" ")
                    lsplane=ravnina
                else:
                    print(end="")
                print(koord)
                
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
                    
                if lstiprotation != tipfedrejt:
                    print(tipfedrejt, end=" ")
                    lstiprotation=tipfedrejt
                else:
                    print(end="")
                    
                if rotation == "CLW":
                    smjervrtnje=("M3 ")
                elif rotation == "CCLW":
                    smjervrtnje=("M4 ")
                else:
                    print(f"Provjeriti treću vrijednost (smjer vrtnje): {line}")
                    
                if lsrotation != smjervrtnje:
                    print(smjervrtnje, end=" ")
                    lsrotation=smjervrtnje
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
                    
                if lstipfedrejt != fedrejt:
                    print(fedrejt, end=" ")
                    lstipfedrejt=fedrejt
                else:
                    print(end="")
                print("F"+numf)
                
            elif command == "TPRINT":
                izbor_alat = elements[1].strip().split(",")
                sklop = izbor_alat[0].strip()
                drzac = izbor_alat[1].strip()
                ostrica = izbor_alat[2].strip()
                if lssklop != sklop:
                    print(f"T={sklop}")
                    lssklop=sklop
                else:
                    print(end="")
                
            elif command == "SWITCH" or command == "LOADTL" or command == "CUTTER" or command == "TOOLNO":
                print(end="")
                
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
            
        elif "FINI" in line:
            print(" G18 G1 X40 Z90\n M30")
            
        elif "PARTNO" in line:
            print("#DEFINIRATI SIROVAC")
        
        else:
            print(end="")