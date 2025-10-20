class Urun:
    def __init__(self, urun_id, isim, fiyat):
        self.urun_id = urun_id
        self.isim = isim
        self.fiyat = fiyat

    def bilgileri_goster(self):
        print(f"Urun ID: {self.urun_id}")
        print(f"Isim: {self.isim}")
        print(f"Fiyat: {self.fiyat:.2f} TL")


class ElektronikUrun(Urun):
    def __init__(self, urun_id, isim, fiyat, garanti_suresi):
        super().__init__(urun_id, isim, fiyat)
        self.garanti_suresi = garanti_suresi

    def bilgileri_goster(self):
        print("--- Elektronik Urun ---")
        super().bilgileri_goster()
        print(f"Garanti Suresi: {self.garanti_suresi} yil")


class GiyimUrunu(Urun):
    def __init__(self, urun_id, isim, fiyat, beden, renk):
        super().__init__(urun_id, isim, fiyat)
        self.beden = beden
        self.renk = renk

    def bilgileri_goster(self):
        print("--- Giyim Urunu ---")
        super().bilgileri_goster()
        print(f"Beden: {self.beden}")
        print(f"Renk: {self.renk}")


class Magaza:
    def __init__(self):
        self.urunler = []
        self.son_id = 0

    def urun_ekle(self, urun):
        self.urunler.append(urun)
        print(f"\n'{urun.isim}' magazaya eklendi.")

    def urun_cikar(self, urun_id):
        silinecek_urun = None
        for urun in self.urunler:
            if urun.urun_id == urun_id:
                silinecek_urun = urun
                break
        
        if silinecek_urun:
            self.urunler.remove(silinecek_urun)
            print(f"\n'{silinecek_urun.isim}' (ID: {urun_id}) urunu silindi.")
        else:
            print(f"\nBu ID'ye sahip bir urun bulunamadi.")

    def urunleri_goster(self):
        print("\n--- MAGAZADAKI URUNLER ---")
        if not self.urunler:
            print("Magazada hic urun yok.")
        else:
            for urun in self.urunler:
                urun.bilgileri_goster()
                print("-" * 25)
    
    def yeni_id_al(self):
        self.son_id += 1
        return self.son_id

def sistemi_baslat():
    magaza = Magaza()
    
    # Baslangicta sistemde olacak urunler
    laptop = ElektronikUrun(magaza.yeni_id_al(), "Laptop", 15000, 2)
    tshirt = GiyimUrunu(magaza.yeni_id_al(), "T-Shirt", 250, "M", "Mavi")
    magaza.urunler.extend([laptop, tshirt])
    
    print("----- E-ticaret Yonetim Paneline Hosgeldin -----")

    while True:
        print("\n--- MENU ---")
        print("1: Yeni Urun Ekle")
        print("2: Urun Cikar")
        print("3: Tum Urunleri Goster")
        print("q: Cikis Yap")
        
        secim = input("Ne yapmak istersin?: ").strip().lower()

        if secim == 'q':
            print("\nGorusuruz!")
            break
        
        elif secim == '1':
            tip = input("Elektronik mi (e), Giyim mi (g) ekleyeceksin?: ").lower()
            
            try:
                isim = input("Urunun adi: ")
                fiyat = float(input("Fiyati (TL): "))
                urun_id = magaza.yeni_id_al()

                if tip == 'e':
                    garanti = int(input("Garanti suresi (yil): "))
                    yeni_urun = ElektronikUrun(urun_id, isim, fiyat, garanti)
                    magaza.urun_ekle(yeni_urun)
                elif tip == 'g':
                    beden = input("Beden: ")
                    renk = input("Renk: ")
                    yeni_urun = GiyimUrunu(urun_id, isim, fiyat, beden, renk)
                    magaza.urun_ekle(yeni_urun)
                else:
                    print("Gecersiz tip girdin. 'e' ya da 'g' yazmaliydin.")
                    magaza.son_id -= 1 # ID'yi bosa harcamayalim
            except ValueError:
                print("Hatali giris. Fiyat veya garanti gibi sayisal alanlara harf girdin.")
                magaza.son_id -= 1 # ID'yi bosa harcamayalim

        elif secim == '2':
            try:
                urun_id = int(input("Silmek istedigin urunun ID'sini gir: "))
                magaza.urun_cikar(urun_id)
            except ValueError:
                print("Lutfen gecerli bir ID (sayi) gir.")

        elif secim == '3':
            magaza.urunleri_goster()
            
        else:
            print("\nGecersiz secim! Menuden birini sec.")

sistemi_baslat()
