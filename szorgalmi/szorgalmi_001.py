#Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
#- pozitív páros vagy
#- negatív páratlan.
#Az eredményről tájékoztatja a felhasználót.
#https://sulipy.hu/elagazasok/logikai_kifejezesek?tab=feladatok

szam=int(input("Adj meg egy számot:"))

if (szam % 2) == 0 and (szam > 0):
    print("A szám páros és pozitív")   
elif (szam % 2) == 0 and (szam < 0):
    print("A szám páros és negatív")
elif (szam > 0):
    print("A szám páratlan és pozitív")
elif (szam < 0):
    print("A szám páratlan és negatív")
elif (szam == 0):
    print("A szám 0")