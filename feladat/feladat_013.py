'''
be: szam
ki: a szam negativ
'''
'''
szam=int(input("Adj meg egy egész számot: "))
if szam>0:
    print(f"A szám ({szam}) pozitív")
'''

#-----------

'''
be: szam
ki: a szam negativ e
'''
'''
szam=int(input("Adj meg egy egész számot: "))
if szam>0:
    print(f"A szám ({szam}) pozitív")
elif szam<0:
    print(f"A szám ({szam}) negatív")
'''

#-----------

'''
be: szam
ki: a szam negativ e vagy 0
'''
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

'''
be: szam
ki: a szam negativ e vagy 0
'''
szam=int(input("Adj meg egy egész számot: "))
if szam>0:
    print(f"A szám ({szam}) pozitív")
elif szam<0:
    print(f"A szám ({szam}) negatív")
elif szam==0:
    print(f"A szám nulla")