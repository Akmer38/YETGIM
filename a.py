"""
İndirilen teknik_veri.json dosyasındaki araçları listele
"""

import json
from collections import defaultdict

def list_all_cars():
    """JSON dosyasındaki tüm araçları listele"""
    
    print("📂 teknik_veri.json dosyası okunuyor...")
    print("=" * 70)
    
    try:
        with open('teknik_veri.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ Dosya başarıyla okundu!")
        print(f"📊 Toplam Kayıt: {len(data) if isinstance(data, list) else 'Dict formatında'}\n")
        
        # Veri yapısını kontrol et
        if isinstance(data, list) and len(data) > 0:
            print("🔍 İlk kayıt yapısı:")
            print(f"Anahtarlar: {list(data[0].keys())}\n")
            
            # Markalara göre grupla
            brands_dict = defaultdict(list)
            
            for item in data:
                # Olası alan isimlerini dene
                brand = (item.get('marka') or item.get('brand') or 
                        item.get('Marka') or item.get('Brand') or 
                        item.get('make') or 'Bilinmiyor')
                
                model = (item.get('model') or item.get('Model') or 
                        item.get('model_adi') or item.get('model_name') or 'Model')
                
                brands_dict[brand].append(model)
            
            # Markaları ve modellerini listele
            print("=" * 70)
            print("🚗 MARKA VE MODEL LİSTESİ")
            print("=" * 70)
            
            total_models = 0
            for brand in sorted(brands_dict.keys()):
                models = list(set(brands_dict[brand]))  # Tekrarları kaldır
                models.sort()
                
                print(f"\n📌 {brand.upper()} ({len(models)} model)")
                print("-" * 70)
                
                for i, model in enumerate(models, 1):
                    print(f"   {i:2d}. {model}")
                    total_models += 1
            
            print("\n" + "=" * 70)
            print(f"✅ Toplam {len(brands_dict)} Marka")
            print(f"✅ Toplam {total_models} Benzersiz Model")
            print("=" * 70)
            
        elif isinstance(data, dict):
            print("📋 JSON yapısı:")
            for key in data.keys():
                print(f"   - {key}")
                
                if isinstance(data[key], list):
                    print(f"     └─ {len(data[key])} öğe")
                    if len(data[key]) > 0:
                        print(f"     └─ Örnek: {data[key][0]}")
        
        return True
        
    except FileNotFoundError:
        print("❌ teknik_veri.json dosyası bulunamadı!")
        print("\n📥 Dosyayı şu şekilde indirebilirsin:")
        print("PowerShell:")
        print('Invoke-WebRequest -Uri "https://huggingface.co/datasets/nezahatkorkmaz/arac-teknik-ozellikler-veriseti/resolve/main/teknik_veri.json" -OutFile "teknik_veri.json"')
        return False
        
    except json.JSONDecodeError:
        print("❌ JSON formatı hatalı!")
        return False
        
    except Exception as e:
        print(f"❌ Hata: {e}")
        return False

if __name__ == "__main__":
    list_all_cars()