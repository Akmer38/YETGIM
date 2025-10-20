import pandas as pd


veri4 = {
    "Kategori" : ["Elektronik","Kitap","Giyim","Elektronik","Kitap","Giyim","Elektronik", "Kitap", "Giyim"],
    "Satış" : [100,150,200,250,300,350,400,450,500]
}

df4 = pd.DataFrame(veri4)
ortalama_satis = df4['Satış'].mean()
ortalamadan_yuksek_olanlar = df4[df4['Satış'] > ortalama_satis]


print(ortalamadan_yuksek_olanlar)