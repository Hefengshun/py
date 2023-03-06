from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 创建一个浏览器对象
web = Chrome()
# 打开一个网址
web.get("https://www.lagou.com/")

# 找到某个元素点击
el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/ul/li[6]/a')
el.click()  # 点击事件
# print(web.title)
time.sleep(1)  # 让浏览器缓一会
input = web.find_element(By.XPATH, '//*[@id="search_input"]')
input.send_keys("python", Keys.ENTER)
# 找到输入框 写入Python 并后面跟上操作

# 查找数据
# 找到页面中存放数据的标签
div = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')
for i in div:
    name = i.find_element(By.XPATH, './div/div/div[1]/span').text
    print(name)
