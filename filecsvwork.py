import csv

f = open("./data/movimientos.dat", "r")
reader = csv.reader(f, delimiter=",", quotechar='"')
for registro in reader:
    print(registro)

f.close()

f = open("./data/movimientos.dat", "r")
reader = csv.DictReader(f, delimiter=",", quotechar='"')
for registro in reader:
    print (registro)

f.close()