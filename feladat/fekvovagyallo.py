width=int(input("Add meg a téglalap szélességét (cm):  "))
height=int(input("Add meg a téglalap magasságát (cm):  "))
terulet=int(height*width)

if width>height:
    print("A téglalap fekvő.")
elif height>width:
    print("A téglalap álló.")
else:
    print("A téglalap egy négyzet.")

print(f"Területe: {terulet}cm²")