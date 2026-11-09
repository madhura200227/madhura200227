from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--window-size=600,300')
driver = webdriver.Chrome(options=opts)

html = """
<!DOCTYPE html>
<html style="background-color: #1e040c; padding: 40px; text-align: center;">
<head><meta charset="utf-8"></head>
<body>
  <div style="margin-bottom: 24px;">
    <p style="color: #D99AA7; font-family: monospace; font-size: 12px; margin-bottom: 8px;">CHERRY ROYALE MODE</p>
    <img src="assets/stats/profile-views-cherry.svg" height="36" />
  </div>

  <div style="background-color: #140d0e; padding: 20px; border-radius: 8px;">
    <p style="color: #D99AA7; font-family: monospace; font-size: 12px; margin-bottom: 8px;">MIDNIGHT ESPRESSO MODE</p>
    <img src="assets/stats/profile-views.svg" height="36" />
  </div>
</body>
</html>
"""

with open("test_badge.html", "w", encoding="utf-8") as f:
    f.write(html)

driver.get("http://127.0.0.1:8080/test_badge.html")
driver.save_screenshot("C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/test_custom_views_badge.png")
driver.quit()
print("Saved test_custom_views_badge.png!")

