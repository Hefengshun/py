import requests

# 原本的url= https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0&genres=%E5%96%9C%E5%89%A7
url = "https://movie.douban.com/j/new_search_subjects"
# 如果发现get方法请求的url很长就可以在？号后删除 但是要重新封装参数 （问号后的就是参数）
param = {
    "sort" : 'U' ,
    "range" : ' 0 , 10 ' ,
    'tags' : "" ,
    'start' : 0 ,
    'genres' : '喜剧'
}
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
# get方式发送参数是paramss
res = requests.get( url=url , params=param , headers=headers )
print( res.json( ) )  # 现在没有出现 就是禁止爬虫了
# 现在就要看一下默认的User-Agent是什么
# print(res.request.headers )  # {'User-Agent': 'python-requests/2.26.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
# 这代表别人发现我是py请求的  所以要找到User-Agent
res.close( )  # 关掉res
