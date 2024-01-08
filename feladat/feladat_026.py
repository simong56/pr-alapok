tantargyak = ['matek', 'töri', 'bio', 'kémia', 'info']
szamlalo=0
index=0
for tantargy in tantargyak: 
    print(f"A tantárgyak listája {index}. eleme {tantargy}")
    szamlalo = szamlalo+1
print(f"{szamlalo} eleme van a tantárgyak listának")