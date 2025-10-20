class BankaHesabi:
    def __init__(self, hesap_sahibi):
        self.hesap_sahibi = hesap_sahibi
        self.bakiye = 0.0
    def para_yatir(self, miktar):

        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar:.2f} TL yatırıldı.")
            self.bakiye_goster()
        else:
            print("Geçersiz miktar. Lütfen pozitif bir sayı girin.")

    def para_cek(self, miktar):

        if miktar <= 0:

            print("Geçersiz miktar. Lütfen pozitif bir sayı girin.")
        elif self.bakiye >= miktar:
            self.bakiye -= miktar
            print(f"{miktar:.2f} TL çekildi.")
            self.bakiye_goster()
        else:
            print("Yetersiz bakiye!")
            print(f"Çekmek istediğiniz miktar: {miktar:.2f} TL")
            self.bakiye_goster()

    def bakiye_goster(self):
        print(f"Güncel bakiye: {self.bakiye:.2f} TL")


def banka_uygulamasini_baslat():
    print("banka uygulaması")

    isim = input("hesap sahibinin adını girin: ")
    hesap = BankaHesabi(isim)
    print("Hoş geldiniz, Hesabınız oluşturuldu.")

    while True:
        print("işlemler")
        print("1 para yatır")
        print("2 para çek")
        print("3 Bakiye ")
        print("q çıkış ")
    
        secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/q): ").strip().lower()

        if secim == 'q':
            print(f"uygulamadan çıkış yapılıyor")
            break 
        elif secim == '1':
            try:
                miktar_str = input("Yatırmak istediğiniz miktar: ")
                miktar = float(miktar_str)
                hesap.para_yatir(miktar)
            except ValueError:
                print("lütfen geçerli bir sayı girin.")
        
        elif secim == '2':
            try:
                miktar_str = input("Çekmek istediğiniz miktar: ")
                miktar = float(miktar_str)
                hesap.para_cek(miktar)
            except ValueError:
                print("lütfen geçerli bir sayı girin.")
        
        elif secim == '3':
            hesap.bakiye_goster()
        
        else:
            print("Geçersiz seçim! Lütfen menüdeki seçeneklerden birini girin (1, 2, 3 veya q).")

banka_uygulamasini_baslat()