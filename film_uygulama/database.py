import sqlite3
from models import Film

class FilmDatabase:
    """Veritabanı işlemleri için sınıf"""
    
    def __init__(self, db_name="filmler.db"):
        self.db_name = db_name
        self.create_table()
    
    def get_connection(self):
        """Veritabanı bağlantısı oluştur"""
        return sqlite3.connect(self.db_name)
    
    def create_table(self):
        """Film tablosunu oluştur"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                baslik TEXT NOT NULL,
                yonetmen TEXT,
                yil INTEGER,
                tur TEXT,
                puan REAL DEFAULT 0,
                izlendi BOOLEAN DEFAULT 0,
                notlar TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def film_ekle(self, film):
        """Yeni film ekle"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO filmler (baslik, yonetmen, yil, tur, puan, izlendi, notlar)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (film.baslik, film.yonetmen, film.yil, film.tur, 
              film.puan, film.izlendi, film.notlar))
        
        conn.commit()
        film_id = cursor.lastrowid
        conn.close()
        return film_id
    
    def tum_filmleri_getir(self):
        """Tüm filmleri getir"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM filmler ORDER BY baslik')
        rows = cursor.fetchall()
        conn.close()
        
        filmler = []
        for row in rows:
            film = Film(
                id=row[0],
                baslik=row[1],
                yonetmen=row[2],
                yil=row[3],
                tur=row[4],
                puan=row[5],
                izlendi=bool(row[6]),
                notlar=row[7]
            )
            filmler.append(film)
        
        return filmler
    
    def film_getir(self, film_id):
        """ID'ye göre film getir"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM filmler WHERE id = ?', (film_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return Film(
                id=row[0],
                baslik=row[1],
                yonetmen=row[2],
                yil=row[3],
                tur=row[4],
                puan=row[5],
                izlendi=bool(row[6]),
                notlar=row[7]
            )
        return None
    
    def film_guncelle(self, film):
        """Film bilgilerini güncelle"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE filmler 
            SET baslik=?, yonetmen=?, yil=?, tur=?, puan=?, izlendi=?, notlar=?
            WHERE id=?
        ''', (film.baslik, film.yonetmen, film.yil, film.tur, 
              film.puan, film.izlendi, film.notlar, film.id))
        
        conn.commit()
        conn.close()
    
    def film_sil(self, film_id):
        """Film sil"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM filmler WHERE id = ?', (film_id,))
        
        conn.commit()
        conn.close()
    
    def film_ara(self, arama_terimi):
        """Film ara (başlık veya yönetmende)"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM filmler 
            WHERE baslik LIKE ? OR yonetmen LIKE ?
            ORDER BY baslik
        ''', (f'%{arama_terimi}%', f'%{arama_terimi}%'))
        
        rows = cursor.fetchall()
        conn.close()
        
        filmler = []
        for row in rows:
            film = Film(
                id=row[0],
                baslik=row[1],
                yonetmen=row[2],
                yil=row[3],
                tur=row[4],
                puan=row[5],
                izlendi=bool(row[6]),
                notlar=row[7]
            )
            filmler.append(film)
        
        return filmler
    
    def istatistikleri_getir(self):
        """Film istatistiklerini getir"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Toplam film sayısı
        cursor.execute('SELECT COUNT(*) FROM filmler')
        toplam = cursor.fetchone()[0]
        
        # İzlenen film sayısı
        cursor.execute('SELECT COUNT(*) FROM filmler WHERE izlendi = 1')
        izlenen = cursor.fetchone()[0]
        
        # Ortalama puan
        cursor.execute('SELECT AVG(puan) FROM filmler WHERE puan > 0')
        ort_puan = cursor.fetchone()[0] or 0
        
        # En yüksek puanlı film
        cursor.execute('SELECT baslik, puan FROM filmler WHERE puan > 0 ORDER BY puan DESC LIMIT 1')
        en_iyi = cursor.fetchone()
        
        conn.close()
        
        return {
            'toplam': toplam,
            'izlenen': izlenen,
            'izlenmedi': toplam - izlenen,
            'ortalama_puan': round(ort_puan, 1),
            'en_iyi_film': en_iyi[0] if en_iyi else "Henüz yok",
            'en_iyi_puan': en_iyi[1] if en_iyi else 0
        }