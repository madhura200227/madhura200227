import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1400,1250')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=chrome_options)

try:
    print('Loading http://127.0.0.1:8080/preview.html...')
    driver.get('http://127.0.0.1:8080/preview.html')
    time.sleep(3)
    driver.save_screenshot('crystal_clear_cherry.png')
    print('Saved crystal_clear_cherry.png')

    # Crop hero banner text area to inspect crystal clarity
    im = Image.open('crystal_clear_cherry.png')
    hero_crop = im.crop((180, 160, 750, 620))
    hero_crop.save('crystal_clear_hero_crop.png')
    print('Saved crystal_clear_hero_crop.png')

    # Switch to espresso mode
    toggle_btn = driver.find_element(By.ID, 'modeToggleBtn')
    toggle_btn.click()
    time.sleep(2)
    driver.save_screenshot('crystal_clear_espresso.png')
    print('Saved crystal_clear_espresso.png')

finally:
    driver.quit()

