(function () {
  var root = document.documentElement;
  root.classList.add('js');

  // header border once scrolled (IntersectionObserver on a sentinel, no scroll listener)
  var head = document.querySelector('.site-head');
  var sentinel = document.createElement('div');
  sentinel.style.cssText = 'position:absolute;top:0;height:8px;width:1px';
  document.body.prepend(sentinel);
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (e) {
      head.classList.toggle('is-scrolled', !e[0].isIntersecting);
    }).observe(sentinel);
  }

  // mobile menu
  var burger = document.querySelector('.burger');
  var menu = document.getElementById('menu');
  function setMenu(open) {
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    document.body.classList.toggle('menu-open', open);
    if (open) {
      menu.hidden = false;
      requestAnimationFrame(function () { menu.classList.add('is-open'); });
      var first = menu.querySelector('a');
      if (first) first.focus();
    } else {
      menu.classList.remove('is-open');
      setTimeout(function () { if (!menu.classList.contains('is-open')) menu.hidden = true; }, 300);
      burger.focus();
    }
  }
  burger.addEventListener('click', function () { setMenu(burger.getAttribute('aria-expanded') !== 'true'); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') setMenu(false);
  });
  menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });

  // reveals
  var hero = document.querySelector('.hero');
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
  }
  if (hero) requestAnimationFrame(function () { requestAnimationFrame(function () { hero.classList.add('is-in'); }); });

  // floating card: show after the first viewport, hide over the footer
  var card = document.querySelector('.float-card');
  var foot = document.querySelector('.site-foot');
  if (card && 'IntersectionObserver' in window) {
    var past = false, atFoot = false, forms = 0;
    var top = document.querySelector('.hero, .phero');
    function upd() { card.classList.toggle('is-on', past && !atFoot && !forms); }
    var fio = new IntersectionObserver(function (es) {
      es.forEach(function (e) { forms += e.isIntersecting ? 1 : (e.target._seen ? -1 : 0); e.target._seen = e.isIntersecting; });
      forms = Math.max(0, forms); upd();
    });
    document.querySelectorAll('.request, .cta-band').forEach(function (el) { fio.observe(el); });
    if (top) new IntersectionObserver(function (e) { past = !e[0].isIntersecting; upd(); }).observe(top);
    new IntersectionObserver(function (e) { atFoot = e[0].isIntersecting; upd(); }).observe(foot);
  }

  // form validation
  document.querySelectorAll('form.form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      var firstBad = null;
      form.querySelectorAll('.field').forEach(function (f) {
        var input = f.querySelector('input,select,textarea');
        var err = f.querySelector('.err');
        var msg = '';
        if (input.required && !input.value.trim()) msg = 'Please fill this in.';
        else if (input.type === 'email' && input.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value)) msg = 'Please enter a valid email address.';
        else if (input.type === 'tel' && input.value && input.value.replace(/\D/g, '').length < 10) msg = 'Please enter a full phone number.';
        f.classList.toggle('has-err', !!msg);
        err.textContent = msg;
        input.setAttribute('aria-invalid', msg ? 'true' : 'false');
        if (msg) {
          input.setAttribute('aria-describedby', err.id || (err.id = input.id + '-err'));
          if (!firstBad) firstBad = input;
        }
      });
      if (firstBad) { e.preventDefault(); firstBad.focus(); }
    });
  });
})();
