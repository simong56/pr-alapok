nev=input("Kereszteneved: ")
kor=int(input("Életkorod: "))

if kor<1:
    print(f"A kora alapján {nev} egy csecsemő!")
elif 1<=kor<6:
    print(f"A kora alapján {nev} egy kisgyerek!")
elif 6<=kor<12:
    print(f"A kora alapján {nev} egy gyerek!")
elif 12<=kor<16:
    print(f"A kora alapján {nev} egy serdülő!")
elif 16<=kor<25:
    print(f"A kora alapján {nev} egy ifjú!")
elif 25<=kor<65:
    print(f"A kora alapján {nev} egy felnőtt!")
else:
    print(f"A kora alapján {nev} egy nyugdíjas!")
