import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1400,6000')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("http://127.0.0.1:8080/preview.html")
    time.sleep(3)
    driver.save_screenshot("full_page_tall.png")

    stats_img = driver.find_element(By.XPATH, "//img[contains(@src, 'github-stats')]")
    loc = stats_img.location
    size = stats_img.size
    print(f"Stats loc: {loc}, size: {size}")

    im = Image.open("full_page_tall.png")
    crop_stats = (
        max(0, int(loc['x'] - 20)),
        max(0, int(loc['y'] - 20)),
        min(im.width, int(loc['x'] + size['width'] + 20)),
        min(im.height, int(loc['y'] + size['height'] + 20))
    )
    cropped = im.crop(crop_stats)
    cropped.save("crop_overview_4cards.png")
    print("Successfully saved crop_overview_4cards.png!")
finally:
    driver.quit()

