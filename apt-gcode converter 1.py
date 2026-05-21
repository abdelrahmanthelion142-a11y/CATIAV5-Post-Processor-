import os
import sys
from parseline import Myparseline
from jezici import HR, EN

while True:
    izbor = input("Choose language (HR/EN): ").strip().upper()
    if izbor == "HR" or izbor == "1" or izbor == "HRV" or izbor == "HRVATSKI":
        LANG = HR
        break
    elif izbor == "EN" or izbor == "2" or izbor == "ENG" or izbor == "ENGLISH":
        LANG = EN
        break
    else:
        print("- Invalid choice. Please enter HR or EN.")

print(LANG["def programa"])

while True:
    catia_comments = input(LANG["catia comentari"]).strip().upper()
    if catia_comments == "DA" or catia_comments == "YES" or catia_comments == "1":
        ccmt=1
        break
    elif catia_comments == "NE" or catia_comments == "NO" or catia_comments == "0":
        ccmt=0
        break
    else:
        print(LANG["kriv odabir za komt"])
        continue

while True:
    spindle_start = input(LANG["spindle start"]).strip().upper()
    if spindle_start == "DA" or spindle_start == "YES" or spindle_start == "1":
        ss=1
        break
    elif spindle_start == "NE" or spindle_start == "NO" or spindle_start == "0":
        ss=0
        break
    else:
        print(LANG["krivi spindle start"])
        continue


# check if file was first argument
if len(sys.argv) < 2:
    print(LANG["Nije predana datoteka."])
    # input("Klikni Enter za dalje...")
    exit(1000)

# this is the file you dropped
input_file = sys.argv[1]

# provjeriti da li postoji file
if not os.path.exists(input_file):
    print(LANG["Nepostojeća datoteka."])
    # input("Klikni Enter za dalje...")
    exit(1001)


# provjeriti da li je file tekstualni
if not os.path.isfile(input_file):
    print(LANG["Neispravna vrsta"])
    exit(1002)

print(LANG["Datoteka učitana:"], input_file)
print(LANG["Učitavanje linija"])

parse = Myparseline(LANG, ccmt, ss)

# provjeriti da li je zaista tekstualna datoteka
try:
    with open(input_file, "r", encoding="utf-8") as f:
        myline = ""
        for line in f:           
            myline += line.strip()
            if(myline.endswith("$")):
                myline = myline[:-1]
                continue
            else:
                parse.parseline(myline)
                myline = ""

except UnicodeDecodeError:
    print(LANG["Neispravna vrsta"])
    #input("Klikni Enter za dalje...")
    exit(1003)
except Exception as e:
    print(LANG["error"] + str(e))
    #input("Klikni Enter za dalje...")
    exit(1004)

print("\n" + LANG["Gotovo."])
exit(0)