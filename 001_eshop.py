class Produkt:
    # nazev = mydlo
    # cena = za 1 MJ 
    # pocet = 2
    # jednotka = "kg"
    def __init__(self,nazev,cena,pocet,mjednotka):
        self.nazev =  nazev
        self.cena = cena
        self.pocet = pocet
        self.mjednotka = mjednotka      
         
class Kosik:
    # polozky
    def __init__(self):
        self.polozky = []         
    def pridej(self,produkt,pocet):
        self.polozky.append([produkt,pocet])
    
    def vypis_obsah(self):
        print("Obsah kosiku: ")
        #2 kus <tab> Nazev produktu
        
        for polozka in self.polozky:
            print(f"{polozka[0].pocet} {polozka[0].mjednotka}\t{polozka[0].nazev}")    
    
        
class Zakaznik:
    # _login
    # kosik
    def __init__(self,login):
        self._login = login
        self.kosik = Kosik()
    
    # tzv. getter (get - získání obsahu atributu)
    def get_login(self):
        return self._login
    
    # tzv. setter (set - změna obsahu atributu)
    def set_login(self,nova_hodnota):
        self._login = nova_hodnota



z1 = Zakaznik("Franta")
z2 = Zakaznik("Maty")

flashdisk = Produkt("Flash disk 128 GB",100,1,1)
mouka = Produkt("All purpose flour",200,1,"kg")
meloun = Produkt("Meloun",5,1,"kg")

z1.kosik.pridej(mouka,2)
z1.kosik.pridej(meloun,6)

z1._login = "Hacker"

print(f"Toto je kosik zakaznika {z1._login} , : {z1.kosik.polozky}")
print(flashdisk,mouka)

print(z1.kosik.vypis_obsah())

