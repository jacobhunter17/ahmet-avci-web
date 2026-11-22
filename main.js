document.getElementById('y').textContent = new Date().getFullYear();

// Mobil menü
const btn = document.querySelector('.menu-btn');
const links = document.querySelector('.links');
btn.addEventListener('click', () => {
  const open = links.classList.toggle('open');
  btn.setAttribute('aria-expanded', open);
});
links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));

// Kaydırınca beliren bölümler
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('show'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
} else {
  document.querySelectorAll('.reveal').forEach(el => el.classList.add('show'));
}

// Video: tıklanana kadar YouTube yüklenmez (site hızlı kalır, çerez yok)
document.querySelectorAll('[data-yt]').forEach(a => a.addEventListener('click', e => {
  e.preventDefault();
  const f = document.createElement('iframe');
  f.src = 'https://www.youtube-nocookie.com/embed/' + a.dataset.yt + '?autoplay=1';
  f.title = 'YouTube video';
  f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
  f.allowFullscreen = true;
  a.replaceWith(f);
}));

// İletişim formu: talep türüne göre hazır e-posta açar
const form = document.getElementById('davet');
if (form) {
  const konular = {
    konferans: 'Konferans / Seminer Talebi',
    danismanlik: 'Kurumsal Eğitim / Danışmanlık Talebi',
    basin: 'Basın / Röportaj Talebi',
    genel: 'Web Sitesinden Mesaj'
  };
  const tur = new URLSearchParams(location.search).get('tur');
  if (tur && konular[tur]) form.tur.value = tur;
  form.addEventListener('submit', e => {
    e.preventDefault();
    const f = new FormData(form);
    const body = `Ad Soyad: ${f.get('ad')}\nKurum: ${f.get('kurum')}\nE-posta: ${f.get('eposta')}\n\n${f.get('mesaj')}`;
    location.href = 'mailto:ahmetavci7@gmail.com?subject=' + encodeURIComponent(konular[f.get('tur')] || konular.genel) + '&body=' + encodeURIComponent(body);
  });
}
