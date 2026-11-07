with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = "'signature',\n        'snake'"
replacement = "'signature',\n        'snake',\n        'live-portfolio-badge'"

if target in text:
    text = text.replace(target, replacement)
    with open('preview.html', 'w', encoding='utf-8') as f:
        f.write(text)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Added live-portfolio-badge to swapThemeAssets')
else:
    print('Target not found')

