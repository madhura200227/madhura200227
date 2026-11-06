import urllib.request

endpoints = [
    "http://127.0.0.1:8080/api/status",
    "http://127.0.0.1:8080/assets/hero/hero-banner.svg",
    "http://127.0.0.1:8080/assets/hero/hero-banner-cherry.svg",
    "http://127.0.0.1:8080/assets/hero/hero-banner-preview.png",
    "http://127.0.0.1:8080/assets/hero/hero-comparison.png",
    "http://127.0.0.1:8080/assets/hero/hero-banner.gif"
]

for url in endpoints:
    try:
        req = urllib.request.urlopen(url, timeout=3)
        print(f"Status 200 OK: {url} ({req.length} bytes)")
    except Exception as e:
        print(f"Error for {url}: {e}")

