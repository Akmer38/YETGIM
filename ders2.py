ales = int(input("ALES puanınızı giriniz: "))
yds = int(input("YDS puanınızı giriniz: "))
diploma = float(input("diploma puanınızı giriniz: "))

if ales>=60 and yds>=60  and diploma>= 2.5 :
    print("yüksek lisans yapabilirsniz")
else :
    print("yüksek lisans yapamazsınız")



harf = input("Bir harf giriniz: ").lower()  

sesli_harfler = "aeıioöuü"


if harf in sesli_harfler:
    print("Bu bir sesli harftir.")
else:
    print("Bu bir sessiz harftir.")


sayi = int(input("Bir sayı giriniz: "))

toplam = 0

for i in range(1, sayi + 1):
    toplam += i

print( toplam)