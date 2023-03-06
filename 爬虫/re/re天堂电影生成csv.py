import requests
import re
import csv

url = "https://www.dydytt.net/index2.htm"
url2 = "https://www.dydytt.net/"
send = requests.get( url )  # verify=False  去掉安全验证
send.encoding = "gb2312"  # 这里改变编码格式 看标签head里的<META http-equiv=Content-Type content="text/html; charset=gb2312">中的charset
# print( send.text )

obj1 = re.compile( r"2021新片精品.*?<ul>(?P<ul>.*?)</ul>" , re.S )
obj2 = re.compile( r"<a href='(?P<herf>.*?)'" , re.S )
obj3 = re.compile( r'◎译　　名(?P<panming>.*?)<br />.*?<a target="_blank" href="(?P<xialian>.*?)">' , re.S )
result1 = obj1.finditer( send.text )
chiden_herf_list = [ ]
for it in result1 :
    ul = it.group( "ul" )
    # print( ul )  # 拿到ul里的 li 了
    result2 = obj2.finditer( ul )
    for itt in result2 :
        # 拼接子页面的url
        # 域名＋子页面地址  有的需要 有的不需要
        # print( itt.group( "herf" ).strip( "/" ) )
        chide_hear = url2 + itt.group( "herf" )
        chiden_herf_list.append( chide_hear )  # 把子页面连接保存起来

# 因为第一个herf不是所以删除


del (chiden_herf_list[ 0 ])

# 准备一个文件把数据写进去
f = open( "2021最新电影下载地址.csv" , mode="w" )
# 写东西
csvwriter = csv.writer( f )

# 提取子页面的内容


for href in chiden_herf_list :
    chide_resp = requests.get( href , verify=False )
    chide_resp.encoding = "gb2312"
    result3 = obj3.finditer( chide_resp.text )
    for i in result3 :
        dic = i.groupdict( )
        csvwriter.writerow( dic.values( ) )
f.close( )
