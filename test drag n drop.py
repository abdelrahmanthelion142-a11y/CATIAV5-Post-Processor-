
import os
import sys

# check if file was first argument
if len(sys.argv) < 2:
    print("Nije predana datoteka.")
    # input("Klikni Enter za dalje...")
    exit(1000)

# this is the file you dropped
input_file = sys.argv[1]
machine = sys.argv[2] if len(sys.argv) > 2 else None

# provjeriti da li postoji file
if not os.path.exists(input_file):
    print("Nepostojeća datoteka.")
    # input("Klikni Enter za dalje...")
    exit(1001)


# provjeriti da li je file tekstualni
if not os.path.isfile(input_file):
    print("Neispravna datoteka.")
    #input("Klikni Enter za dalje...")
    exit(1002)

print("Datoteka učitana:", input_file)
print("Pretraživanje linija\n")



# provjeriti da li je zaista tekstualna datoteka
try:
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            print(line)

            
            
except UnicodeDecodeError:
    print("Nevaljana vrsta datoteke. Molimo odaberite tekstualnu datoteku.")
    #input("Klikni Enter za dalje...")
    exit(1003)
except Exception as e:
    print(f"Greška prilikom čitanja datoteke: {e}")
    #input("Klikni Enter za dalje...")
    exit(1004)

print("\nGotovo.")
exit(0)