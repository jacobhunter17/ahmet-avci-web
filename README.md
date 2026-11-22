# Prof. Dr. Ahmet Avcı – Kişisel Web Sitesi

Adres: https://www.ahmetavci7.com (yakında https://www.ahmetavci.com.tr; geçiş için `tools/sayfalar.py` içindeki `SITE` değerini değiştirip sayfaları yeniden üretin)

Sade HTML, CSS ve JavaScript ile yazılmış çok sayfalı site. Vercel'de derleme adımı yoktur.

- `tools/sayfalar.py` – bütün `*.html` sayfaları ve `sitemap.xml` dosyasını üretir. Ortak menü ve alt bölüm burada tek yerdedir. İçerik değişince `python3 tools/sayfalar.py` çalıştırıp çıkan HTML dosyalarını da commit edin.
- `style.css` – tasarım (öneri modeli: lacivert #1F2A44, krem #F6F1E7, eski altın #B8893B)
- `main.js` – menü, animasyonlar, video ve talep türüne göre e-posta açan iletişim formu
- `img/` – görseller

Duyuru şeridi: `tools/sayfalar.py` içindeki `DUYURU` değişkenine metin yazın.

## Yayın
`main` dalına yapılan her değişiklik Vercel'de siteyi otomatik günceller.
Vercel ayarı: Framework Preset = "Other", Build Command boş, Output Directory = `.`
