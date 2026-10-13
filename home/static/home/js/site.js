// FastConnect: header, mobile menu, scroll reveals and counters.
(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // =============================
  // Header: solid background once the page is scrolled
  // =============================
  const header = document.querySelector('[data-header]');
  if (header) {
    const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 24);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // =============================
  // Mobile menu
  // =============================
  const menuBtn = document.getElementById('menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if (menuBtn && mobileMenu) {
    const setOpen = (open) => {
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
      mobileMenu.classList.toggle('is-open', open);
      // keep the header solid while the menu is open so the links are readable
      header?.classList.toggle('is-scrolled', open || window.scrollY > 24);
    };
    menuBtn.addEventListener('click', () => setOpen(menuBtn.getAttribute('aria-expanded') !== 'true'));
    mobileMenu.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => setOpen(false)));
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileMenu.classList.contains('is-open')) {
        setOpen(false);
        menuBtn.focus();
      }
    });
    window.matchMedia('(min-width: 768px)').addEventListener('change', (e) => e.matches && setOpen(false));
  }

  // =============================
  // Scroll reveal ([data-reveal], optional data-delay in ms)
  // =============================
  const revealEls = document.querySelectorAll('[data-reveal], .speed-bar');
  revealEls.forEach((el) => {
    if (el.dataset.delay) el.style.setProperty('--delay', el.dataset.delay);
  });
  if (reduceMotion || !('IntersectionObserver' in window)) {
    revealEls.forEach((el) => el.classList.add('is-visible'));
  } else {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach((el) => revealObserver.observe(el));
  }

  // =============================
  // Animated counters ([data-count-to])
  // =============================
  const counters = document.querySelectorAll('[data-count-to]');
  const runCounter = (el) => {
    const target = parseInt(el.dataset.countTo, 10);
    if (reduceMotion) { el.textContent = target; return; }
    const duration = 1600;
    const start = performance.now();
    const tick = (now) => {
      const p = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - p, 4);
      el.textContent = Math.round(target * eased);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if ('IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        runCounter(entry.target);
        counterObserver.unobserve(entry.target);
      });
    }, { threshold: 0.6 });
    counters.forEach((el) => counterObserver.observe(el));
  } else {
    counters.forEach((el) => { el.textContent = el.dataset.countTo; });
  }

  // =============================
  // Cards that follow the cursor with a soft spotlight ([data-spotlight])
  // =============================
  if (!reduceMotion && window.matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('[data-spotlight]').forEach((card) => {
      card.addEventListener('pointermove', (e) => {
        const r = card.getBoundingClientRect();
        card.style.setProperty('--mx', `${e.clientX - r.left}px`);
        card.style.setProperty('--my', `${e.clientY - r.top}px`);
      });
    });
  }

  // =============================
  // Contact form: preselect the plan from ?plan=<code> (links from the plan cards)
  // =============================
  const planSelect = document.querySelector('select[name="plan"]');
  const planParam = new URLSearchParams(window.location.search).get('plan');
  if (planSelect && planParam && planSelect.querySelector(`option[value="${CSS.escape(planParam)}"]`)) {
    planSelect.value = planParam;
  }

  // =============================
  // Contact form: show a sending state on submit
  // =============================
  document.querySelectorAll('form[data-loading-form]').forEach((form) => {
    const btn = form.querySelector('[type="submit"]');
    const label = btn?.querySelector('[data-label]');
    const spinner = btn?.querySelector('[data-spinner]');
    const originalLabel = label?.textContent;
    form.addEventListener('submit', () => {
      if (!btn) return;
      btn.disabled = true;
      if (label) label.textContent = 'Enviando…';
      spinner?.classList.remove('hidden');
    });
    // coming back with the browser's back button restores the page as it was; re-enable the button
    window.addEventListener('pageshow', (e) => {
      if (!e.persisted || !btn) return;
      btn.disabled = false;
      if (label) label.textContent = originalLabel;
      spinner?.classList.add('hidden');
    });
  });

  // =============================
  // Toast messages: auto-dismiss
  // =============================
  document.querySelectorAll('[data-toast]').forEach((toast) => {
    const close = () => {
      toast.style.transition = 'opacity .4s, transform .4s';
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(-10px)';
      setTimeout(() => toast.remove(), 400);
    };
    toast.querySelector('[data-toast-close]')?.addEventListener('click', close);
    setTimeout(close, 7000);
  });
})();
