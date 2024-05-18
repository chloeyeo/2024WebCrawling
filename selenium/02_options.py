from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # remove any non-necessary logs
options.add_experimental_option("detach", True) # stop the webdriver from turning off
options.add_argument("--start-maximized") # start webdriver with max browser screen size
# options.add_argument("headless") # so we don't see the webdriver in browser and it just runs in background

service = Service()
driver = webdriver.Chrome(service=service, options=options) # start a webdriver and make its options set to chrome

driver.get("https://www.naver.com")