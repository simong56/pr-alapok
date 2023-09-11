# feladat_002
'''
Kérjük be a billenytűzetről a két egész számot és írassuk ki a két szám összegét a képernyőre!
'''

szam1 = input("Kérek egy számot: ")
szam1 = int(szam1)
szam3 = float(szam1)

szam2 = int(input("Kérek egy másik számot: "))

osszeg = szam1 + szam2
print(f"A megadott két szám összege: {osszeg}")
print(f"A megadott két szám összege: {szam1 + szam2}")
print(f"szam_1 változó típusa: {type(szam1)}")
print(f"szam_2 változó típusa: {type(szam2)}")
print(f"osszeg változó típusa: {type(osszeg)}")
print(f"szam3 változó értéke: {szam3}")
print(f"szam3 változó típusa: {type(szam3)}")