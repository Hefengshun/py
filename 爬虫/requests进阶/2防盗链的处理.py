# 1.拿到contID
# 2.拿到videoStatus返回json——> srcURl
# 3.srURl里面的内容进行修正
# 4.下载视频
import requests

# 拉取视频的网址
url = "https://www.pearvideo.com/video_1748613"
contID = url.split( "_" )[ 1 ]
videoStatusURl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.6841683759573365"
headers = {
    'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36" ,
    # 防盗链：溯源，当前本次请求的上一级是谁
    # 'Referer' : 'https://www.pearvideo.com/video_1748613'  #这里就可以写成
    'Referer' : url
}
resp = requests.get( videoStatusURl , headers=headers )
dic = resp.json( )
srcUrl = dic[ "videoInfo" ][ "videos" ][ "srcUrl" ]
systemTime = dic[ "systemTime" ]
# print( srcUrl , systemTime )
# 真实的链接  https://video.pearvideo.com/mp4/third/20211225/cont-1748613-15195380-175010-hd.mp4
# 拿到的链接  https://video.pearvideo.com/mp4/third/20211225/1640518712383-15195380-175010-hd.mp4      1640518712383
srcUrl = srcUrl.replace( systemTime , f"cont-{contID}" )
print( srcUrl )

# 下载视频
with open( "a.mp4" , mode="wb" ) as f :
    f.write( requests.get( srcUrl ).content )
