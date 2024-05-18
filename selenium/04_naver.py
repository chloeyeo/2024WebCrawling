from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # remove any non-necessary logs
options.add_experimental_option("detach", True) # stop the webdriver from turning off
options.add_argument("--start-maximized") # start webdriver with max browser screen size
# options.add_argument("headless") # so we don't see the webdriver in browser and it just runs in background

service = Service()
driver = webdriver.Chrome(service=service, options=options) # start a webdriver and make its options set to chrome
driver.get("https://search.shopping.naver.com/search/all?query=노트북")
action = driver.find_element(By.CSS_SELECTOR, "body")

for i in range(11):
    # delete 키 오른쪽 바로 옆에 있는 end키를 11번 눌러서 페이지 끝까지 내린다.
    action.send_keys(Keys.END) #모든 데이타가 다 불러져 온 상태에서 크롤링을 하려고 끝까지 페이지를 내린거다.

data = []
tree = driver.find_elements(By.CLASS_NAME, "product_item__MDtDF") # get className: double-click -> ctrl+c (after f12 dev tools click element)

for item in tree:
    name = item.find_element(By.CLASS_NAME, "product_title__Mmw2K").text
    price = item.find_element(By.CLASS_NAME, "price_num__S2p_v").text.replace("원", " KRW")
    link = item.find_element(By.CLASS_NAME, "product_link__TrAac").get_attribute("href")
    data.append([name,price,link])
    
df1 = pd.DataFrame(data, columns=["name", "price", "link"])
df1.to_csv("result2", index=False)