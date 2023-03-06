# pip install bs4
import requests
from bs4 import BeautifulSoup
url="http://www.xinfadi.com.cn/index.html"
res = requests.get(url)


#解析数据BeautifulSoup进行处理 生成bs4对象
page = BeautifulSoup(res.text,"html.parser")  #指定一个解析器
# 2.从bs对象中查找数据
# find(标签,属性=值)   一个
# find_all(标签,属性=值)  一堆
table=page.find("tbody",attrs={
    "id":"ulTableBody",
    "class":"ul"
})
print(table)
# 1.把页面中的源码交给
# print(res.json())