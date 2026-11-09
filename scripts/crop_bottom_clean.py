import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--window-size=1400,900')
driver = webdriver.Chrome(options=opts)

try:
    driver.get('http://127.0.0.1:8080/preview.html')
    time.sleep(2)
    # Scroll to bottom
    driver.execute_script('document.querySelector(".status-dock").style.display = "none"; window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)

    driver.save_screenshot('bottom_cherry.png')

    pv = driver.find_element(By.XPATH, "//img[contains(@src, 'profile-views')]")
    # Take screenshot of just this element directly using selenium!
    pv.screenshot('C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/element_views_cherry.png')

    # Also capture footer context
    footer = driver.find_element(By.XPATH, "//img[contains(@src, 'signature')]/..")
    footer.screenshot('C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/verified_bottom_views_cherry.png')

    # Toggle mode to Espresso
    toggle_btn = driver.find_element(By.ID, 'modeToggleBtn')
    toggle_btn.click()
    time.sleep(1)
    driver.execute_script('document.querySelector(".status-dock").style.display = "none"; window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)

    footer.screenshot('C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/verified_bottom_views_espresso.png')
    print("Successfully captured clean footer screenshots!")

finally:
    driver.quit()
