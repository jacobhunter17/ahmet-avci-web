#!/usr/bin/env python3
"""Sitenin HTML sayfalarını üretir. Ortak üst menü ve alt bölüm burada tek yerde durur.
Kullanım: python3 tools/sayfalar.py   (depo kökünden). Çıktı: kökteki *.html dosyaları."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Yeni alan adı Vercel'de geçerli olunca bunu "https://www.ahmetavci.com.tr" yapın ve sayfaları yeniden üretin.
SITE = "https://www.ahmetavci7.com"
MAIL = "ahmetavci7@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/ahmetavci7/"
SCHOLAR = "https://scholar.google.com/citations?user=0Kvo2tEAAAAJ"
DERGIPARK = "https://dergipark.org.tr/tr/pub/@ahmetavci7"
VIDEO_ID = "k4j9KXiS_m0"
# Duyuru şeridi: yeni kitap ya da yaklaşan seminer olunca buraya yazın (boşsa gösterilmez).
DUYURU = "Duyuru: yeni kitap ve yaklaşan seminer duyuruları burada yer alacak."

MENU = [
    ("hakkimda.html", "Hakkımda"),
    ("kitaplar.html", "Kitaplar"),
    ("konferanslar.html", "Konferanslar"),
    ("videolar.html", "Videolar"),
    ("yazilar.html", "Yazılar"),
    ("iletisim.html", "İletişim"),
]

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%231F2A44'/%3E%3Ctext x='32' y='42' "
           "font-family='Georgia,serif' font-size='28' fill='%23B8893B' text-anchor='middle'%3EAA%3C/text%3E%3C/svg%3E")


def mailto(subject):
    from urllib.parse import quote
    return f"mailto:{MAIL}?subject={quote(subject)}"


def head(path, title, desc):
    url = f"{SITE}/" if path == "index.html" else f"{SITE}/{path}"
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/img/portre.jpg">
<meta property="og:type" content="website">
<meta property="og:locale" content="tr_TR">
<meta name="theme-color" content="#1F2A44">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
"""


def nav(path):
    bar = f'<div class="announce">{DUYURU}</div>\n' if DUYURU else ""
    links = "\n".join(
        f'      <a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{t}</a>' for h, t in MENU)
    return f"""{bar}<header class="nav" id="top">
  <div class="wrap nav-inner">
    <a href="./" class="brand">Prof. Dr. Ahmet Avcı</a>
    <button class="menu-btn" aria-label="Menü" aria-expanded="false">☰</button>
    <nav class="links">
{links}
      <a href="iletisim.html?tur=konferans" class="btn btn-small">Konferans Talebi</a>
    </nav>
  </div>
</header>
"""


FOOTER = f"""<footer class="footer">
  <div class="wrap footer-grid">
    <div>
      <img src="img/portre.jpg" alt="" width="64" height="64" class="footer-photo" loading="lazy">
      <p><strong>Prof. Dr. Ahmet Avcı</strong><br>İstanbul Sabahattin Zaim Üniversitesi öğretim üyesi. Eğitim, yönetim, liderlik, aile ve gençlik üzerine çalışıyor, seminer ve konferanslar veriyor.</p>
    </div>
    <div>
      <h4>Menü</h4>
      <a href="kitaplar.html">Kitaplar</a><a href="konferanslar.html">Konferanslar</a><a href="videolar.html">Videolar</a><a href="yazilar.html">Yazılar</a><a href="akademik.html">Akademik</a><a href="danismanlik.html">Kurumsal Danışmanlık</a><a href="basinda.html">Basında</a><a href="kaynaklar.html">Kaynaklar</a><a href="bulten.html">Bülten</a><a href="en.html">English</a>
    </div>
    <div>
      <h4>İletişim</h4>
      <a href="iletisim.html?tur=konferans">Konferans ve seminer</a><a href="iletisim.html?tur=danismanlik">Eğitim ve danışmanlık</a><a href="iletisim.html?tur=basin">Basın ve röportaj</a><a href="mailto:{MAIL}">{MAIL}</a>
    </div>
    <div>
      <h4>Bülten</h4>
      <form class="mini-bulten" onsubmit="return false"><input type="email" placeholder="E-posta adresiniz" aria-label="E-posta adresiniz" disabled><button class="btn btn-small" disabled>Yakında</button></form>
      <div class="social">
        <a href="#" class="soon" aria-label="YouTube (yakında)" title="Yakında">YouTube</a>
        <a href="#" class="soon" aria-label="Instagram (yakında)" title="Yakında">Instagram</a>
        <a href="#" class="soon" aria-label="X (yakında)" title="Yakında">X</a>
        <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
        <a href="#" class="soon" aria-label="Facebook (yakında)" title="Yakında">Facebook</a>
      </div>
      <a href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar</a><a href="{DERGIPARK}" target="_blank" rel="noopener">DergiPark</a>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>© <span id="y"></span> Prof. Dr. Ahmet Avcı</span>
    <span><a href="kvkk.html">KVKK Aydınlatma Metni</a> · <a href="cerez-politikasi.html">Çerez Politikası</a> · <a href="gizlilik.html">Gizlilik</a></span>
  </div>
</footer>

<script src="main.js"></script>
</body>
</html>
"""


def bos(text="Yakında eklenecek."):
    """İçeriği henüz olmayan alan için yer tutucu."""
    return f'<div class="bos reveal"><span>{text}</span></div>'


def bos_kartlar(n, etiket, cls="bos-kart"):
    return "\n".join(f'      <div class="{cls} reveal"><span>{etiket}</span></div>' for _ in range(n))


def page_hero(eyebrow, title, lead=""):
    lead_html = f'\n    <p class="lead">{lead}</p>' if lead else ""
    return f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title}</h1>{lead_html}
  </div>
