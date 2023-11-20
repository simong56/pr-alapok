#Simon Gábor 10b
szam=int(input("Adj meg egy egész számot: "))
if szam>0:
    print(f"A számod {szam}, ami pozitív")
elif szam<0:
    print(f"A számod {szam}, ami negatív")
elif szam==0:
    print(f"A számod nulla")