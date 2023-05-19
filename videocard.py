class Videocards:
  def __init__(self, sor):
   oszlop = sor.split(";")
   self.nev = oszlop[0] 
   self.ar = int(oszlop[1]) 
   self.ventilatorokszama = int(oszlop[2])
   self.ram = oszlop[3]
print("---------------------------")
fajl = open("videocards.txt","r",encoding="utf-8")
fajl.readline()
k_lista = [Videocards(sor.strip()) for sor in fajl]
print("Videokaryak neve és áruk($):")
for videocards in k_lista:
  print(videocards.nev,videocards.ar)
print("---------------------------")
print(f"számuk: {len(k_lista)} db")

osszeg = 0
for k in k_lista:
    osszeg = osszeg + k.ar
print(f"A videokartyak összértéke: {osszeg} $")
print("---------------------------")
print("500.000 $ feletti videocards:")
for videocards in k_lista:
    if videocards.ar > 500000:
        print("\t"+videocards.nev)
print("---------------------------")

videocards_szam = 0
for videocards in k_lista:
    if videocards.ar > 500000:
        videocards_szam += 1
print(f"500.000 $ feletti videokartyak száma: {videocards_szam} db")
print("---------------------------")
sorba = sorted(k_lista, key=lambda n: n.ar)
print(f"A legdrágább videokartya neve: {sorba[-1].nev}")

legdragabb = max(f.ar for f in k_lista)
for item in k_lista:
     if item.ar == legdragabb:
         print(f"a legdrágább videokartya ára: {item.ar}")
print("---------------------------")