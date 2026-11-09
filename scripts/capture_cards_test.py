from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--window-size=1000,900')
driver = webdriver.Chrome(options=opts)

html = """
<!DOCTYPE html>
<html style="background-color: #1e040c; padding: 40px; font-family: sans-serif;">
<head><meta charset="utf-8"></head>
<body>
  <div style="max-width: 860px; margin: 0 auto; text-align: center;">
    <div style="font-family: -apple-system, sans-serif; font-size: 22px; font-weight: 700; color: #FFF5ED; margin-bottom: 24px; display: flex; align-items: center; justify-content: center; gap: 8px;">
      <span>📊</span> Developer Cards
    </div>
    
    <div style="display: flex; justify-content: center; gap: 16px; margin-bottom: 18px;">
      <img src="assets/stats/github-stats-cherry.svg" width="495" height="195" />
      <img src="assets/stats/languages-cherry.svg" width="340" height="195" />
    </div>

    <div style="display: flex; justify-content: center;">
      <img src="assets/stats/streak-cherry.svg" width="495" height="195" />
    </div>
  </div>
</body>
</html>
"""

with open("test_cards.html", "w", encoding="utf-8") as f:
    f.write(html)

driver.get("http://127.0.0.1:8080/test_cards.html")
driver.save_screenshot("test_developer_cards.png")
driver.quit()
print("Saved test_developer_cards.png!")

