import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1400,1250')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=chrome_options)

try:
    print('Capturing updated preview...')
    driver.get('http://127.0.0.1:8080/preview.html')
    time.sleep(3)
    driver.save_screenshot('preview_goals_cherry.png')
    print('Saved preview_goals_cherry.png')

    # Switch to espresso
    toggle_btn = driver.find_element(By.ID, 'modeToggleBtn')
    toggle_btn.click()
    time.sleep(2)
    driver.save_screenshot('preview_goals_espresso.png')
    print('Saved preview_goals_espresso.png')

finally:
    driver.quit()

