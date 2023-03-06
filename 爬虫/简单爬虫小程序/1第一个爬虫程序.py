# 引入一个内置的库
from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen( url )

# print( )
with open( "mybaidu.html" , mode="w" , encoding="utf-8" ) as f :
    f.write( resp.read( ).decode( "utf-8" ) )  # 读取到网页的源代码 并用写进了 f
print( "over" )
