from selenium import webdriver
import time
import pyautogui

driver = webdriver.Chrome()
driver.get("https://chromedino.com/")

time.sleep(3)

driver.maximize_window()
time.sleep(1)

pyautogui.click(600, 400)
time.sleep(1)

pyautogui.press("space")

last_jump_time = time.time()

region = (700, 430, 180, 50)

while True:
    image = pyautogui.screenshot(region=region)

    obstacle = False

    for x in range(0, 180, 20):
        pixel = image.getpixel((x, 45))

        if pixel[0] < 100:
            obstacle = True
            break

    # ✅ NO sleep here
    if obstacle and (time.time() - last_jump_time > 0.12):
        pyautogui.press("space")
        last_jump_time = time.time()
