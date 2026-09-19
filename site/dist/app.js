(() => {
  const body = document.body;
  const fontButton = document.getElementById('fontToggle');
  const themeButton = document.getElementById('themeToggle');
  const menuButton = document.getElementById('menuToggle');
  const sidebar = document.getElementById('sidebar');

  if (localStorage.getItem('atd-font') === 'large') {
    body.classList.add('large-text');
    fontButton?.setAttribute('aria-pressed', 'true');
    if (fontButton) fontButton.textContent = '標準文字';
  }

  const savedTheme = localStorage.getItem('atd-theme');
  if (savedTheme === 'dark') body.classList.add('manual-dark');
  if (savedTheme === 'light') body.classList.add('manual-light');

  fontButton?.addEventListener('click', () => {
    const large = body.classList.toggle('large-text');
    fontButton.setAttribute('aria-pressed', String(large));
    fontButton.textContent = large ? '標準文字' : '放大文字';
    localStorage.setItem('atd-font', large ? 'large' : 'standard');
  });

  themeButton?.addEventListener('click', () => {
    const darkNow = body.classList.contains('manual-dark') ||
      (!body.classList.contains('manual-light') && matchMedia('(prefers-color-scheme: dark)').matches);
    body.classList.toggle('manual-dark', !darkNow);
    body.classList.toggle('manual-light', darkNow);
    themeButton.setAttribute('aria-pressed', String(!darkNow));
    localStorage.setItem('atd-theme', darkNow ? 'light' : 'dark');
  });

  menuButton?.addEventListener('click', () => {
    const open = sidebar?.classList.toggle('open') ?? false;
    menuButton.setAttribute('aria-expanded', String(open));
  });

  sidebar?.addEventListener('click', event => {
    if (event.target.closest('a') && innerWidth <= 820) {
      sidebar.classList.remove('open');
      menuButton?.setAttribute('aria-expanded', 'false');
    }
  });

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && sidebar?.classList.contains('open')) {
      sidebar.classList.remove('open');
      menuButton?.setAttribute('aria-expanded', 'false');
      menuButton?.focus();
    }
  });
})();
