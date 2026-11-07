import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1400,1200')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=chrome_options)

try:
    print('Navigating to http://127.0.0.1:8080/preview.html...')
    driver.get('http://127.0.0.1:8080/preview.html')
    time.sleep(3)

    # 1. Take Cherry Royale Default Mode Screenshot
    driver.save_screenshot('preview_cherry_mode.png')
    print('Saved preview_cherry_mode.png')

    # 2. Click Mode Toggle Button to switch to Midnight Espresso
    toggle_btn = driver.find_element(By.ID, 'modeToggleBtn')
    toggle_btn.click()
    time.sleep(2)
    driver.save_screenshot('preview_espresso_mode.png')
    print('Saved preview_espresso_mode.png')

    # 3. Simulate GitHub Dark Mode rendering of the Hero Banner + Badge
    github_html = """
    <!DOCTYPE html>
    <html style="background-color: #0d1117; color: #c9d1d9; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
    <head><meta charset="utf-8"></head>
    <body style="background-color: #0d1117; margin: 0; padding: 40px 20px;">
      <div style="max-width: 1012px; margin: 0 auto; background: #0d1117; text-align: center;">
        <img src="assets/hero/hero-banner-cherry.gif" style="max-width: 100%; height: auto; border-radius: 8px;" />
        <div style="margin: 24px 0;">
          <a href="https://madhura200227.github.io/madhura200227/">
            <img src="assets/icons/live-portfolio-badge-cherry.svg" height="38" />
          </a>
        </div>
        <div style="margin-top: 18px;">
          <a href="#"><img src="assets/icons/connect-linkedin-cherry.svg" height="34" style="margin: 0 8px;" /></a>
          <a href="#"><img src="assets/icons/connect-email-cherry.svg" height="34" style="margin: 0 8px;" /></a>
          <a href="#"><img src="assets/icons/connect-github-cherry.svg" height="34" style="margin: 0 8px;" /></a>
        </div>
      </div>
    </body>
    </html>
    """
    with open('github_dark_simulation.html', 'w', encoding='utf-8') as f:
        f.write(github_html)

    driver.get('http://127.0.0.1:8080/github_dark_simulation.html')
    time.sleep(2)
    driver.save_screenshot('github_dark_simulation.png')
    print('Saved github_dark_simulation.png')

finally:
    driver.quit()

