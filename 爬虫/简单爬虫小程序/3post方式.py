import requests

url = "https://fanyi.baidu.com/sug"
s = input( "请输入你要翻译的英文" )
dat = {
    "kw" : s
}
# 发送post请求，发送的数据必须放在字典中，通过data参数进行传递
# 发送请求
resp = requests.post( url , data=dat )
# print( resp.json( ) )  # 将服务器返回的数据直接返回为json=> dict
s=resp.json( )
for i in s["data"]:
    print(i)
resp.close( )  # 关掉res
