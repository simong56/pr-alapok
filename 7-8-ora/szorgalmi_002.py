#szorgalmi_002.py
#Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi, hogy az ikrek (Henrik és Hanna) jönnek-e ma kosrazni! Például így: Jön Henrik ma kosarazni? (igen/nem). A program írja ki, hogy melyik állítás igaz az alábbiak közül:
#- egyikük sem jön kosarazni,
#- mind a ketten jönnek kosarazni,
#- csak az egyikük jön kosarazni.
#https://sulipy.hu/elagazasok/logikai_kifejezesek?tab=feladatok

he=input("Henrik ma jön kosarazni? igen/nem választ írj ")
ha=input("Hanna ma jön kosarazni? igen/nem választ írj ")

if he=="igen" and ha=="igen":
    print("Mindketten jönnek ma kosarazni")
elif he=="igen" and ha=="nem":
    print("Csak Henrik jön ma kosarazni")
elif he=="nem" and ha=="igen":
    print("Csak Hanna jön ma kosarazni")
elif he=="nem" and ha=="nem":
    print("Egyiken se jönnek ma kosarazni")
    
