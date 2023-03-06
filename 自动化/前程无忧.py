from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# 准备好配置参数
opt = Options( )
opt.add_argument( "--headless" )
opt.add_argument( "--disbale-gpu" )

# 创建一个浏览器的对象
web = Chrome( options=opt )  # 把参数配置设置到浏览器中
# web = Chrome( )
web.get( "https://www.51job.com/?from=baidupz" )

# 点击地区
web.find_element( By.XPATH , '/html/body/div[5]/div[1]/div[1]/div/a[4]' ).click( )

# 跳转新选项卡页面睡上三秒
time.sleep( 3 )
# 视角调整到新的窗口里面
web.switch_to.window( web.window_handles[ -1 ] )
# 在新的窗口里提取内容
web.find_element( By.XPATH , '//*[@id="kwdselectid"]' ).send_keys( "前端" , Keys.ENTER )
# 输入搜索之后页面发生了变化  需要在此定位选项卡
web.switch_to.window( web.window_handles[ -1 ] )
time.sleep( 7 )
inputs = web.find_element( By.XPATH , '//*[@id="jump_page"]' )
for num in range( 1 , 101 ) :
    inputs.clear( )
    inputs.send_keys( num )
    web.find_element( By.XPATH , '/html/body/div[2]/div[3]/div/div[2]/div[4]/div[2]/div/div/div/span[3]' ).click( )
    time.sleep( 2 )
    lists = web.find_elements( By.XPATH , '/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div' )
    for item in lists :
        item.find_element( By.XPATH , ' a / p[ 1 ] / span[ 1 ]' ).click( )
        time.sleep( 5 )
        web.switch_to.window( web.window_handles[ -1 ] )
        message = web.find_element( By.XPATH , '/html/body/div[3]/div[2]/div[3]/div[1]/div' )
        print( message.text )
        # 关掉子窗口
        time.sleep( 1 )
        web.close( )
        # 还需要变更
        time.sleep( 1 )
        web.switch_to.window( web.window_handles[ -1 ] )

web.close( )
