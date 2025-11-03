<img width="1919" height="1019" alt="image" src="https://github.com/user-attachments/assets/a576e934-7af6-460c-bfcc-8c3317d6705f" />Film Kütüphanesi - Flask Projesi
Kişisel film koleksiyonunuzu yönetmek için Python, Flask, OOP ve SQLite kullanılarak oluşturulmuş tam özellikli bir web uygulaması.

Projenin ana sayfasından bir görünüm:

<img width="1894" height="936" alt="image" src="https://github.com/user-attachments/assets/0557ba3e-16cd-4c0a-a7f3-dbcfa4fb4d55" />


📖 Proje Hakkında
Bu proje, kullanıcıların kişisel film arşivlerini oluşturup yönetebilecekleri modern ve dinamik bir web uygulamasıdır. Kullanıcılar koleksiyonlarına film ekleyebilir, mevcut filmlerin bilgilerini düzenleyebilir, izledikleri filmleri işaretleyebilir ve koleksiyonlarıyla ilgili detaylı istatistikleri görüntüleyebilirler.

Proje, Nesne Yönelimli Programlama (OOP) prensipleri kullanılarak modüler bir yapıda geliştirilmiştir. Veritabanı işlemleri ve film nesneleri ayrı sınıflarda (FilmDatabase ve Film) yönetilmektedir.

✨ Temel Özellikler
Tam CRUD İşlevselliği:

Create: Yeni filmler ekle (Başlık, Yönetmen, Yıl, Tür, Puan, Notlar).

Read: Tüm filmleri ana sayfada listele.

Update: Mevcut filmlerin tüm bilgilerini düzenle.

Delete: Filmleri koleksiyondan kalıcı olarak sil.

İzlendi Takibi: Filmleri tek bir tıkla "İzlendi" veya "İzlenmedi" olarak işaretleyin.

İstatistik Sayfası:

Toplam film sayısı

Toplam izlenen film

Toplam izlenmeyen film

Koleksiyondaki filmlerin puan ortalaması

En çok eklenen (favori) film türü

Arama Fonksiyonu: Film başlığına göre koleksiyon içinde anlık arama yapın.

Kalıcı Depolama: Tüm film verileri, filmler.db adında bir SQLite veritabanında saklanır.

Modern Arayüz: Bootstrap 5 ile oluşturulmuş, mobil uyumlu (responsive) ve temiz bir tasarım.

Flash Mesajları: Film ekleme, silme, güncelleme gibi işlemler için kullanıcıyı bilgilendiren bildirimler.

🛠️ Kullanılan Teknolojiler
Backend: Python, Flask

Database: SQLite

Frontend: HTML
