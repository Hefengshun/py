# 1.找到未加密的参数                    #window.arsea(参数，xxx，xxx，xxx)
# 2.想办法把参数加密（必须参考网易的逻辑），params=encText，encSecKey=encSecKey
# 3.请求到网易，拿到评论信息
# 需要安装pycrypto    但是要执行这个pip install pycryptodome
import requests
from Crypto.Cipher import AES
from base64 import b64decode
import json

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

# 请求方式POST
data = {
    "csrf_token" : "" ,
    "cursor" : "-1" ,
    "offset" : "0" ,
    "orderType" : "1" ,
    "pageNo" : "1" ,
    "pageSize" : "20" ,
    "rid" : "R_SO_4_1376142151" ,
    "threadId" : "R_SO_4_1376142151"
}
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
e = "010001"
i = "mieMhzZfN3dfRwXs"


def get_encSecKey( ) :
    return "65920bec6bc7ff4c65507474845d6f79fa6c4f97aa06179ad1f109545d42417922f13dddc83e5db3ffd795230cc7933210a7f16f6ba01f31b28d33e7610829e096aaa37561aedbf8ecb0ff0df209196331accbbc91175c8bc79abb38ff32cf80f030b4690815f5af846846998e4cc7dd29e1cdf1af09967d9460c283c9fb75fb"


def to_16( data ) :
    # data += '='
    # print( len( data ) )
    data = data.replace( data[ -1 ] , "=" )[ :-1 ]
    pad = 16 - len( data ) % 16
    data += chr( pad ) * pad

    # data += '=' * (-len( data ) % 4)
    print( json.dumps( data ) )
    print( len( data ) )
    return data


def get_params( data ) :
    # 默认这里收到是字符串
    first = enc_params( data , g )
    second = enc_params( first , i )
    return second
    # 返回的就是params


def enc_params( data , key ) :
    # 加密过程
    iv = "0102030405060708"
    data = to_16( data )
    aes = AES.new( key=key.encode( "utf-8" ) , IV=iv.encode( 'utf-8' ) , mode=AES.MODE_CBC )
    # 创建加密器
    bs = aes.encrypt( data.encode( "utf-8" ) )
    # 加密,加密的内容的长度必须是16的倍数
    return str( b64decode( bs ) , "utf-8" )
    # 转化成字符串返回

    # 处理加密过程


"""
        function a(a) {   #返回的16位随机的字符串
            var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
            for (d = 0; a > d; d += 1)  #循环16次
                e = Math.random() * b.length,  #随机数
                e = Math.floor(e),  #取整
                c += b.charAt(e);  #去字符串中的xxx位置  这里就把字母e拿出来了
            return c
        }
        function b(a, b) {   #a是要加密的内容，
            var c = CryptoJS.enc.Utf8.parse(b)  c为是b  b就是密钥
              , d = CryptoJS.enc.Utf8.parse("0102030405060708")
              , e = CryptoJS.enc.Utf8.parse(a)  #e是数据
              , f = CryptoJS.AES.encrypt(e, c, {  #AES加密书法   #c是加密的密钥
                iv: d,   #偏移量
                mode: CryptoJS.mode.CBC  #CBC模式 加密
            });
            return f.toString()
        }
        function c(a, b, c) {  #c里面不产生为随机数
            var d, e;
            return setMaxDigits(131),
            d = new RSAKeyPair(b,"",c),
            e = encryptedString(d, a)
        }
        function d(d, e, f, g) {    #(d:就是数据  e:010001  f:应为太长让道上面f的变量里      g:0CoJUm6Qyw8W8jud)
            var h = {}   #空对象
              , i = a(16);      #a其实是上面的函数   i就是一个16位的随机值  ，把i设置成定值
            return h.encText = b(d, g),    #g密钥
            h.encText = b(h.encText, i),   #这个地方返回的就是params    i也是密钥
            h.encSecKey = c(i, e, f),       #这个地方就是encSecKey  e和f是定死的  i是随机的 执行偏差就是在i身上  i一旦固定的到的key就是固定的
            h
        }
        
        两次加密  ：
        数据+g=》b=》 第一次加密+i=>  b =params
"""
resp = requests.post( url , data={
    "params" : get_params( json.dumps( data ) ) ,
    "encSecKey" : get_encSecKey( )
} )
print( resp.text )
