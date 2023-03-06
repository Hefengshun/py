# 通过一个第三方的机器去发送请求
import requests

# 59.37.18.243  端口3128   合成为59.37.18.243:3128
proxies = {
    # "http" : "" ,                  #由下面的链接前端部分决定用http还是https
    "https" : "http://59.37.18.243:3128"  # 有的版本前需要加https://   有的则不需要
}
i = 1
while 1 <= i <= 5 :
    resp = requests.get( "https://www.baidu.com" , proxies=proxies )
    resp.encoding = "utf-8"
    i += 1
    print( resp.text )
    print( f"输出的次数为{i}" )
