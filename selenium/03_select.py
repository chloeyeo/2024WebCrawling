from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # remove any non-necessary logs
options.add_experimental_option("detach", True) # stop the webdriver from turning off
options.add_argument("--start-maximized") # start webdriver with max browser screen size
# options.add_argument("headless") # so we don't see the webdriver in browser and it just runs in background

service = Service()
driver = webdriver.Chrome(service=service, options=options) # start a webdriver and make its options set to chrome
# webdriver is used for dynamic crawling - to get the data dynamically as if the chrome webdriver is a person
# it will be perceived as if the webdriver is a person because we're setting its options as chrome
# so our webdriver with chrome options will be recognized as a Chrome browser (=thus perceive this as a human/coming from a human
# as if a human actually opened their browser to visit the web pages when it's actually our webdriver crawling).

driver.get("https://www.naver.com")

# .find_element() is same as select_one() (for plural .find_elements() which is same as select())
search = driver.find_element(By.ID, "query") # 네이버 검색창 input element의 id="query" 이기 때문에 By.ID 를 "query"라고 지정해준거임.
search.click() # 그 검색창 element를 인위적으로 클릭해준다.
search.send_keys("모니터", Keys.ENTER) # 검색창에 "모니터" 쓰고 엔터키 누른다 (=검색).