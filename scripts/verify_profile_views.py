import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1400,1600')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=chrome_options)

try:
    print("Navigating to http://127.0.0.1:8080/preview.html...")
    driver.get("http://127.0.0.1:8080/preview.html")
    time.sleep(3)

    # 1. Take Cherry screenshot
    driver.save_screenshot("verify_cherry_views.png")
    print("Saved verify_cherry_views.png")

    # 2. Toggle to Espresso mode
    toggle_btn = driver.find_element(By.ID, "modeToggleBtn")
    toggle_btn.click()
    time.sleep(2)
    driver.save_screenshot("verify_espresso_views.png")
    print("Saved verify_espresso_views.png")

    # 3. Crop key sections for visual proof
    im = Image.open("verify_cherry_views.png")

    # Launch badge + views badge crop (around y=350 to 550, x=350 to 1050)
    # Let's locate the element or crop dynamically
    try:
        # Find img with komarev in src
        komarev_img = driver.find_element(By.XPATH, "//img[contains(@src, 'komarev')]")
        loc = komarev_img.location
        size = komarev_img.size
        print(f"Komarev img location: {loc}, size: {size}")
        
        # Crop with surrounding context
        crop_box = (
            max(0, int(loc['x'] - 200)),
            max(0, int(loc['y'] - 120)),
            min(im.width, int(loc['x'] + size['width'] + 200)),
            min(im.height, int(loc['y'] + size['height'] + 120))
        )
        cropped = im.crop(crop_box)
        cropped.save("crop_views_badge.png")
        print("Saved crop_views_badge.png")
    except Exception as e:
        print(f"Error cropping badge: {e}")

    # Find stats SVG
    try:
        stats_img = driver.find_element(By.XPATH, "//img[contains(@src, 'github-stats')]")
        s_loc = stats_img.location
        s_size = stats_img.size
        print(f"Stats img location: {s_loc}, size: {s_size}")
        crop_stats = (
            max(0, int(s_loc['x'] - 20)),
            max(0, int(s_loc['y'] - 20)),
            min(im.width, int(s_loc['x'] + s_size['width'] + 20)),
            min(im.height, int(s_loc['y'] + s_size['height'] + 20))
        )
        stats_cropped = im.crop(crop_stats)
        stats_cropped.save("crop_overview_4cards.png")
        print("Saved crop_overview_4cards.png")
    except Exception as e:
        print(f"Error cropping stats: {e}")

    # Crop dock at bottom
    try:
        dock = driver.find_element(By.CLASS_NAME, "status-dock")
        d_loc = dock.location
        d_size = dock.size
        dock_box = (
            max(0, int(d_loc['x'] - 10)),
            max(0, int(d_loc['y'] - 10)),
            min(im.width, int(d_loc['x'] + d_size['width'] + 10)),
            min(im.height, int(d_loc['y'] + d_size['height'] + 10))
        )
        # re-open to get unscaled
        dock_cropped = Image.open("verify_cherry_views.png").crop(dock_box)
        dock_cropped.save("crop_status_dock.png")
        print("Saved crop_status_dock.png")
    except Exception as e:
        print(f"Error cropping dock: {e}")

finally:
    driver.quit()
    print("Verification script finished.")

