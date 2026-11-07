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
    print('Testing preview.html...')
    driver.get('http://127.0.0.1:8080/preview.html')
    time.sleep(3)
    driver.save_screenshot('preview_with_theme_bar.png')
    print('Saved preview_with_theme_bar.png')

    # Simulate GitHub view of README.md with the theme selector bar
    with open('README.md', 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Capture the top portion of the actual preview
    print('Done capturing')

finally:
    driver.quit()

