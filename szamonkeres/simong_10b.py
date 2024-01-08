#Simon Gábor, 2.feladat

import random

szam=random.randint(1,2)

guess=(input("Fej vagy írás? (kisbetűvel, ékezettel)  "))

if guess=="fej" and szam==1:
    print("Eltaláltad")
elif guess=="írás" and szam==2:
    print("Eltaláltad")
elif guess=="fej" and szam==2:
    print("Nem talált")
elif guess=="írás" and szam==1:
    print("Nem talált")
