darab_karakter=1
sor=1
adott=int(input("adj egy szamot: "))
while sor<=adott:
    oszlop=1
    while oszlop<=darab_karakter:
        print("0 ", end='')
        oszlop=oszlop+1
    print("")
    darab_karakter=darab_karakter+1
    sor=sor+1

if sor>=adott:
    while oszlop<=darab_karakter:
        print("0 ", end='')
        oszlop=oszlop+1
    print("")
    darab_karakter=darab_karakter+1
    sor=sor+1