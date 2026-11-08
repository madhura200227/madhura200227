import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1400,1200')
driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get('http://127.0.0.1:8080/preview.html')
    time.sleep(2)
    elem = driver.find_element(By.XPATH, "//*[contains(text(), 'Contribution Activity')]")
    driver.execute_script('arguments[0].scrollIntoView(true);', elem)
    time.sleep(1)
    driver.save_screenshot('snake_verified.png')
    im = Image.open('snake_verified.png')
    crop = im.crop((180, 50, 1220, 500))
    crop.save('snake_verified_crop.png')
    print('Captured snake_verified_crop.png')
finally:
    driver.quit()

