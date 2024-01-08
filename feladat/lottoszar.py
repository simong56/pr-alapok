import random

sorsolt_szamok=[]
tippek=[]
talaltszam=[]
db=5
for i in range(0,5):
    sorsolt_szamok.append(random.randint(1,90))

tipp1=int(input("Első lottó szám: "))
tipp2=int(input("Második lottó szám: "))
tipp3=int(input("Harmadik lottó szám: "))
tipp4=int(input("Negyedik lottó szám: "))
tipp5=int(input("Ötödik lottó szám: "))

tippek.append(tipp1)
tippek.append(tipp2)
tippek.append(tipp3)
tippek.append(tipp4)
tippek.append(tipp5)

#if any(int in sorsolt_szamok for int in tippek):
#    print("valami van")

sorsoltset=set(sorsolt_szamok)
tippeltset=set(tippek)

talaltszam=len(tippeltset.intersection(sorsoltset))

print(f"{talaltszam} darab számot találtál el.")
print(f"A húzott számok: {sorsolt_szamok}")
print(f"A te számaid: {tippek}")
