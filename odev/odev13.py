class Dikdortgen:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    @property
    def genislik(self):
        return self._genislik

    @genislik.setter
    def genislik(self, value):
        if value > 0:
            self._genislik = value
        else:
            raise ValueError("Genişlik 0'dan büyük olmalı.")

    @property
    def yukseklik(self):
        return self._yukseklik

    @yukseklik.setter
    def yukseklik(self, value):
        if value > 0:
            self._yukseklik = value
        else:
            raise ValueError("Yükseklik 0'dan büyük olmalı.")

    @property
    def alan(self):
        return self.genislik * self.yukseklik

    @property
    def cevre(self):
        return 2 * (self.genislik + self.yukseklik)
        
    def bilgileri_goster(self):
        print("\n--- Dikdörtgenin Durumu ---")
        print(f"Genişlik: {self.genislik}")
        print(f"Yükseklik: {self.yukseklik}")
        print(f"Alanı: {self.alan}")
        print(f"Çevresi: {self.cevre}")
        print("-" * 27)

def programi_baslat():
    print("----- Dikdörtgen Programı -----")
    
    while True:
        try:
            genislik = float(input("Bir genişlik gir: "))
            yukseklik = float(input("Bir yükseklik gir: "))
            dikdortgen = Dikdortgen(genislik, yukseklik)
            print("\nSüper, dikdörtgen hazır.")
            dikdortgen.bilgileri_goster()
            break
        except ValueError as e:
            print(f"Hata: {e}. Lütfen pozitif bir sayı gir.")

    while True:
        print("\n--- MENÜ ---")
        print("1: Genişliği Değiştir")
        print("2: Yüksekliği Değiştir")
        print("3: Bilgileri Göster")
        print("q: Çıkış")
        
        secim = input("Ne yapmak istersin?: ").strip().lower()

        if secim == 'q':
            print("\nHadi görüşürüz!")
            break
        
        elif secim == '1':
            try:
                yeni_genislik = float(input("Yeni genişliği gir: "))
                dikdortgen.genislik = yeni_genislik
                print("\nTamam, genişlik değişti.")
                dikdortgen.bilgileri_goster()
            except ValueError as e:
                print(f"Hata: {e}")

        elif secim == '2':
            try:
                yeni_yukseklik = float(input("Yeni yüksekliği gir: "))
                dikdortgen.yukseklik = yeni_yukseklik
                print("\nTamam, yükseklik değişti.")
                dikdortgen.bilgileri_goster()
            except ValueError as e:
                print(f"Hata: {e}")
        
        elif secim == '3':
            dikdortgen.bilgileri_goster()
            
        else:
            print("\nYanlış seçim! Menüden birini seç.")

programi_baslat()