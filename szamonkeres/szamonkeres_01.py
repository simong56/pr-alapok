print("Simon Gábor")
jegy = int(input("Kérek egy jegyet 1-5: "))

if jegy>6:
    print("A jegye 5-nél nagybb, ami nem megfelelő")
elif jegy<1:
    print("A jegye 1-nél kisebb, ami nem megfelelő")

elif jegy==1:
    print(f"A jegye {jegy}, vagyis elégtelen.")
elif jegy==2:
    print(f"A jegye {jegy}, vagyis elégséges.")
elif jegy==3:
    print(f"A jegye {jegy}, vagyis közepes.")
elif jegy==4:
    print(f"A jegye {jegy}, vagyis jó.")
elif jegy==5:
    print(f"A jegye {jegy}, vagyis jeles.")