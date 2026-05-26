<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Landing Demo</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <style>body{font-family:Arial;max-width:800px;margin:2rem auto;padding:0 1rem}header{border-bottom:1px solid #eee;padding-bottom:1rem;margin-bottom:1rem}</style>
</head>
<body>
  <header><h1 id="hero-title">Loading...</h1></header>
  <main id="content"></main>

  <section>
    <h2>Contact</h2>
    <form id="contact-form">
      <input name="name" placeholder="Name" required /><br/>
      <input name="email" placeholder="Email" required /><br/>
      <textarea name="message" placeholder="Message" required></textarea><br/>
      <button type="submit">Send</button>
    </form>
  </section>

  <script>
    const API = (path) => `/api${path}`;
    async function load() {
      const res = await fetch(API('/content/'));
      const sections = await res.json();
      const hero = sections.find(s => s.key === 'hero');
      document.getElementById('hero-title').innerText = hero?.title || 'Welcome';
      const main = document.getElementById('content');
      sections.forEach(s => {
        const sec = document.createElement('section');
        sec.innerHTML = `<h3>${s.title}</h3><div>${s.content || ''}</div>`;
        main.appendChild(sec);
      });
    }
    document.getElementById('contact-form').addEventListener('submit', async e => {
      e.preventDefault();
      const fd = new FormData(e.target);
      const payload = Object.fromEntries(fd.entries());
      await fetch(API('/contact/'), { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload) });
      alert('Message queued');
      e.target.reset();
    });
    load();
  </script>
</body>
</html>
