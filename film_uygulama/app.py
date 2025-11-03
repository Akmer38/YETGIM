from flask import Flask, render_template, request, redirect, url_for, flash
from models import Film
from database import FilmDatabase

app = Flask(__name__)
app.secret_key = 'film-kutuphanesi-secret-key-2024'  # Flash mesajları için gerekli

# Veritabanı nesnesi
db = FilmDatabase()

@app.route('/')
def index():
    """Ana sayfa - Tüm filmler"""
    arama = request.args.get('arama', '')
    
    if arama:
        filmler = db.film_ara(arama)
    else:
        filmler = db.tum_filmleri_getir()
    
    return render_template('index.html', filmler=filmler, arama=arama)

@app.route('/film/ekle', methods=['GET', 'POST'])
def film_ekle():
    """Yeni film ekleme sayfası"""
    if request.method == 'POST':
        # Form verilerini al
        film = Film(
            baslik=request.form['baslik'],
            yonetmen=request.form['yonetmen'],
            yil=int(request.form['yil']) if request.form['yil'] else 0,
            tur=request.form['tur'],
            puan=float(request.form['puan']) if request.form['puan'] else 0,
            izlendi='izlendi' in request.form,
            notlar=request.form['notlar']
        )
        
        # Veritabanına ekle
        db.film_ekle(film)
        flash('Film başarıyla eklendi!', 'success')
        return redirect(url_for('index'))
    
    return render_template('film_ekle.html')

@app.route('/film/duzenle/<int:film_id>', methods=['GET', 'POST'])
def film_duzenle(film_id):
    """Film düzenleme sayfası"""
    film = db.film_getir(film_id)
    
    if not film:
        flash('Film bulunamadı!', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # Form verilerini güncelle
        film.baslik = request.form['baslik']
        film.yonetmen = request.form['yonetmen']
        film.yil = int(request.form['yil']) if request.form['yil'] else 0
        film.tur = request.form['tur']
        film.puan = float(request.form['puan']) if request.form['puan'] else 0
        film.izlendi = 'izlendi' in request.form
        film.notlar = request.form['notlar']
        
        # Veritabanını güncelle
        db.film_guncelle(film)
        flash('Film başarıyla güncellendi!', 'success')
        return redirect(url_for('index'))
    
    return render_template('film_duzenle.html', film=film)

@app.route('/film/sil/<int:film_id>')
def film_sil(film_id):
    """Film silme"""
    db.film_sil(film_id)
    flash('Film silindi!', 'info')
    return redirect(url_for('index'))

@app.route('/istatistikler')
def istatistikler():
    """İstatistikler sayfası"""
    stats = db.istatistikleri_getir()
    filmler = db.tum_filmleri_getir()
    
    # Türlere göre grupla
    turler = {}
    for film in filmler:
        if film.tur:
            turler[film.tur] = turler.get(film.tur, 0) + 1
    
    return render_template('istatistikler.html', stats=stats, turler=turler)

@app.route('/film/izlendi/<int:film_id>')
def izlendi_degistir(film_id):
    """İzlendi durumunu değiştir"""
    film = db.film_getir(film_id)
    if film:
        film.izlendi = not film.izlendi
        db.film_guncelle(film)
        durum = "izlendi" if film.izlendi else "izlenmedi"
        flash(f'Film {durum} olarak işaretlendi!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)