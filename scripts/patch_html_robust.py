with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove green dot from .live-dot
text = text.replace('background: #4ade80;\n      box-shadow: 0 0 8px #4ade80;', 'background: var(--accent-cherry);\n      box-shadow: 0 0 8px var(--accent-cherry);')

# 2. Update picture replacement in swapThemeAssets
old_picture_block = """      // 1. Process all <source> elements inside <picture> tags
      document.querySelectorAll('#content picture source').forEach(source => {
        let srcset = source.getAttribute('srcset') || '';
        let clean = srcset.split('?')[0];

        if (clean.includes('hero-banner')) {
          if (theme === 'cherry') {
            source.setAttribute('srcset', 'assets/hero/hero-banner-cherry.gif?v=' + v);
          } else {
            source.setAttribute('srcset', 'assets/hero/hero-banner.gif?v=' + v);
          }
        }

        if (clean.includes('snake')) {
          if (theme === 'cherry') {
            source.setAttribute('srcset', 'assets/stats/snake-cherry.svg?v=' + v);
          } else {
            source.setAttribute('srcset', 'assets/stats/snake.svg?v=' + v);
          }
        }
      });"""

new_picture_block = """      // 1. Process all <picture> elements and inner <source> & <img>
      document.querySelectorAll('#content picture').forEach(pic => {
        const sources = pic.querySelectorAll('source');
        const img = pic.querySelector('img');
        const isHero = (img && img.src.includes('hero-banner')) || Array.from(sources).some(s => s.srcset.includes('hero-banner'));
        if (isHero) {
          const newSrc = theme === 'cherry' ? 'assets/hero/hero-banner-cherry.gif?v=' + v : 'assets/hero/hero-banner.gif?v=' + v;
          sources.forEach(s => s.setAttribute('srcset', newSrc));
          if (img) img.setAttribute('src', newSrc);
        }
        const isSnake = (img && img.src.includes('snake')) || Array.from(sources).some(s => s.srcset.includes('snake'));
        if (isSnake) {
          const newSrc = theme === 'cherry' ? 'assets/stats/snake-cherry.svg?v=' + v : 'assets/stats/snake.svg?v=' + v;
          sources.forEach(s => s.setAttribute('srcset', newSrc));
          if (img) img.setAttribute('src', newSrc);
        }
      });"""

text = text.replace(old_picture_block, new_picture_block)

# 3. Update link click bindings
old_link_bind = """        // Bind in-page clicks on README links to instant client mode toggles
        document.querySelectorAll('#content a[href*="README"]').forEach(a => {
          a.addEventListener('click', (e) => {
            e.preventDefault();
            const href = a.getAttribute('href') || '';
            if (href.includes('README-espresso')) {
              setBrandMode('espresso');
            } else {
              setBrandMode('cherry');
            }
          });
        });"""

new_link_bind = """        // Bind in-page clicks on ANY theme toggle link to instant client mode toggles
        document.querySelectorAll('#content a').forEach(a => {
          const href = a.getAttribute('href') || '';
          if (href.includes('espresso')) {
            a.addEventListener('click', (e) => {
              e.preventDefault();
              setBrandMode('espresso');
            });
          } else if (href.includes('cherry')) {
            a.addEventListener('click', (e) => {
              e.preventDefault();
              setBrandMode('cherry');
            });
          }
        });"""

text = text.replace(old_link_bind, new_link_bind)

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated preview.html & index.html with green dot removal, picture refresh, and comprehensive link binding')

