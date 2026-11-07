with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

target_swap = """        for (const name of assetNames) {"""

replacement_swap = """        if (cleanSrc.includes('theme-cherry') || cleanSrc.includes('theme-espresso')) {
          if (theme === 'cherry') {
            if (cleanSrc.includes('theme-cherry')) cleanSrc = 'assets/icons/theme-cherry-active.svg';
            if (cleanSrc.includes('theme-espresso')) cleanSrc = 'assets/icons/theme-espresso-inactive.svg';
          } else {
            if (cleanSrc.includes('theme-cherry')) cleanSrc = 'assets/icons/theme-cherry-inactive.svg';
            if (cleanSrc.includes('theme-espresso')) cleanSrc = 'assets/icons/theme-espresso-active.svg';
          }
        }

        for (const name of assetNames) {"""

target_marked = """        document.getElementById('content').innerHTML = marked.parse(markdown);
        // Force asset calibration immediately upon render
        setBrandMode(currentMode);"""

replacement_marked = """        document.getElementById('content').innerHTML = marked.parse(markdown);
        // Force asset calibration immediately upon render
        setBrandMode(currentMode);

        // Bind in-page clicks on README links to instant client mode toggles
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

if target_swap in text and target_marked in text:
    text = text.replace(target_swap, replacement_swap).replace(target_marked, replacement_marked)
    with open('preview.html', 'w', encoding='utf-8') as f:
        f.write(text)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated preview.html & index.html with interactive pill handlers')
else:
    print('Targets not found')

