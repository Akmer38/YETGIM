class Film:
    """Film sınıfı - Her film için nesne"""
    
    def __init__(self, id=None, baslik="", yonetmen="", yil=0, tur="", 
                 puan=0, izlendi=False, notlar=""):
        self.id = id
        self.baslik = baslik
        self.yonetmen = yonetmen
        self.yil = yil
        self.tur = tur
        self.puan = puan
        self.izlendi = izlendi
        self.notlar = notlar
    
    def __str__(self):
        """Film bilgilerini string olarak döndür"""
        durum = "İzlendi ✓" if self.izlendi else "İzlenmedi"
        return f"{self.baslik} ({self.yil}) - {self.yonetmen} - {durum} - ⭐{self.puan}/10"
    
    def to_dict(self):
        """Film nesnesini dictionary'ye çevir"""
        return {
            'id': self.id,
            'baslik': self.baslik,
            'yonetmen': self.yonetmen,
            'yil': self.yil,
            'tur': self.tur,
            'puan': self.puan,
            'izlendi': self.izlendi,
            'notlar': self.notlar
        }