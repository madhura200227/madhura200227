with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = "document.getElementById('backendStatusText').innerText = `BACKEND API: LOCAL FILE SERVER`;"
replacement = "document.getElementById('backendStatusText').innerText = (window.location.hostname && window.location.hostname.includes('github.io')) ? 'ENGINE: LIVE (GITHUB PAGES)' : 'BACKEND: LOCAL ENGINE';"

if target in text:
    text = text.replace(target, replacement)
    with open('preview.html', 'w', encoding='utf-8') as f:
        f.write(text)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated preview.html & index.html successfully')
else:
    print('Target not found in preview.html')

