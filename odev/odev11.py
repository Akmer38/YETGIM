class Arac:
    def __init__(self, marka, model, gunluk_ucret):
        self.marka = marka
        self.model = model
        self.gunluk_ucret = gunluk_ucret

    def bilgileri_goster(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Gunluk Ucret: {self.gunluk_ucret} TL")


class Otomobil(Arac):
    def __init__(self, marka, model, gunluk_ucret, kapi_sayisi):
        super().__init__(marka, model, gunluk_ucret)
        self.kapi_sayisi = kapi_sayisi

    def bilgileri_goster(self):
        print("--- Otomobil Bilgileri ---")
        super().bilgileri_goster()
        print(f"Kapi Sayisi: {self.kapi_sayisi}")


class Motorsiklet(Arac):
    def __init__(self, marka, model, gunluk_ucret, motor_hacmi):
        super().__init__(marka, model, gunluk_ucret)
        self.motor_hacmi = motor_hacmi

    def bilgileri_goster(self):
        print("--- Motorsiklet Bilgileri ---")
        super().bilgileri_goster()
        print(f"Motor Hacmi: {self.motor_hacmi} cc")


class KiralamaSistemi:
    def __init__(self):
        self.mevcut_araclar = []
        self.kiralanmis_araclar = []

    def arac_ekle(self, arac):
        self.mevcut_araclar.append(arac)
        print(f"\nTamamdir, {arac.marka} {arac.model} sisteme eklendi.")
    
    def arac_bul(self, marka, model, liste):
        for arac in liste:
            if arac.marka.lower() == marka.lower() and arac.model.lower() == model.lower():
                return arac
        return None

    def arac_kirala(self, marka, model):
        kiralanacak_arac = self.arac_bul(marka, model, self.mevcut_araclar)
        
        if kiralanacak_arac:
            self.mevcut_araclar.remove(kiralanacak_arac)
            self.kiralanmis_araclar.append(kiralanacak_arac)
            print(f"\n{marka} {model} kiralandi. Iyi yolculuklar!")
        else:
            print("\nBu arac ya mevcut degil ya da zaten kiralanmis.")
            
    def arac_iade_et(self, marka, model):
        iade_edilecek_arac = self.arac_bul(marka, model, self.kiralanmis_araclar)
        
        if iade_edilecek_arac:
            self.kiralanmis_araclar.remove(iade_edilecek_arac)
            self.mevcut_araclar.append(iade_edilecek_arac)
            print(f"\n{marka} {model} iade edildi. Tesekkurler!")
        else:
            print("\nBoyle bir arac kiralanmamis gorunuyor.")

    def araclari_goster(self, liste_tipi):
        if liste_tipi == "mevcut":
            print("\n--- KIRALANABILIR ARACLAR ---")
            liste = self.mevcut_araclar
            if not liste:
                print("Su an kiralanabilir arac yok.")
        elif liste_tipi == "kiralanmis":
            print("\n--- KIRALANMIS ARACLAR ---")
            liste = self.kiralanmis_araclar
            if not liste:
                print("Kirada hic arac yok.")
        
        for arac in liste:
            arac.bilgileri_goster()
            print("-" * 20)

def sistemi_baslat():
    sistem = KiralamaSistemi()
    
    # Baslangicta sistemde olacak araclar
    oto1 = Otomobil("Toyota", "Corolla", 500, 4)
    motor1 = Motorsiklet("Yamaha", "R1", 800, 1000)
    sistem.mevcut_araclar.extend([oto1, motor1])

    print("----- Arac Kiralama Sistemine Hosgeldin -----")

    while True:
        print("\n--- MENU ---")
        print("1: Yeni Arac Ekle")
        print("2: Arac Kirala")
        print("3: Arac Iade Et")
        print("4: Kiralanabilir Araclari Goster")
        print("5: Kiralanmis Araclari Goster")
        print("q: Cikis")
        
        secim = input("Ne yapmak istersin?: ").strip().lower()

        if secim == 'q':
            print("\nGorusuruz!")
            break
        
        elif secim == '1':
            tip = input("Otomobil mi (o), Motorsiklet mi (m) ekleyeceksin?: ").lower()
            marka = input("Marka: ")
            model = input("Model: ")
            ucret = int(input("Gunluk Ucret (TL): "))
            
            if tip == 'o':
                kapi = int(input("Kapi Sayisi: "))
                yeni_arac = Otomobil(marka, model, ucret, kapi)
                sistem.arac_ekle(yeni_arac)
            elif tip == 'm':
                hacim = int(input("Motor Hacmi (cc): "))
                yeni_arac = Motorsiklet(marka, model, ucret, hacim)
                sistem.arac_ekle(yeni_arac)
            else:
                print("Gecersiz tip girdin.")

        elif secim == '2':
            marka = input("Kiralamak istedigin aracin markasi: ")
            model = input("Modeli: ")
            sistem.arac_kirala(marka, model)

        elif secim == '3':
            marka = input("Iade etmek istedigin aracin markasi: ")
            model = input("Modeli: ")
            sistem.arac_iade_et(marka, model)

        elif secim == '4':
            sistem.araclari_goster("mevcut")
        
        elif secim == '5':
            sistem.araclari_goster("kiralanmis")
            
        else:
            print("\nGecersiz secim! Menuden birini sec.")

sistemi_baslat()