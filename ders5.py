class Arabalar:
    
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
    
    def bilgileri_goster(self):
        print(f"arabanin markasi : {self.marka}")
        print(f"arabanin modeli  : {self.model}")
        print(f"arabanin piyasaya cikis tarihi : {self.yil}")


print("lutfen araba markanizi girin : \n")
marka = input()

print("lutfen arabanizin modelini  girin : \n")
model = input()

print("lutfen arabanizin cikis tarihini girin : \n")
yil = input()

print()

araba1 = Arabalar("toyota", "corolla", "2000")

araba2 = Arabalar(marka, model, yil)

araba1.bilgileri_goster()
print()
araba2.bilgileri_goster()