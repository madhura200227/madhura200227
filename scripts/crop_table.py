from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--window-size=1400,6000')
driver = webdriver.Chrome(options=opts)

try:
    driver.get('http://127.0.0.1:8080/preview.html')
    # Find table that has 'Views'
    tables = driver.find_elements(By.TAG_NAME, 'table')
    for t in tables:
        if 'Views' in t.text or 'CGPA' in t.text:
            loc = t.location
            size = t.size
            print(f"Found table at {loc}, size {size}")
            im = Image.open('full_page_tall.png')
            crop_box = (
                max(0, int(loc['x'] - 20)),
                max(0, int(loc['y'] - 20)),
                min(im.width, int(loc['x'] + size['width'] + 20)),
                min(im.height, int(loc['y'] + size['height'] + 20))
            )
            c = im.crop(crop_box)
            c.save('C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/crop_numbers_table.png')
            print("Successfully saved crop_numbers_table.png!")
            break
finally:
    driver.quit()