</section>
"""


def write(path, title, desc, body):
    html = head(path, title, desc) + nav(path) + "\n<main>\n" + body + "</main>\n\n" + FOOTER
    (ROOT / path).write_text(html, encoding="utf-8")


# ---------- ortak içerik parçaları ----------

TOPICS = [
    ("Başarılı ve Mutlu Olmaya Var mısın?", "Öğrenciler, gençler ve öğretmenler için başarıyı ve mutluluğu birlikte hedefleyen bir yol haritası.", "Öğrenciler · Gençler · Öğretmenler", "ogrenci"),
    ("Kendimizi ve Çocuklarımızı Nasıl Yetiştirelim?", "Aile içi iletişim, anne-baba tutumları ve çocuğun gelişiminde okul-aile iş birliği.", "Veliler · Aileler", "ogrenci"),
    ("Gençlik Dönemi: Sorunlar ve Çözümler", "Gençlerin dünyasını anlamak, doğru iletişim kurmak ve onlara yön göstermek.", "Veliler · Eğitimciler", "egitimci"),
    ("Okulda ve Kurumda Liderlik", "Dönüşümcü liderlik, örgüt kültürü ve ekibe ilham vermek. Okul yöneticileri ve kurum liderleri için.", "Okul yöneticileri · Kurum liderleri", "egitimci"),
    ("Dijital Liderlik ve Proaktif İş Davranışı", "Teknoloji, insan kaynakları ve kurumsal başarı: dijital çağda çözüm üreten ekipler kurmak.", "Şirketler · Kurumlar", "kurum"),
    ("İletişim ve İnsan İlişkileri", "İş hayatında ve ailede etkili iletişim, empati ve güçlü ilişkiler.", "Herkes için", "kurum"),
]


def topic_cards(items):
    return "\n".join(f"""      <article class="card reveal">
        <h3>{t}</h3>
        <p>{d}</p>
        <p class="meta">{m}</p>
      </article>""" for t, d, m, _ in items)


BOOKS = [
    # (başlık, açıklama, ek bilgi, kapak görseli; görsel yoksa "")
    ("Başarılı ve Mutlu Olmaya Var mısın?", "Öğrencilere ve gençlere başarıyla mutluluğu birlikte kurmanın yollarını anlatan bir rehber.", "21. baskı · HBG Yayınları", "basarili-ve-mutlu.jpg"),
    ("Kendimizi ve Çocuklarımızı Nasıl Yetiştirelim?", "Aile içi iletişim, anne-baba tutumları ve çocuk yetiştirme üzerine anne ve babalar için bir kitap.", "", "kendimizi-ve-cocuklarimizi.jpg"),
    ("Dijital Liderlik ve Proaktif İş Davranışları İlişkisi", "Bireysel özümseme kapasitesi ve katılımcı insan kaynakları uygulamalarının rolü.", "Gece Kitaplığı", "dijital-liderlik.jpg"),
    ("Personel Güçlendirme, Örgütsel Adanmışlık, İş Tatmini", "Kurumsal Başarının Anahtarı 1. Eğitim yönetimi açısından analiz ve değerlendirme.", "Gece Kitaplığı", "kurumsal-basari-1.jpg"),
    ("Psikolojik Sermaye, Çalışan Esenliği, Örgütsel Dayanıklılık, İş Yaşamında Anlam ve Amaç", "Kurumsal Başarının Anahtarı 2. Eğitim yönetimi açısından analiz ve değerlendirme.", "Gece Kitaplığı", "kurumsal-basari-2.jpg"),
    ("Eğitim Bilimine Giriş", "Eğitim bilimlerinin temel konularını bir arada ele alan kapsamlı bir kaynak kitap.", "12 bölüm · 1.008 sayfa", ""),
]


def book_cards():
    return "\n".join(f"""      <article class="book reveal">{f'<img class="cover-img" src="img/kitaplar/{c}" alt="{t} kitap kapağı" width="600" height="900" loading="lazy">' if c else f'<div class="cover">{t}</div>'}<h3>{t}</h3><p>{d}</p>{f'<p class="meta">{m}</p>' if m else ''}<p class="book-links"><span class="soon-pill">İlk bölümü indir · yakında</span><span class="soon-pill">Satın al · yakında</span></p></article>""" for t, d, m, c in BOOKS)


VIDEO = f"""<div class="video reveal">
  <a class="video-facade" href="https://www.youtube.com/watch?v={VIDEO_ID}" data-yt="{VIDEO_ID}" target="_blank" rel="noopener" aria-label="Videoyu oynat: Prof. Dr. Ahmet Avcı konuşması">
    <img src="https://i.ytimg.com/vi/{VIDEO_ID}/hqdefault.jpg" alt="" loading="lazy">
    <span class="play" aria-hidden="true">▶</span>
  </a>
