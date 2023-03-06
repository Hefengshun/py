import requests
import re
import csv

url = "https://movie.douban.com/chart"
params = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
res = requests.get( url , headers=params )
s = res.text
# 解析数据
# 单双引号必须与页面的相同  页面里面 标签用双引号 这里的标签里面也得是双引号
obj = re.compile(
    r'<td valign="top">.*?<div class="pl2">.*?<span style="font-size:13px;">(?P<name>.*?)</span>.*?'
    r'<div class="star clearfix">.*?<span class="pl">(?P<porper>.*?)</span>' ,
    re.S )
result = obj.finditer( s )
# 准备一个文件把数据写进去
f = open( "data.csv" , mode="w" )
# 写东西
csvwriter = csv.writer( f )
for i in result :
    dic = i.groupdict( )
    csvwriter.writerow( dic.values( ) )
    # print( i.group( "name" ) )
    # print( i.group( "porper" ) )
f.close( )
print( "over!!" )
