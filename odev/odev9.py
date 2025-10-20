class Ogrenci:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
        self.notlar = []

    def not_ekle(self, notu):
        if (isinstance(notu, int) or isinstance(notu, float)) and 0 <= notu <= 100:
            self.notlar.append(notu)
            print("Notun eklendi.")
        else:
            print("Gecersiz not girdin. Not 0 ile 100 arasinda olmali.")

    def ortalama_hesapla(self):
        if not self.notlar:
            return 0.0
        return sum(self.notlar) / len(self.notlar)

    def harf_notu(self):
        ortalama = self.ortalama_hesapla()
        if ortalama >= 90:
            return "AA"
        elif ortalama >= 80:
            return "BA"
        elif ortalama >= 70:
            return "BB"
        elif ortalama >= 60:
            return "CB"
        elif ortalama >= 50:
            return "CC"
        else:
            return "FF"

def ogrenci_sistemini_baslat():
    print("Ogrenci Not Sistemine Hosgeldin")
    
    ad = input("Adini gir: ").strip()
    soyad = input("Soyadini gir: ").strip()
    
    ogrenci = Ogrenci(ad, soyad)
    print("Tamamdir", ogrenci.ad, "seni kaydettim.")

    while True:
        print("\nNe yapmak istersin?")
        print("1 - Not Ekle")
        print("2 - Ortalamami Goster")
        print("3 - Harf Notumu Goster")
        print("4 - Tum Notlarimi Goster")
        print("q - Cikis Yap")

        secim = input("Islem sec: ").strip().lower()

        if secim == 'q':
            print("Gorusuruz", ogrenci.ad, "!")
            break

        elif secim == '1':
            try:
                not_str = input("Eklemek istedigin not: ")
                not_degeri = float(not_str)
                ogrenci.not_ekle(not_degeri)
            except ValueError:
                print("Lutfen sadece sayi gir.")
        
        elif secim == '2':
            ortalama = ogrenci.ortalama_hesapla()
            if ortalama == 0.0:
                print("Daha hic not girmemissin.")
            else:
                print("Not Ortalaman:", ortalama)
        
        elif secim == '3':
            if not ogrenci.notlar:
                 print("Once not girmen lazim.")
            else:
                harf = ogrenci.harf_notu()
                print("Harf Notun:", harf)

        elif secim == '4':
             if not ogrenci.notlar:
                 print("Hic notun yok.")
             else:
                 print("Girdigin Notlar:", ogrenci.notlar)
        
        else:
            print("Gecersiz secim! Menuden birini sec.")

ogrenci_sistemini_baslat()