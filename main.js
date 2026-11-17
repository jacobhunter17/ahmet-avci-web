document.getElementById('y').textContent = new Date().getFullYear();

const btn = document.querySelector('.menu-btn');
const links = document.querySelector('.links');
btn.addEventListener('click', () => {
  const open = links.classList.toggle('open');
  btn.setAttribute('aria-expanded', open);
});
links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));

const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('show'); io.unobserve(e.target); } });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Form: ziyaretçinin e-posta uygulamasında hazır bir e-posta açar
document.getElementById('davet').addEventListener('submit', e => {
  e.preventDefault();
  const f = new FormData(e.target);
  const body = `Ad Soyad: ${f.get('ad')}\nKurum: ${f.get('kurum')}\nE-posta: ${f.get('eposta')}\n\n${f.get('mesaj')}`;
  location.href = 'mailto:ahmetavci7@gmail.com?subject=' + encodeURIComponent('Seminer / Konuşma Daveti') + '&body=' + encodeURIComponent(body);
});
