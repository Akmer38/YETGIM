class Calisan:
    def __init__(self, ad, soyad, calisan_id):
        self.ad = ad
        self.soyad = soyad
        self.calisan_id = calisan_id

    def maas_hesapla(self):
        raise NotImplementedError("Alt sınıflar bu metodu implemente etmelidir.")
    
    def __str__(self):
        return f"{self.ad} {self.soyad} (ID: {self.calisan_id})"


class TamZamanli(Calisan):
    def __init__(self, ad, soyad, calisan_id, aylik_maas):
        super().__init__(ad, soyad, calisan_id)
        self.aylik_maas = aylik_maas

    def maas_hesapla(self):
        return self.aylik_maas


class YariZamanli(Calisan):
    def __init__(self, ad, soyad, calisan_id, saat_ucreti, calisilan_saat):
        super().__init__(ad, soyad, calisan_id)
        self.saat_ucreti = saat_ucreti
        self.calisilan_saat = calisilan_saat

    def maas_hesapla(self):
        return self.saat_ucreti * self.calisilan_saat


def toplam_maas_hesapla(calisanlar_listesi):
    toplam_maas = 0
    for calisan in calisanlar_listesi:
        toplam_maas += calisan.maas_hesapla()
    return toplam_maas


# --- Örnek Kullanım ---

calisan1 = TamZamanli("Ali", "Veli", 1001, 10000)
calisan2 = YariZamanli("Ayşe", "Demir", 1002, 50, 80)
calisan3 = TamZamanli("Mehmet", "Yılmaz", 1003, 12500)

calisanlar = [calisan1, calisan2, calisan3]

print("--- Bireysel Maaşlar ---")
for calisan in calisanlar:
    print(f"{calisan}: {calisan.maas_hesapla()} TL")

print("\n" + "="*28 + "\n")

toplam_gider = toplam_maas_hesapla(calisanlar)
print(f"Şirketin Toplam Aylık Maaş Gideri: {toplam_gider} TL")