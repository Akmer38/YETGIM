import pandas as pd
data = {
    "Ad": ["Ahmet", "Ayşe", "Ali"],
    "Yaş": [18, 20, 19],
    "Şehir": ["İstanbul", "Ankara", "İzmir"],
    "Not": [75, 90, 60]
}

df = pd.DataFrame(data)
df['sonuc'] =df['Not'].apply(lambda x: 'geçti' if x >= 70 else 'kaldı') 
print(df)