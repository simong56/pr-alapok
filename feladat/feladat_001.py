# feladat_001
'''
Kérjük be a billenytűzetről a nevünket és irassuk ki a képernyőre!
A billenytűzetről mindig szöveget (stringet) olvasunk be!
type(változó)
'''

vezeteknev = input("Kérem a vezetékneved: ")

keresztnev = input("Kérem a keresztneved: ")
print(f"Szóval a neved:  {vezeteknev} {keresztnev}")
print(f"A vezetéknév változó típua: {type(vezeteknev)}")
print(f"A keresztnév változó típua: {type(keresztnev)}")