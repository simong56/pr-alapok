def menut_kiir(tipus):
    if tipus==2:
        print("1. Új adat bevitele")
        print("2. Kilépés a programból")
    elif tipus==3:
        print("1. Új adat bevitele")
        print("2. Adat módosítása / törlése")
        print("3. Kilépés a programból")
    else:
        print(f"A megadott menüszám, {menu_alahuzas_szama} érvénytelen.")

menu_alahuzas_szama = int(input("Kérem a menü számot: "))
menut_kiir(menu_alahuzas_szama)