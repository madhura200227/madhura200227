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

    # 1. Full page screenshot (Cherry)
    driver.save_screenshot("full_cherry_footer.png")
    im_c = Image.open("full_cherry_footer.png")

    # Crop Top Hero Launch section to verify NO views badge is there
    launch_badge = driver.find_element(By.XPATH, "//img[contains(@src, 'live-portfolio-badge')]")
    loc_lb = launch_badge.location
    size_lb = launch_badge.size
    crop_top = (
        max(0, int(loc_lb['x'] - 200)),
        max(0, int(loc_lb['y'] - 40)),
        min(im_c.width, int(loc_lb['x'] + size_lb['width'] + 200)),
        min(im_c.height, int(loc_lb['y'] + size_lb['height'] + 140))
    )
    cropped_top = im_c.crop(crop_top)
    cropped_top.save("C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/verified_clean_top_section.png")
    print("Saved verified_clean_top_section.png")

    # Crop Bottom Footer section to verify custom views badge
    pv_img = driver.find_element(By.XPATH, "//img[contains(@src, 'profile-views')]")
    loc_pv = pv_img.location
    size_pv = pv_img.size
    print(f"Profile views badge loc: {loc_pv}, size: {size_pv}")

    crop_bottom = (
        max(0, int(loc_pv['x'] - 200)),
        max(0, int(loc_pv['y'] - 120)),
        min(im_c.width, int(loc_pv['x'] + size_pv['width'] + 200)),
        min(im_c.height, int(loc_pv['y'] + size_pv['height'] + 60))
    )
    cropped_bottom_cherry = im_c.crop(crop_bottom)
    cropped_bottom_cherry.save("C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/verified_bottom_views_cherry.png")
    print("Saved verified_bottom_views_cherry.png")

    # 2. Toggle to Midnight Espresso
    toggle_btn = driver.find_element(By.ID, "modeToggleBtn")
    toggle_btn.click()
    time.sleep(2)
    driver.save_screenshot("full_espresso_footer.png")
    im_e = Image.open("full_espresso_footer.png")

    cropped_bottom_espresso = im_e.crop(crop_bottom)
    cropped_bottom_espresso.save("C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/verified_bottom_views_espresso.png")
    print("Saved verified_bottom_views_espresso.png")

finally:
    driver.quit()
    print("All footer views verifications completed!")
