import re

# 正则前面加一个r 转义用的
# findall：匹配字符串中所以符合正则的内容
# lst = re.findall( r"\d+" , "我的电话号是：10086，我女朋友的电话是：10010" )
# print( lst )  # ['10086', '10010']

#

# 这个是重点用到
# finditer：匹配字符串中所以的内容[返回的是迭代器]
# it = re.finditer( r"\d+" , "我的电话号是：10086，我女朋友的电话是：10010" )
# print( it )  # <callable_iterator object at 0x000001E159314790>
# for i in it :
#     print( i )
#     # <re.Match object; span=(7, 12), match='10086'>
#     # <re.Match object; span=(22, 27), match='10010'>
#     print( i.group( ) )  # 10086  10010  可以通过group函数那到match


# # search 只解锁一个就返回的是match对象，拿数据.group()
# s = re.search( r"\d+" , "我的电话号是：10086，我女朋友的电话是：10010" )
# print( s )  # <re.Match object; span=(7, 12), match='10086'>
# print( s.group( ) )  # 10086

# match  重头开始匹配  匹配一个也返回
# s = re.match( r"\d+" , "10086，我女朋友的电话是：10010" )
# print( s )  # <re.Match object; span=(0, 5), match='10086'>
# print( s.group( ) )  # 10086


# 预加载正则

# 使用compile先把正则加载
# obj = re.compile( r"\d+" , re.S )  # re.S:能匹配换行符
# res = obj.finditer( "我的电话号是：10086，我女朋友的电话是：10010" )
# print( res )  # <callable_iterator object at 0x00000171399141F0>
# # 重复使用
# s = obj.findall( "我的电话号是：186，我女朋友的电话是：10010" )
# print( s )  # ['186', '10010']

#


#
s = """<div class='sadsad'>是防辐射<div>
<div class='gdfgdf'>电饭锅<div>
<div class='vsdvs'>更好那个<div>
<div class='dsdfs'>同意他人<div>
<div class='dfsfdds'>给你还能<div>

"""
# (?P<分组的名字>正则)  可以单独从内容中进一步提取到内容
obj = re.compile( r"<div class='.*?'>(?P<shuju>.*?)<div>" , re.S )
result = obj.finditer( s )
for i in result :
    print( i.group( "shuju" ) )
