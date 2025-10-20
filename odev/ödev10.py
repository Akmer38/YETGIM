class Kitap:
    def __init__(self, baslik, yazar, isbn):
        self.baslik = baslik
        self.yazar = yazar
        self.isbn = isbn
    
    def __str__(self):
        return f"'{self.baslik}', Yazar: {self.yazar}, ISBN: {self.isbn}"


class Kutuphane:
    def __init__(self):
        self.kitaplar = []
    
    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"'{kitap.baslik}' kitabi eklendi.")
    
    def kitap_ara(self, baslik):
        for kitap in self.kitaplar:
            if kitap.baslik.lower() == baslik.lower():
                return kitap
        return None
    
    def kitap_odunc_ver(self, baslik):
        kitap = self.kitap_ara(baslik)
        
        if kitap:
            self.kitaplar.remove(kitap)
            print(f"'{kitap.baslik}' kitabini odunc aldin.")
        else:
            print(f"'{baslik}' diye bir kitap bulamadim.")
    
    def mevcut_kitaplari_goster(self):
        print("\n--- KUTUPHANEDEKI KITAPLAR ---")
        if not self.kitaplar:
            print("Hic kitap kalmamis.")
        else:
            for kitap in self.kitaplar:
                print(f"- {kitap}")
        print("------------------------------")


def kutuphane_sistemini_baslat():
    kutuphane = Kutuphane()
    
    kitap1 = Kitap("Sefiller", "Victor Hugo", "978-1234567890")
    kitap2 = Kitap("1984", "George Orwell", "978-0987654321")
    kutuphane.kitaplar.append(kitap1)
    kutuphane.kitaplar.append(kitap2)
    
    print("Kutuphane Sistemine Hosgeldin")
    print("Bazi kitaplar zaten vardi, sisteme ekledim.")

    while True:
        print("\n--- MENU ---")
        print("1: Kitap Ekle")
        print("2: Kitap Odunc Al")
        print("3: Kitaplari Goster")
        print("q: Cikis")
        
        secim = input("Ne yapmak istersin?: ").strip().lower()

        if secim == 'q':
            print("\nGorusuruz!")
            break
        
        elif secim == '1':
            baslik = input("Kitabin adi: ").strip()
            yazar = input("Yazari kim: ").strip()
            isbn = input("ISBN numarasi: ").strip()
            
            yeni_kitap = Kitap(baslik, yazar, isbn)
            kutuphane.kitap_ekle(yeni_kitap)

        elif secim == '2':
            baslik = input("Odunc almak istedigin kitabin adi: ").strip()
            kutuphane.kitap_odunc_ver(baslik)

        elif secim == '3':
            kutuphane.mevcut_kitaplari_goster()
            
        else:
            print("Gecersiz secim! Menuden birini sec.")

kutuphane_sistemini_baslat()