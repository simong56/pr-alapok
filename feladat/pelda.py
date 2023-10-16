
def beker_egy_szamot():
    szam=int(input("adj meg egy egész számot: "))
    print(szam)

def beker_egy_szamot1(parameter1):
    szam1=int(input("adj meg egy egész számot: "))
    szam1=szam1+parameter1
    print(szam1)

def szamok_osszege():
    return 5+9

beker_egy_szamot()
beker_egy_szamot1(100) 
osszeg=szamok_osszege()
print(osszeg)

#be: szam
#ki: a szam negativ

'''
szam=int(input("Adj meg egy egész számot: "))
if szam>0:
    print(f"A szám ({szam}) pozitív")
'''

#-----------


#be: szam
#ki: a szam negativ e

'''
szam=int(input("Adj meg egy egész számot: "))
if szam>0:
    print(f"A szám ({szam}) pozitív")
elif szam<0:
    print(f"A szám ({szam}) negatív")
'''

#-----------


#be: szam
#ki: a szam negativ e vagy 0

'''
szam=int(input("Adj meg egy egész számot: "))
if szam>0:
    print(f"A szám ({szam}) pozitív")
elif szam<0:
    print(f"A szám ({szam}) negatív")
else:
    print(f"A szám 0")
'''

#-----------


#be: szam
#ki: a szam negativ e vagy 0

'''
szam=int(input("Adj meg egy egész számot: "))
if szam>0:
    print(f"A szám ({szam}) pozitív")
elif szam<0:
    print(f"A szám ({szam}) negatív")
elif szam==0:
    print(f"A szám nulla")
'''