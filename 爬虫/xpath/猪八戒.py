import requests
from lxml import etree

url = "https://guangzhou.zbj.com/search/f/?kw=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91"
resp = requests.get( url )
# print( resp.text )
# 解析
html = etree.HTML( resp.text )
# 拿到每一个服务商的div
divs = html.xpath( "/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div" )
for div in divs :
    divtext = div.xpath( "./div/div/a[2]/div[2]/div[1]/span[1]/text()" )[ 0 ].strip( "¥" )
    ptext = "开发".join( div.xpath( "./div/div/a[2]/div[2]/div[2]/p/text()" ) )
    gstext = div.xpath( "./div/div/a[1]/div[1]/p/text()" )[ 1 ].strip( "\n\n" )
    hometext = div.xpath( "./div/div/a[1]/div[1]/div/span/text()" )
    # print( divtext )
    # print( ptext )
    print( gstext )
    # print( hometext )
