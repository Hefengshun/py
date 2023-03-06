# 1.拿到主页面的源代码，然后提取到子页面的链接地址，href
# 2.通过href拿到子页面的内容，从子页面找到图片的下载地址
# 3.下载图片
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/meinvbizhi/yangyanmeinv.htm"
url2 = "https://www.umei.cc"
resp = requests.get( url )
resp.encoding = "utf-8"  # 处理乱码
# 把源代码交给BeautifulSoup
main_page = BeautifulSoup( resp.text , "html.parser" )

alist = main_page.find( "div" , class_="TypeList" ).find_all( "a" )  # 把范围第一次缩小
# print( alist )
for i in alist :
    href = url2 + i.get( "href" )
    # 拿到子页面的源代码
    child_page_resp = requests.get( href )
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    # 从子页面拿到下载路径
    child_page = BeautifulSoup( child_page_text , "html.parser" )
    imghref = child_page.find( "div" , class_="ImageBody" ).find( "img" )
    src = imghref.get( "src" )
    # 下载图片
    img_resp = requests.get( src )
    # img_resp.content  #这里是拿到是字节   把字节写进文件 文件就是图片
    img_name = src.split( "/" )[ -1 ]  # 拿到url后面的内容
    with open( "img/" + img_name , mode="wb" ) as f :  # img文件夹加进去
        f.write( img_resp.content )  # 图片内容写入文件
    print( "over!!" , img_name )
    time.sleep( 1 )

print( "all over" )
