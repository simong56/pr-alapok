mondat=input("adj meg egy mondatot: ")

if mondat.endswith("."):
    print("A mondat kijelentő.")
elif mondat.endswith("?"):
    print("A mondat kérdő.")
elif mondat.endswith("!"):
    print("A mondat felkiáltó, felszólító vagy óhajtó.")
else:
    print("A mondat végére rakj mondatvégi jelet! (./?/!)")
