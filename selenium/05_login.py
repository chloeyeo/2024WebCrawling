from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import pyperclip
import pyautogui

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # remove any non-necessary logs
options.add_experimental_option("detach", True) # stop the webdriver from turning off
options.add_argument("--start-maximized") # start webdriver with max browser screen size


service = Service()
driver = webdriver.Chrome(service=service, options=options) # start a webdriver and make its options set to chrome
driver.get("https://nid.naver.com/nidlogin.login")\
    
id = driver.find_element(By.ID, "id")
id.click()
pyperclip.copy("<your_actual_id>") # e.g. chloechunsatoto
pyautogui.hotkey("ctrl", "v")

pw = driver.find_element(By.ID, "pw")
pw.click()
pyperclip.copy("<your_actual_password>")
pyautogui.hotkey("ctrl", "v")

# login = driver.find_element(By.CSS_SELECTOR,".btn_login") # same as below class_name (where we just not add the .)
login = driver.find_element(By.CLASS_NAME, "btn_login")
login.click()

# id = driver.find_element(By.ID, "id")
# id.click()
# id.send_keys("<your_actual_id>", Keys.TAB)
# pw = driver.find_element(By.ID, "pw")
# pw.click()
# pw.send_keys("<your_actual_password>", Keys.ENTER)
