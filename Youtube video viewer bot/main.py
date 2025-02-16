from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.chrome.options import Options

while True:
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  
    pyautogui.moveTo(1052,555)
    driver = webdriver.Chrome(chrome_options)
    driver.set_window_position(-2000, 0)
    driver.get("https://www.youtube.com/watch?v=rhktxR2qrZ0")
    
    driver.find_element(By.CSS_SELECTOR, ".ytp-play-button").click()

    time.sleep(15)
    driver.quit()

    pyautogui.moveTo(1035,467, duration=0.8)