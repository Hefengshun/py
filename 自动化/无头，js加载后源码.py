from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome

# 准备好配置参数
opt = Options( )
opt.add_argument( "--headless" )
opt.add_argument( "--disbale-gpu" )

# 创建一个浏览器的对象
web = Chrome( options=opt )  # 把参数配置设置到浏览器中

# js加载数据后  拿到源码 的代码是  web.page_source
web.page_source
