document.addEventListener('DOMContentLoaded', () => {
  // 1) Year stamp
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // 2) Image fallback: if any image fails, mark it gracefully
  document.querySelectorAll('img').forEach((img) => {
    img.addEventListener('error', () => {
      // Only swap once to avoid loops
      if (!img.classList.contains('img-error')) {
        img.classList.add('img-error');
        // Transparent 1x1 PNG placeholder
        const placeholder = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAkMBQ6c+2EwAAAAASUVORK5CYII=';
        if (img.src !== placeholder) {
          img.src = placeholder;
          img.alt = img.alt || 'Image not available';
        }
      }
    }, { once: true });
  });

  // 3) Optional: check links (HTTP only). When opened as file:// this is skipped.
  const isHttp = location.protocol.startsWith('http');
  if (isHttp) {
    const sameOrigin = (url) => {
      try {
        const u = new URL(url, location.href);
        return u.origin === location.origin;
      } catch { return false; }
    };
    const shouldCheck = (href) => /\.(pdf|ipynb|py|png|jpg|jpeg|gif)$/i.test(href);

    document.querySelectorAll('a[href]').forEach((a) => {
      const href = a.getAttribute('href');
      if (!href || href.startsWith('#') || !shouldCheck(href)) return;
      const url = new URL(href, location.href);
      if (!sameOrigin(url)) return;

      fetch(url, { method: 'HEAD' }).then((res) => {
        if (!res.ok) a.classList.add('broken');
      }).catch(() => a.classList.add('broken'));
    });
  }
});
