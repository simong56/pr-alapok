"""
A feladat_003 kibővítése:
0 éves ---> Még nem születtél meg!
1|2|3|4|5 éves vagy, még nem jársz általános iskolába!
6|7|...|13|14 éves vagy, általános iskolába jársz!
15|16|...|63|64 éves vagy, tanulsz vagy dolgozol!
65 vagy több éves vagy, nyugdíjas.

"""

kor = int(input("hány éves vagy? "))

if kor <= 0:
    print("Még nem születtél meg!")

if kor <= 5:
    print(f"{kor} éves vagy, még nem jársz általános iskolába!")

if kor >= 6 and kor <= 14:
    print(f"{kor} éves vagy, általános iskolába jársz!")

if kor >= 15 and kor <= 64:
    print(f"{kor} éves vagy, tanulsz vagy dolgozol!")

if kor >= 65 :
    print(f"65 vagy több éves vagy, nyugdíjas.")