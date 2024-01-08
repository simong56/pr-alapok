import random
szam=int(input("tippeld meg a számot 1, 2 vagy 3: "))
randomszam=random.randint(1,3)
if szam==randomszam:
    print("Eltaláltad!")
else:
    print(f"a te számod {szam} volt, a random szám pedig {randomszam}")