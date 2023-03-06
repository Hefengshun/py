# 登录  -> 得到cookie
# 带着cookie 去请求到书架url -> 书架上的内容
# 必须得把上面的的两个操作连起来
# 我们可以用session进行请求 -> session你可以认为是一连串的请求，在这个过程中cookie不会丢失
import requests

#
# # 会话
# session = requests.session( )
# # 1.登录
# url = "https://passport.17k.com/ck/user/login"
# data = { 'loginName' : '15518191739' , 'password' : 'HEfengshun.1029' }
# session.post( url , data=data )
# # print( resp.text )
# # print( resp.cookies )  #看cookie
# # 2.拿书架数据
# # 刚才那个session中是有cookie的
# url2 = "https://user.17k.com/ck/user/mine/readList?page=1&appKey=2406394919"
# resp = session.get( url2 )
# print( resp.json( ) )

# 方法2
resp = requests.get( "https://user.17k.com/ck/user/mine/readList?page=1&appKey=2406394919" , headers={
    "Cookie" : "GUID=942f5f72-a1a7-4491-9b15-71f473807370; sajssdk_2015_cross_new_user=1; _openId=ow-yN5ueX3q_-0_Kn-wwESYobQfU; c_channel=0; c_csc=web; BAIDU_SSP_lcr=https://open.weixin.qq.com/; Hm_lvt_9793f42b498361373512340937deb2a0=1640510817,1640510906; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F11%252F11%252F07%252F87390711.jpg-88x88%253Fv%253D1640511464000%26id%3D87390711%26nickname%3Dtakeoff12%26e%3D1656063806%26s%3D81e3405605a9e26f; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2287390711%22%2C%22%24device_id%22%3A%2217df610821496a-00557cfa84f9cd-978153c-1327104-17df6108215c4d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%AB%99%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22open.weixin.qq.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22942f5f72-a1a7-4491-9b15-71f473807370%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1640512807"
} )
print( resp.text )
