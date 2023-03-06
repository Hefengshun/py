from  selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
import  time

we = Chrome()
we.get('http://localhost:8080/')
el=we.find_element(By.XPATH, '//*[@id="app"]/div[2]/button[1]' )
# for i in el:
while True:
    time.sleep(0.1)
    el.click() #点击事件