</div>"""

STATS = """  <div class="wrap stats reveal">
    <div><strong>2</strong><span>doktora</span></div>
    <div><strong>6</strong><span>kitap</span></div>
    <div><strong>30+</strong><span>hakemli makale</span></div>
    <div><strong>850+</strong><span>akademik atıf</span></div>
    <div><strong>3</strong><span>kurucusu olduğu üniversite merkezi</span></div>
  </div>"""

PUBS = [
    ("2015", "Investigation of transformational and transactional leadership styles of school principals, and evaluation of them in terms of educational administration", "Educational Research and Reviews, 10(20) · 175 atıf"),
    ("2015", "Öğretmen algılarına göre okul müdürlerinin liderlik stilleri", "HAYEF Journal of Education, 12(2) · 106 atıf"),
    ("2016", "Effect of Leadership Styles of School Principals on Organizational Citizenship Behaviors", "Educational Research and Reviews, 11(11) · 80 atıf"),
    ("2015", "Örgütsel vatandaşlık davranışları: Kavramsal gelişimi ve eğitim örgütleri açısından etkileri", "Hasan Âli Yücel Eğitim Fakültesi Dergisi, 12(24) · 67 atıf"),
    ("2010", "Aile yapı ve atmosferinin okul şiddetine etkisi", "Değerler Eğitimi Dergisi, 8(19) · 63 atıf"),
    ("2015", "Dönüşümcü ve işlemci liderlik stilleri: Kavramsal çerçevesi ve eğitim örgütleri açısından etkileri", "FSM İlmî Araştırmalar İnsan ve Toplum Bilimleri Dergisi · 53 atıf"),
    ("2017", "Psychological needs as the predictor of teachers' perceived stress levels", "A. Avcı, H. Bozgeyikli, Ş. Kesici · Journal of Education and Training Studies, 5(4) · 36 atıf"),
    ("2025", "Psikolojik sermaye ile duygusal tükenmişlik arasındaki ilişkide algılanan mesleki stresin aracı etkisi: Öğretmenler üzerine bir çalışma", 'E. E. Boğazlıyan, A. Avcı · Adıyaman Üniversitesi Sosyal Bilimler Enstitüsü Dergisi · <a href="https://doi.org/10.14520/adyusbd.1782434" target="_blank" rel="noopener">DOI</a>'),
]

TIMELINE = [
    ("2024–", "Öğretim Üyesi, İstanbul Sabahattin Zaim Üniversitesi. İZÜSEM ve ÖGEM yönetim kurulu üyesi"),
    ("2022", "Genel Müdür Yardımcısı, Türkiye Katılım Sigorta (kuruluş ekibi): İnsan Kaynakları, Finans, Bilgi Teknolojileri, Kurumsal İletişim ve Tedarik"),
    ("2020–2023", "Türkiye Sigorta: Eğitim, Gelişim ve Akademi Direktörü, ardından CEO Ofis Direktörü"),
    ("", "İkinci doktora: Dijital Liderlik ve Proaktif İş Davranışı, Bireysel Özümseme Kapasitesi ve Katılımcı İnsan Kaynaklarının Rolü"),
    ("2018", "Kurucu Müdür ve Yönetim Kurulu Başkanı, Sosyal İş Birlikleri Bölgesi Uygulama ve Araştırma Merkezi (SOSYOPARK)"),
    ("2014–2016", "Kurucu Müdür, Kariyer, Girişimcilik ve Mesleki Test Merkezi (FSMKAM)"),
    ("2010–2018", "Kurucu Müdür ve Yönetim Kurulu Başkanı, Sürekli Eğitim Uygulama ve Araştırma Merkezi (FSMSEM)"),
    ("2010", "Eğitim Bilimleri Bölümü öğretim üyesi, Fatih Sultan Mehmet Vakıf Üniversitesi"),
    ("2002–2010", "Lisans (2002), yüksek lisans (2005) ve doktora (2010), Marmara Üniversitesi"),
]

# ---------- sayfalar ----------

def build():
    # Ana sayfa
    write("index.html",
          "Prof. Dr. Ahmet Avcı | Akademisyen, Yazar, Konuşmacı",
          "Prof. Dr. Ahmet Avcı: akademisyen, yönetici, yazar ve keynote speaker. Eğitim, yönetim, liderlik, aile ve gençlik üzerine seminer ve konferanslar.",
          f"""<section class="hero">
  <div class="wrap hero-inner">
    <div class="hero-text reveal">
      <p class="eyebrow">Akademisyen · Yönetici · Yazar · Keynote Speaker</p>
      <h1>Başarılı ve mutlu bir hayat için <span>bilim, tecrübe ve değer</span></h1>
      <p class="lead">Prof. Dr. Ahmet Avcı, İstanbul Sabahattin Zaim Üniversitesi öğretim üyesi. Üniversite, kamu ve özel sektördeki yöneticilik tecrübesini eğitim, yönetim, aile ve gençlik üzerine seminerlerle buluşturuyor.</p>
      <div class="cta">
        <a href="kitaplar.html" class="btn">Kitapları İnceleyin</a>
        <a href="iletisim.html?tur=konferans" class="btn btn-ghost">Konferans Talebi</a>
      </div>
    </div>
    <div class="hero-photo reveal">
      <img src="img/portre.jpg" alt="Prof. Dr. Ahmet Avcı" width="330" height="330">
    </div>
  </div>
{STATS}
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow reveal">Size uygun içerik</p>
    <h2 class="reveal">Kim için ne var?</h2>
    <div class="doors">
      <a class="door reveal" href="kitaplar.html"><span class="door-k">Öğrenci &amp; Aile</span><h3>Başarı, mutluluk ve aile içi iletişim</h3><p>Gençler ve anne-babalar için kitaplar ve seminerler.</p><span class="more">Kitaplara göz atın →</span></a>
      <a class="door reveal" href="konferanslar.html#egitimciler"><span class="door-k">Eğitimci &amp; Okul</span><h3>Okulda liderlik ve öğretmen gelişimi</h3><p>Okul yöneticileri ve öğretmenler için seminer ve mesleki gelişim programları.</p><span class="more">Seminer konuları →</span></a>
      <a class="door reveal" href="danismanlik.html"><span class="door-k">Kurum &amp; Şirket</span><h3>Dijital liderlik, insan kaynakları ve yönetim</h3><p>Kurumlar için konferans, kurumsal eğitim ve yönetim danışmanlığı.</p><span class="more">Kurumsal hizmetler →</span></a>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap two-col">
    <div class="reveal">
      <p class="eyebrow">Tanıtım</p>
      <h2>Sahneden bir kesit</h2>
      <p>1–2 dakikalık tanıtım videosu hazırlanınca buraya gelecek. Şimdilik konuşmalarından bir kesit. Diğer videolar için <a href="videolar.html">Videolar</a> sayfasına bakabilirsiniz.</p>
    </div>
    {VIDEO}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Kitaplar</p><h2>Yazdığı kitaplar</h2></div><a href="kitaplar.html" class="all">Tümü →</a></div>
    <div class="books">
{book_cards()}
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">YouTube</p><h2>Son videolar</h2></div><a href="videolar.html" class="all">Tüm videolar →</a></div>
    <div class="bos-grid">
{bos_kartlar(3, "Video yakında", "bos-kart video-kart")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Konferans ve Seminerler</p><h2>Kurumunuz için konuşma başlıkları</h2></div><a href="konferanslar.html" class="all">Tüm konular →</a></div>
    <div class="cards">
{topic_cards(TOPICS)}
    </div>
    <p class="eyebrow reveal logos-title">Konuşma yaptığı kurumlar</p>
    <div class="logos">
{bos_kartlar(6, "Logo", "bos-logo")}
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <p class="eyebrow reveal">Yorumlar</p>
    <h2 class="reveal">Dinleyenler ne diyor?</h2>
    <div class="bos-grid">
{bos_kartlar(3, "Kurum yöneticileri, öğretmenler, aileler ve öğrencilerden yorumlar yakında", "bos-kart yorum-kart")}
    </div>
  </div>
</section>

<section class="section bulten">
  <div class="wrap bulten-inner reveal">
    <div><p class="eyebrow">Bülten</p><h2>Kitabın ilk bölümünü ücretsiz alın</h2><p>Aylık e-posta bültenine kaydolun, yeni yazılar ve seminerlerden ilk siz haberdar olun.</p></div>
    <form class="bulten-form" onsubmit="return false"><input type="email" placeholder="E-posta adresiniz" aria-label="E-posta adresiniz" disabled><button class="btn" disabled>Yakında</button></form>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Yazılar</p><h2>Son yazılar</h2></div><a href="yazilar.html" class="all">Tüm yazılar →</a></div>
    <div class="bos-grid">
{bos_kartlar(3, "Yazı yakında")}
    </div>
  </div>
</section>

<section class="section band">
  <div class="wrap band-inner reveal">
    <div><h2>Etkinliğinize konuşmacı mı arıyorsunuz?</h2><p>Seminer, konferans, panel, moderatörlük ve kurumsal eğitim talepleriniz için yazın.</p></div>
    <a href="iletisim.html?tur=konferans" class="btn">Konferans Talebi</a>
  </div>
</section>
""")

    # Hakkımda
    tl = "\n".join(f'      <li class="reveal"><span>{y}</span>{t}</li>' for y, t in TIMELINE)
    write("hakkimda.html",
          "Hakkımda | Prof. Dr. Ahmet Avcı",
          "Prof. Dr. Ahmet Avcı'nın biyografisi ve kariyer zaman çizelgesi: Marmara Üniversitesi, FSMVÜ, Türkiye Sigorta, Türkiye Katılım Sigorta ve İstanbul Sabahattin Zaim Üniversitesi.",
          page_hero("Hakkımda", "Akademiden yönetim masasına, kürsüden ekrana",
                    "Akademisyen, yönetici, yazar, moderatör, TV programı yapımcısı ve keynote speaker.") +
          f"""<section class="section">
  <div class="wrap two-col">
    <div class="reveal">
      <img src="img/portre.jpg" alt="Prof. Dr. Ahmet Avcı" width="330" height="330" class="about-photo">
      <h3 class="small-h">Çalışma alanları</h3>
      <div class="tags">
        <span>İşletme Yönetimi ve Organizasyon</span><span>Eğitim Yönetimi ve Denetimi</span><span>Örgütsel Davranış</span><span>Liderlik</span><span>Örgüt Kültürü</span><span>İnsan Kaynakları Yönetimi</span><span>İnsan İlişkileri ve İletişim</span><span>Aile, Gençlik ve Eğitim</span>
      </div>
    </div>
    <div class="reveal prose">
      <p>İstanbul'da doğan Prof. Dr. Ahmet Avcı; 2002'de lisans, 2005'te yüksek lisans ve 2010'da doktora eğitimini Marmara Üniversitesi'nde tamamladı. 2010 yılında Fatih Sultan Mehmet Vakıf Üniversitesi Eğitim Bilimleri Bölümü'nde akademik kariyerine başladı. Aynı yıl Sürekli Eğitim Uygulama ve Araştırma Merkezi'nin (FSMSEM) kurucu müdürlüğünü üstlendi ve merkezi 2010–2018 yılları arasında yönetti. 2014'te Kariyer, Girişimcilik ve Mesleki Test Merkezi'ni (FSMKAM), 2018'de ise tasarımında ve geliştirilmesinde aktif rol aldığı SOSYOPARK'ı kurucu müdür olarak hayata geçirdi.</p>
      <p>2020–2023 yılları arasında Varlık Fonu bünyesindeki kurumlarda üst düzey yöneticilik yaptı. Türkiye Sigorta'da önce Eğitim, Gelişim ve Akademi Direktörlüğünü, ardından CEO Ofis Direktörlüğünü yürüttü. 2022'de Türkiye Katılım Sigorta'nın kuruluşunda aktif rol aldı; İnsan Kaynakları, Finans, Bilgi Teknolojileri, Kurumsal İletişim ve Tedarik birimlerini Genel Müdür Yardımcısı olarak yönetti.</p>
      <p>Ulusal ve uluslararası birçok araştırma ve projede proje başkanı, yürütücü, tasarımcı ve koordinatör olarak görev aldı. Araştırma, eğitim ve danışmanlık şirketlerinde eğitim koordinatörü, proje direktörü ve genel müdür olarak çalıştı; birçok firmaya yönetim danışmanlığı verdi. Pek çok radyo ve televizyon programına konuk oldu; eğitim, kültür ve yönetim konularını ele aldığı “Artılar ve Eksiler” programını hazırlayıp sundu.</p>
      <p>“Dijital Liderlik ve Proaktif İş Davranışı, Bireysel Özümseme Kapasitesi ve Katılımcı İnsan Kaynaklarının Rolü” başlıklı ikinci doktorasıyla, kurumların teknoloji, insan kaynakları ve kurumsal başarı bağlamında yararlanabileceği bir rehber ortaya koydu. Altı kitabı ve ulusal ve uluslararası hakemli dergilerde 30'un üzerinde makalesi bulunuyor.</p>
      <p>2024'ten bu yana İstanbul Sabahattin Zaim Üniversitesi'nde öğretim üyesi olarak görev yapıyor; Sürekli Eğitim Uygulama ve Araştırma Merkezi (İZÜSEM) ile Öğretim ve Öğrenmeyi Geliştirme Uygulama ve Araştırma Merkezi'nin (ÖGEM) yönetim kurullarında yer alıyor. Birçok sivil toplum kuruluşunda çalışıyor ve sosyal sorumluluk projelerine destek veriyor.</p>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <p class="eyebrow reveal">Kariyer</p>
    <h2 class="reveal">Zaman çizelgesi</h2>
    <ul class="timeline">
{tl}
    </ul>
    <p class="reveal"><a class="btn btn-disabled" aria-disabled="true">CV indir (PDF) · yakında</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow reveal">Fotoğraflar</p>
    <h2 class="reveal">Galeri</h2>
    <div class="bos-grid gallery">
{bos_kartlar(6, "Fotoğraf yakında", "bos-kart foto-kart")}
    </div>
  </div>
</section>
""")

    # Kitaplar
    write("kitaplar.html",
          "Kitaplar | Prof. Dr. Ahmet Avcı",
          "Prof. Dr. Ahmet Avcı'nın kitapları: Başarılı ve Mutlu Olmaya Var mısın?, Kendimizi ve Çocuklarımızı Nasıl Yetiştirelim?, Dijital Liderlik, Kurumsal Başarının Anahtarı serisi ve Eğitim Bilimine Giriş.",
          page_hero("Kitaplar", "Yazdığı kitaplar",
                    "Öğrenciler, aileler, eğitimciler ve yöneticiler için yazılmış kitaplar.") +
          f"""<section class="section">
  <div class="wrap">
    <div class="books books-lg">
{book_cards()}
    </div>
    <p class="reveal note-box">Kitapları satın almak veya toplu sipariş ve imza günü için <a href="iletisim.html?tur=genel">bize yazın</a>.</p>
  </div>
</section>
""")

    # Konferanslar
    ogr = [t for t in TOPICS if t[3] in ("ogrenci", "egitimci")]
    kur = [t for t in TOPICS if t[3] == "kurum"]
    write("konferanslar.html",
          "Konferans ve Seminerler | Prof. Dr. Ahmet Avcı",
          "Okullar, kurumlar ve şirketler için seminer, konferans, panel, moderatörlük, kurumsal eğitim ve yönetim danışmanlığı.",
          page_hero("Konferans ve Seminerler", "Konuşma konuları ve kurumsal hizmetler",
                    "Seminer, konferans, panel, moderatörlük, kurumsal eğitim ve yönetim danışmanlığı.") +
          f"""<section class="section" id="egitimciler">
  <div class="wrap">
    <p class="eyebrow reveal">Öğrenciler, aileler ve eğitimciler için</p>
    <h2 class="reveal">Okullar ve eğitim kurumları</h2>
    <div class="cards">
{topic_cards(ogr)}
    </div>
  </div>
</section>

<section class="section alt" id="kurumlar">
  <div class="wrap">
    <p class="eyebrow reveal">Kurumlar ve şirketler için</p>
    <h2 class="reveal">Kurumsal eğitim ve danışmanlık</h2>
    <div class="cards">
{topic_cards(kur)}
      <article class="card reveal">
        <h3>Yönetim Danışmanlığı</h3>
        <p>Örgüt kültürü, insan kaynakları ve kurum içi eğitim akademisi kurulumu. Türkiye Sigorta ve Türkiye Katılım Sigorta'daki üst düzey yöneticilik tecrübesiyle.</p>
        <p class="meta">Şirketler · Kamu kurumları · Okullar</p>
      </article>
    </div>
    <p class="reveal note-box">Danışmanlık ve eğitim paketlerinin ayrıntıları için <a href="danismanlik.html">Kurumsal Danışmanlık</a> sayfasına bakın.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow reveal">Takvim</p>
    <h2 class="reveal">Yaklaşan seminerler</h2>
    {bos("Yaklaşan seminer ve konferanslar burada listelenecek.")}
    <p class="eyebrow reveal logos-title">Konuşma yaptığı kurumlar</p>
    <div class="logos">
{bos_kartlar(6, "Logo", "bos-logo")}
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap two-col">
    <div class="reveal">
      <p class="eyebrow">Geçmiş etkinliklerden</p>
      <h2>Sahneden</h2>
      <ul class="plain">
        <li><strong>Başarılı ve Mutlu Öğrenciler Yetiştirmek</strong><br>İzmir İl Milli Eğitim Müdürlüğü Mesleki Gelişim Akademisi, Mart 2018. <a href="https://izmir.meb.gov.tr/www/basarili-ve-mutlu-ogrenciler-yetistirmek-icin-ogretmenler-ve-idareciler-bir-arada/icerik/1345" target="_blank" rel="noopener">Haberi oku →</a></li>
        <li><strong>Artılar ve Eksiler</strong><br>Eğitim, kültür ve yönetim konularını ele aldığı, hazırlayıp sunduğu televizyon programı.</li>
      </ul>
    </div>
    {VIDEO}
  </div>
</section>

<section class="section band">
  <div class="wrap band-inner reveal">
    <div><h2>Etkinliğiniz için tarih ayıralım</h2><p>Etkinliğin türünü, tarihini ve katılımcı kitlesini yazmanız yeterli.</p></div>
    <a href="iletisim.html?tur=konferans" class="btn">Konferans Talebi</a>
  </div>
</section>
""")

    # Akademik
    pubs = "\n".join(f'      <li class="reveal"><span class="year">{y}</span><div><strong>{t}</strong><em>{m}</em></div></li>' for y, t, m in PUBS)
    write("akademik.html",
          "Akademik Çalışmalar | Prof. Dr. Ahmet Avcı",
          "Prof. Dr. Ahmet Avcı'nın akademik yayınları: eğitim yönetimi, liderlik, örgüt kültürü ve örgütsel vatandaşlık üzerine makaleler.",
          page_hero("Akademik", "Akademik çalışmalar",
                    "Eğitim yönetimi, işletme yönetimi, liderlik, örgüt kültürü ve örgütsel vatandaşlık alanlarında 30'un üzerinde hakemli makale ve 850'nin üzerinde atıf.") +
          f"""<section class="section">
  <div class="wrap">
    <h2 class="reveal">En çok atıf alan yayınlar</h2>
    <ul class="pubs">
{pubs}
    </ul>
    <p class="reveal profiles">Tüm yayınlar: <a href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar</a> · <a href="{DERGIPARK}" target="_blank" rel="noopener">DergiPark</a> · <span class="soon-pill">ORCID · yakında</span></p>
  </div>
</section>

<section class="section alt">
  <div class="wrap two-col">
    <div class="reveal">
      <h2>Projeler</h2>
      {bos("Yürüttüğü ulusal ve uluslararası projeler yakında eklenecek.")}
    </div>
    <div class="reveal">
      <h2>Verdiği dersler</h2>
      {bos("Lisans ve lisansüstü dersler yakında eklenecek.")}
    </div>
  </div>
</section>
""")

    # Medya
    write("basinda.html",
          "Basında | Prof. Dr. Ahmet Avcı",
          "Prof. Dr. Ahmet Avcı'nın televizyon programları, konuşma videoları ve basında yer alan haberleri.",
          page_hero("Basında", "Röportajlar, programlar ve haberler", "Tarih, kanal ve bağlantılarıyla basında yer alan haberler.") +
          f"""<section class="section">
  <div class="wrap">
    <h2 class="reveal">Program ve haberler</h2>
    <div class="events">
      <article class="event reveal">
        <span class="date">Televizyon</span>
        <h3>Artılar ve Eksiler</h3>
        <p>Eğitim, kültür ve yönetim konularının işlendiği, Ahmet Avcı'nın hazırlayıp sunduğu televizyon programı.</p>
      </article>
      <article class="event reveal">
        <span class="date">Mart 2018 · İzmir İl MEM</span>
        <h3>Başarılı ve Mutlu Öğrenciler Yetiştirmek</h3>
        <p>Mesleki Gelişim Akademisi kapsamında öğretmen ve idarecilere verilen seminer.</p>
        <a href="https://izmir.meb.gov.tr/www/basarili-ve-mutlu-ogrenciler-yetistirmek-icin-ogretmenler-ve-idareciler-bir-arada/icerik/1345" target="_blank" rel="noopener">Haberi oku →</a>
      </article>
    </div>
    <h2 class="reveal" style="margin-top:60px">Röportajlar</h2>
    {bos("Röportajlar tarih ve kanal bilgisiyle burada listelenecek.")}
    <p class="reveal note-box">Röportaj ve basın talepleri için <a href="iletisim.html?tur=basin">iletişim formunu</a> kullanabilirsiniz.</p>
  </div>
</section>
""")

    # İletişim
    write("iletisim.html",
          "İletişim | Prof. Dr. Ahmet Avcı",
          "Konferans, seminer, kurumsal eğitim, danışmanlık ve basın talepleriniz için Prof. Dr. Ahmet Avcı ile iletişime geçin.",
          page_hero("İletişim", "Talebinizi iletin",
                    "Konferans, seminer, panel, moderatörlük, kurumsal eğitim, danışmanlık ve basın talepleriniz için yazın.") +
          f"""<section class="section">
  <div class="wrap two-col">
    <div class="reveal">
      <h3>E-posta</h3>
      <p class="contact-line">✉ <a href="mailto:{MAIL}">{MAIL}</a></p>
      <h3>Talep türleri</h3>
      <ul class="plain">
        <li><a href="{mailto('Konferans / Seminer Talebi')}">Konferans ve seminer</a></li>
        <li><a href="{mailto('Kurumsal Eğitim / Danışmanlık Talebi')}">Kurumsal eğitim ve danışmanlık</a></li>
        <li><a href="{mailto('Basın / Röportaj Talebi')}">Basın ve röportaj</a></li>
      </ul>
      <p class="contact-line"><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a> · <a href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar</a></p>
    </div>
    <form class="form reveal" id="davet">
      <label>Talep türü
        <select name="tur" id="tur">
          <option value="konferans">Konferans / Seminer</option>
          <option value="danismanlik">Kurumsal Eğitim / Danışmanlık</option>
          <option value="basin">Basın / Röportaj</option>
          <option value="genel">Genel</option>
        </select>
      </label>
      <label>Ad Soyad<input required name="ad" autocomplete="name"></label>
      <label>Kurum<input name="kurum" autocomplete="organization"></label>
      <label>E-posta<input type="email" required name="eposta" autocomplete="email"></label>
      <label>Mesajınız (etkinlik türü, tarih, yer, katılımcı sayısı)<textarea rows="5" name="mesaj" required></textarea></label>
      <p class="form-note">Gönder'e bastığınızda e-posta uygulamanız hazır bir mesajla açılır. Bilgileriniz sitede saklanmaz. Ayrıntılar: <a href="kvkk.html">KVKK Aydınlatma Metni</a>.</p>
      <button class="btn" type="submit">E-posta ile Gönder</button>
    </form>
  </div>
</section>
""")

    # Videolar
    write("videolar.html", "Videolar | Prof. Dr. Ahmet Avcı",
          "Prof. Dr. Ahmet Avcı'nın konuşma, seminer ve program videoları.",
          page_hero("Videolar", "Konuşmalar ve programlar", "YouTube kanalındaki videolar, çalma listelerine göre.") +
          f"""<section class="section">
  <div class="wrap two-col">
    <div class="reveal"><p class="eyebrow">Öne çıkan</p><h2>Prof. Dr. Ahmet Avcı konuşması</h2></div>
    {VIDEO}
  </div>
</section>
<section class="section alt">
  <div class="wrap">
    <div class="filters reveal"><span class="soon-pill">Seminerler</span><span class="soon-pill">Aile</span><span class="soon-pill">Gençlik</span><span class="soon-pill">Yönetim</span><span class="soon-pill">TV programları</span></div>
    <div class="bos-grid">
{bos_kartlar(6, "Video yakında", "bos-kart video-kart")}
    </div>
  </div>
</section>
""")

    # Yazılar
    write("yazilar.html", "Yazılar | Prof. Dr. Ahmet Avcı",
          "Prof. Dr. Ahmet Avcı'nın öğrenci, aile, eğitimci, hayat, iş ve yönetim üzerine yazıları.",
          page_hero("Yazılar", "Yazılar ve makaleler", "Öğrenci, aile, eğitimci, hayat, iş ve yönetim üzerine.") +
          f"""<section class="section">
  <div class="wrap">
    <div class="filters reveal"><span class="soon-pill">Öğrenci</span><span class="soon-pill">Aile</span><span class="soon-pill">Eğitimci</span><span class="soon-pill">Hayat</span><span class="soon-pill">İş ve Yönetim</span></div>
    <div class="bos-grid">
{bos_kartlar(6, "Yazı yakında")}
    </div>
  </div>
</section>
""")

    # Kurumsal Danışmanlık
    write("danismanlik.html", "Kurumsal Danışmanlık | Prof. Dr. Ahmet Avcı",
          "Okullar, kolejler ve şirketler için kurumsal eğitim ve yönetim danışmanlığı.",
          page_hero("Kurumsal Danışmanlık", "Okullar ve şirketler için danışmanlık ve eğitim",
                    "Üniversite, kamu ve özel sektördeki üst düzey yöneticilik tecrübesiyle.") +
          f"""<section class="section">
  <div class="wrap">
    <div class="cards">
      <article class="card reveal"><h3>Okullar ve kolejler</h3><p>Okul liderliği, öğretmen gelişimi ve okul-aile iş birliği programları.</p>{bos("Paket ayrıntıları yakında.")}</article>
      <article class="card reveal"><h3>Şirketler</h3><p>Dijital liderlik, insan kaynakları, örgüt kültürü ve kurum içi akademi kurulumu.</p>{bos("Paket ayrıntıları yakında.")}</article>
      <article class="card reveal"><h3>Kamu ve STK'lar</h3><p>Yönetim, organizasyon ve eğitim programlarının tasarımı.</p>{bos("Paket ayrıntıları yakında.")}</article>
    </div>
    <p class="reveal note-box">Görüşme talebi için <a href="iletisim.html?tur=danismanlik">iletişim formunu</a> kullanabilirsiniz.</p>
  </div>
</section>
""")

    # Kaynaklar
    write("kaynaklar.html", "Kaynaklar | Prof. Dr. Ahmet Avcı",
          "Ücretsiz çalışma kâğıtları, testler ve sunum özetleri.",
          page_hero("Kaynaklar", "Ücretsiz kaynaklar", "Öğrenciler, aileler ve eğitimciler için çalışma kâğıtları, testler ve sunum özetleri.") +
          f"""<section class="section">
  <div class="wrap">
    <h2 class="reveal">Çalışma kâğıtları</h2>
    <div class="bos-grid">
{bos_kartlar(3, "Çalışma kâğıdı yakında")}
    </div>
    <h2 class="reveal" style="margin-top:60px">Testler</h2>
    <div class="bos-grid">
{bos_kartlar(3, "Test yakında")}
    </div>
    <h2 class="reveal" style="margin-top:60px">Sunum özetleri</h2>
    <div class="bos-grid">
{bos_kartlar(3, "Sunum özeti yakında")}
    </div>
  </div>
</section>
""")

    # Bülten
    write("bulten.html", "Bülten | Prof. Dr. Ahmet Avcı",
          "Prof. Dr. Ahmet Avcı'nın aylık e-posta bülteni.",
          page_hero("Bülten", "Aylık e-posta bülteni", "Kaydolanlara hediye: kitaptan ilk bölüm.") +
          f"""<section class="section">
  <div class="wrap narrow">
    <form class="bulten-form reveal" onsubmit="return false"><input type="email" placeholder="E-posta adresiniz" aria-label="E-posta adresiniz" disabled><button class="btn" disabled>Yakında</button></form>
    {bos("Bülten kaydı yakında açılacak.")}
  </div>
</section>
""")

    # English
    write("en.html", "Prof. Dr. Ahmet Avcı | English",
          "Prof. Dr. Ahmet Avcı: academic, executive, author and keynote speaker.",
          page_hero("English", "Prof. Dr. Ahmet Avcı", "Academic, executive, author and keynote speaker.") +
          f"""<section class="section">
  <div class="wrap narrow">
    {bos("English summary coming soon.")}
  </div>
</section>
""")

    # Yasal metinler
    legal_note = '<p class="legal-meta">Son güncelleme: 22 Kasım 2026</p>'
    write("kvkk.html", "KVKK Aydınlatma Metni | Prof. Dr. Ahmet Avcı",
          "6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamında aydınlatma metni.",
          page_hero("Yasal", "KVKK Aydınlatma Metni") + f"""<section class="section"><div class="wrap prose narrow">
{legal_note}
<p>Bu metin, 6698 sayılı Kişisel Verilerin Korunması Kanunu'nun (“KVKK”) 10. maddesi uyarınca, {SITE.split('//')[1]} adresindeki internet sitesinin ziyaretçilerini bilgilendirmek amacıyla hazırlanmıştır.</p>
<h3>Veri sorumlusu</h3>
<p>Prof. Dr. Ahmet Avcı. İletişim: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h3>İşlenen kişisel veriler ve amaçları</h3>
<p>Site üzerinde form verisi saklanmaz ve üyelik sistemi yoktur. İletişim formunu doldurduğunuzda bilgileriniz (ad soyad, kurum, e-posta, mesaj) yalnızca kendi e-posta uygulamanızda bir taslak oluşturmak için kullanılır ve siz göndermeyi seçerseniz e-posta yoluyla tarafımıza ulaşır. Bize e-posta ile ilettiğiniz kimlik ve iletişim bilgileri; talebinizi değerlendirmek, size dönüş yapmak ve etkinlik organizasyonunu yürütmek amacıyla işlenir.</p>
<h3>Hukuki sebep</h3>
<p>Kişisel verileriniz, KVKK'nın 5. maddesinin 2. fıkrasındaki “bir sözleşmenin kurulması veya ifasıyla doğrudan doğruya ilgili olması” ve “veri sorumlusunun meşru menfaati” hukuki sebeplerine dayanılarak işlenir.</p>
<h3>Aktarım</h3>
<p>E-posta yazışmaları Google LLC tarafından sağlanan e-posta hizmeti üzerinden yürütülür; bu nedenle verileriniz yurt dışındaki sunuculara aktarılabilir. Site, Vercel Inc. altyapısında barındırılmakta ve yazı tipleri Google Fonts üzerinden yüklenmektedir; bu hizmetler teknik olarak IP adresinizi işleyebilir. Verileriniz bunlar dışında üçüncü kişilerle paylaşılmaz.</p>
<h3>Haklarınız</h3>
<p>KVKK'nın 11. maddesi uyarınca kişisel verilerinizin işlenip işlenmediğini öğrenme, bilgi talep etme, düzeltilmesini veya silinmesini isteme ve itiraz etme haklarına sahipsiniz. Taleplerinizi <a href="mailto:{MAIL}">{MAIL}</a> adresine iletebilirsiniz.</p>
</div></section>
""")
    write("cerez-politikasi.html", "Çerez Politikası | Prof. Dr. Ahmet Avcı",
          f"{SITE.split('//')[1]} çerez politikası.",
          page_hero("Yasal", "Çerez Politikası") + f"""<section class="section"><div class="wrap prose narrow">
{legal_note}
<p>Bu site reklam, izleme veya analiz çerezi kullanmaz ve ziyaretçi davranışlarını takip etmez.</p>
<h3>Üçüncü taraf içerikler</h3>
<p>Yazı tipleri Google Fonts üzerinden yüklenir. Sayfalardaki video, siz oynat düğmesine basana kadar yüklenmez; bastığınızda YouTube'un çerez kullanımı azaltılmış (youtube-nocookie.com) oynatıcısı açılır. YouTube'un uygulamaları için <a href="https://policies.google.com/privacy?hl=tr" target="_blank" rel="noopener">Google Gizlilik Politikası</a> geçerlidir.</p>
<h3>Değişiklikler</h3>
<p>Siteye analiz aracı, bülten veya benzeri bir hizmet eklenirse bu politika güncellenir ve gerekiyorsa onayınız istenir.</p>
</div></section>
""")
    write("gizlilik.html", "Gizlilik | Prof. Dr. Ahmet Avcı",
          f"{SITE.split('//')[1]} gizlilik bildirimi.",
          page_hero("Yasal", "Gizlilik") + f"""<section class="section"><div class="wrap prose narrow">
{legal_note}
<p>Gizliliğinize önem veriyoruz. Bu site bilgi amaçlıdır; üyelik, ödeme veya veri saklayan bir form içermez.</p>
<ul>
<li>Ziyaretiniz sırasında barındırma hizmeti (Vercel) güvenlik ve işletim amacıyla standart sunucu kayıtları (IP adresi, tarayıcı bilgisi, ziyaret zamanı) tutabilir.</li>
<li>İletişim formu yalnızca kendi e-posta uygulamanızı açar; gönderdiğiniz e-postalar yalnızca talebinize yanıt vermek için kullanılır.</li>
<li>Çerezlerle ilgili ayrıntılar için <a href="cerez-politikasi.html">Çerez Politikası</a>, kişisel verilerle ilgili haklarınız için <a href="kvkk.html">KVKK Aydınlatma Metni</a> sayfasına bakabilirsiniz.</li>
</ul>
<p>Sorularınız için: <a href="mailto:{MAIL}">{MAIL}</a></p>
</div></section>
""")

    # sitemap
    pages = ["index.html"] + [h for h, _ in MENU] + ["akademik.html", "danismanlik.html", "basinda.html", "kaynaklar.html", "bulten.html", "en.html", "kvkk.html", "cerez-politikasi.html", "gizlilik.html"]
    urls = "\n".join(f"  <url><loc>{SITE}/{'' if p == 'index.html' else p}</loc></url>" for p in pages)
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")


if __name__ == "__main__":
    build()
    print("Sayfalar üretildi.")
