import requests
import re

url = "http://www.0755xsit.com/shizi/jpjs.html"
obj = re.compile( r'<div class="teaname">(?P<name>.*?)</div>.*?<p>(?P<jieshao>.*?)</p>' , re.S )
dat = {
    'id' : 61747565 ,
    'sid' : 'b13a9ed54b94413386dfe70adadc2dc9' ,
    'maxid' : 121290 ,
    '_text' : '' ,
    'lng' : 'cn' ,
    'pp' : '547f' ,
    'sid1' : 'b13a9ed54b94413386dfe70adadc2dc9'
}
hear = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
res = requests.get( url=url , params=dat , headers=hear )
res.encoding = "utf-8"
result = obj.finditer( res.text )
with open( "老师信息.csv" , mode="w" , encoding="utf-8" ) as f :
    for i in result :
        f.write( i.group( "name" ) )
        f.write( ":" )
        f.write( i.group( "jieshao" ).strip( ) )
        f.write( "\n" )
print( "over!!!" )
