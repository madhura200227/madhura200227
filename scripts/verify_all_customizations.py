import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--window-size=1400,6000')
opts.add_argument('--disable-gpu')
opts.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=opts)

try:
    print("Loading preview.html...")
    driver.get("http://127.0.0.1:8080/preview.html")
    time.sleep(3)

    # 1. Capture Cherry full tall screenshot
    driver.save_screenshot("full_cherry_tall.png")
    print("Saved full_cherry_tall.png")

    # 2. Crop Developer Cards section in Cherry
    h3_elem = driver.find_element(By.XPATH, "//h3[contains(text(), 'Developer Cards')]")
    loc_h3 = h3_elem.location
    streak_img = driver.find_element(By.XPATH, "//img[contains(@src, 'streak')]")
    loc_streak = streak_img.location
    size_streak = streak_img.size

    im_cherry = Image.open("full_cherry_tall.png")
    crop_cards = (
        max(0, int(loc_h3['x'] - 50)),
        max(0, int(loc_h3['y'] - 40)),
        min(im_cherry.width, int(loc_streak['x'] + size_streak['width'] + 50)),
        min(im_cherry.height, int(loc_streak['y'] + size_streak['height'] + 40))
    )
    cropped_cards_cherry = im_cherry.crop(crop_cards)
    cropped_cards_cherry.save("C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/verified_developer_cards_cherry.png")
    print("Saved verified_developer_cards_cherry.png")

    # 3. Crop Contribution Activity & Snake Stream section in Cherry
    snake_img = driver.find_element(By.XPATH, "//img[contains(@src, 'snake')]")
    loc_snake = snake_img.location
    size_snake = snake_img.size

    crop_snake = (
        max(0, int(loc_snake['x'] - 20)),
        max(0, int(loc_snake['y'] - 20)),
        min(im_cherry.width, int(loc_snake['x'] + size_snake['width'] + 20)),
        min(im_cherry.height, int(loc_snake['y'] + size_snake['height'] + 20))
    )
    cropped_snake_cherry = im_cherry.crop(crop_snake)
    cropped_snake_cherry.save("C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/verified_snake_stream_cherry.png")
    print("Saved verified_snake_stream_cherry.png")

    # 4. Toggle to Midnight Espresso Mode
    toggle_btn = driver.find_element(By.ID, "modeToggleBtn")
    toggle_btn.click()
    time.sleep(2)
    driver.save_screenshot("full_espresso_tall.png")

    im_espresso = Image.open("full_espresso_tall.png")
    cropped_cards_espresso = im_espresso.crop(crop_cards)
    cropped_cards_espresso.save("C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/verified_developer_cards_espresso.png")
    print("Saved verified_developer_cards_espresso.png")

    cropped_snake_espresso = im_espresso.crop(crop_snake)
    cropped_snake_espresso.save("C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/verified_snake_stream_espresso.png")
    print("Saved verified_snake_stream_espresso.png")

finally:
    driver.quit()
    print("All visual verifications finished successfully!")

