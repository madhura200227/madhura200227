with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

target_block = """    let currentMode = 'cherry';

    function showToast(msg) {
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2500);
    }

    function toggleBrandMode() {
      const body = document.body;
      const btnText = document.getElementById('modeBtnText');
      const cardBtnText = document.getElementById('cardModeBtnText');
      const floatingText = document.getElementById('floatingToggleText');
      const badge = document.getElementById('modeBadge');

      if (currentMode === 'espresso') {
        currentMode = 'cherry';
        body.classList.remove('mode-espresso');
        body.classList.add('mode-cherry');
        btnText.innerText = '✦ Switch to Midnight Éspresso';
        if (cardBtnText) cardBtnText.innerText = '✦ Switch to Midnight Éspresso';
        if (floatingText) floatingText.innerText = 'Switch to Midnight Éspresso';
        badge.innerText = 'CHERRY ROYALE';
        swapThemeAssets('cherry');
      } else {
        currentMode = 'espresso';
        body.classList.remove('mode-cherry');
        body.classList.add('mode-espresso');
        btnText.innerText = '✦ Switch to Cherry Royale';
        if (cardBtnText) cardBtnText.innerText = '✦ Switch to Cherry Royale';
        if (floatingText) floatingText.innerText = 'Switch to Cherry Royale';
        badge.innerText = 'MIDNIGHT ÉSPRESSO';
        swapThemeAssets('espresso');
      }

      // Notify backend of mode change
      fetch('/api/mode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode: currentMode })
      }).catch(() => {});
    }"""

replacement_block = """    const urlParams = new URLSearchParams(window.location.search);
    const initialTheme = urlParams.get('theme');
    let currentMode = (initialTheme === 'espresso') ? 'espresso' : 'cherry';

    function showToast(msg) {
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2500);
    }

    function setBrandMode(mode) {
      currentMode = mode;
      const body = document.body;
      const btnText = document.getElementById('modeBtnText');
      const cardBtnText = document.getElementById('cardModeBtnText');
      const floatingText = document.getElementById('floatingToggleText');
      const badge = document.getElementById('modeBadge');

      if (currentMode === 'espresso') {
        body.classList.remove('mode-cherry');
        body.classList.add('mode-espresso');
        if (btnText) btnText.innerText = '✦ Switch to Cherry Royale';
        if (cardBtnText) cardBtnText.innerText = '✦ Switch to Cherry Royale';
        if (floatingText) floatingText.innerText = 'Switch to Cherry Royale';
        if (badge) badge.innerText = 'MIDNIGHT ÉSPRESSO';
        swapThemeAssets('espresso');
      } else {
        body.classList.remove('mode-espresso');
        body.classList.add('mode-cherry');
        if (btnText) btnText.innerText = '✦ Switch to Midnight Éspresso';
        if (cardBtnText) cardBtnText.innerText = '✦ Switch to Midnight Éspresso';
        if (floatingText) floatingText.innerText = 'Switch to Midnight Éspresso';
        if (badge) badge.innerText = 'CHERRY ROYALE';
        swapThemeAssets('cherry');
      }
    }

    function toggleBrandMode() {
      setBrandMode(currentMode === 'espresso' ? 'cherry' : 'espresso');
      // Notify backend of mode change
      fetch('/api/mode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode: currentMode })
      }).catch(() => {});
    }"""

if target_block in text:
    text = text.replace(target_block, replacement_block)
    # Also ensure setBrandMode(currentMode) is called after markdown parse
    text = text.replace("swapThemeAssets(currentMode);", "setBrandMode(currentMode);")
    with open('preview.html', 'w', encoding='utf-8') as f:
        f.write(text)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated preview.html and index.html with setBrandMode and URL query param support')
else:
    print('target_block not found in preview.html')

