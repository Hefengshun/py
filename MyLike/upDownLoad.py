# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
#
# options = Options()
# # options.add_argument("--headless")  # 无头模式（建议新手先注释掉这一行）
# options.add_experimental_option("detach", True)  # 禁止自动关闭浏览器（建议新手开启）
# options.add_argument('--disable-gpu')
# options.add_argument("--start-maximized")  # 最大化窗口
# service = Service(r'D:\download\msedgedriver.exe')  # 你存放 driver 的路径
# driver = webdriver.Chrome(service=service, options=options)  # 创建 driver
# driver.get("https://www.baidu.com")
# element = driver.find_element(By.XPATH, '//*[@id="kw"]')
# element.send_keys("hello selenium")
# driver.find_element(By.XPATH, '//*[@id="su"]').click()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

from pyppeteer import launch
import asyncio
import json
import time
import sys
import os

# 以下为包装好的 Logger 类的定义
class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        # self.log = open(filename, "a")
        self.log = open(filename, "w", buffering=1, encoding="utf-8")  # 防止编码错误

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

# chrome_options = Options()
# out_path = r'E:\学习资料\py\data'  # 是你想指定的路径
# prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': out_path}
# chrome_options.add_experimental_option('prefs', prefs)
# # chrome_options.add_experimental_option("detach", True)  # 禁止自动关闭浏览器（建议新手开启）
# chrome_options.add_argument(r'E:\学习资料\py\amin\venv\Scripts\chromedriver.exe')
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("http://www.cip.cc/")
#正常进入
async def getData(username, password, url, exepath, urlTwo, downloadPath, startDate, overDate,assignUser,fourFormLocation):
    # print(username, password, url, exepath)
    # 'headless': False如果想要浏览器隐藏更改False为True
    # 127.0.0.1:1080为代理ip和端口，这个根据自己的本地代理进行更改，如果是vps里或者全局模式可以删除掉'--proxy-server=127.0.0.1:1080'
    # browser = await launch(
    #     {'headless': False, 'executablePath': exepath,
    #      'userDataDir': r'()E:\学习资料\py\data', })  # userDataDir设置无效但是会用本身浏览器 问题在于()
    # browser = await launch({'headless': False, 'userDataDir': r'()E:\\学习资料\\py\\data', })
    browser = await launch({'headless': True,'args': [
      #`--disable-extensions-except=/Users/mac/project/dev/puppeteer/extend`, // 不屏蔽这个插件 mac
      # `--disable-extensions-except=C:/Users/Administrator/Desktop/rechargenew`, // 不屏蔽这个插件 window
      '--disable-features=site-per-process', # 添加这个 控制iframe
    ]})
    # browser = await launch({'executablePath': exepath, 'headless': True, 'slowMo': 30})  # 用Chromeium浏览器
    page = await browser.newPage()
    # await page.setUserAgent(
    #     'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36')
    await page.goto(url)
    time.sleep(10)
    await page.waitForSelector('[type="submit"]')
    await  page.type('[name="username"]', username)
    await  page.type('[name="password"]', password)
    # await (await page.$('[name="password"]')).type('Abcd123456')
    await page.click('[type="submit"]')
    time.sleep(5)
    await page.goto(urlTwo)
    time.sleep(10)

    await page.waitForSelector('#nav [href="/web/secure/reportsHome#reportsactiontabcontentstructurechapter"]')
    await page.click('#nav [href="/web/secure/reportsHome#reportsactiontabcontentstructurechapter"]')
    time.sleep(5)
    await fourForm(page,fourFormLocation)  #四张表格的单独嵌入

    # time.sleep(10)
    await page.waitForSelector('[href="#ui-tabs-10"]')
    await page.click('[href="#ui-tabs-10"]')
    # 文件路径
    await mkdir('.'+downloadPath)
    await mkdir(r'.\startImg')
    await mkdir(r'.\overImg')
    aa = os.getcwd() + downloadPath
    # print('当前文件的路径', aa)
    cdp = await page.target.createCDPSession()
    await cdp.send('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': aa})  # 设置下载路径
    # 文件路径结束

    # 时间开始
    await page.waitForSelector('#fromDatePersonalVPDisplay')
    await page.waitForSelector('#toDatePersonalVPDisplay')
    await page.evaluate('document.querySelector("#fromDatePersonalVPDisplay").value=""')
    await page.evaluate('document.querySelector("#toDatePersonalVPDisplay").value=""')
    await page.type('#fromDatePersonalVPDisplay', startDate)
    await page.type('#toDatePersonalVPDisplay', overDate)
    await page.evaluate('document.querySelector("#ui-datepicker-div").style.visibility = "hidden"')
    # 时间结束

    await page.waitForSelector('#ui-tabs-10 #membershipIdMemberPersonalVP')
    # switchover = await page.querySelector('#ui-tabs-10 #membershipIdMemberPersonalVP')
    # await switchover.click()
    option = await page.querySelectorAll('#ui-tabs-10 #membershipIdMemberPersonalVP option')
    # await page.click('#ui-tabs-10 #membershipIdMemberPersonalVP')
    # time.sleep(60)
    optionValueArr=[]
    for i,item in enumerate(option):
        # print(i,item)
        # NowDom = option[i]
        optionValueArr.append({'value':await (await item.getProperty('value')).jsonValue(),'state':'NO','text':await (await item.getProperty('text')).jsonValue()})
    print(optionValueArr,'获得下拉框的value！！！！！！！！！！！！！！！！')
    index: int = 0
    print(index,"查看index的变化")
    if assignUser == 'None':
        await recursionPrint(optionValueArr,page,index);
    else:
        await assignUserPrint(optionValueArr,page,assignUser)


    await browser.close()  # 关闭浏览器文件貌似保存不下来

#四张单独表格
async def fourForm(page,fourFormLocation):
    print("四张表开始")



    # 通用文件路径
    await mkdir('.'+ fourFormLocation)
    await mkdir(r'.'+fourFormLocation+'\startImg')
    await mkdir(r'.'+fourFormLocation+'\overImg')
    # 通用文件路径结束

    # 第一个开始
    print("第一个开始")
    await mkdir(r'.' + fourFormLocation + '\分会名单报告')
    aa = os.getcwd() + fourFormLocation + '\分会名单报告'
    # print('当前文件的路径', aa)
    cdp = await page.target.createCDPSession()
    await cdp.send('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': aa})  # 设置下载路径
    await page.screenshot(
        {'path': '.' + fourFormLocation + '\startImg\分会名单报告按钮.png', 'quality': 100,
         'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事

    await page.waitForSelector('[href="#ui-tabs-2"]')
    await page.click('[href="#ui-tabs-2"]')

    time.sleep(5)

    await page.waitForSelector('#chapter_Roster_Report #button')
    await page.click('#chapter_Roster_Report #button')
    time.sleep(10)
    frame = page.frames
    await page.screenshot(
        {'path': '.' + fourFormLocation + '\startImg\分会名单报告.png', 'quality': 100,
         'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
    frameDom = searchIframe(frame, page)
    if frameDom == None:
        time.sleep(10)
        frame = page.frames
        await page.screenshot(
            {'path': '.' + fourFormLocation + '\startImg\分会名单报告.png', 'quality': 100,
             'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
        frameDom = searchIframe(frame, page)
    print(frameDom, "获取指定iframe")
    time.sleep(10)
    await frameDom.waitForSelector('#links_1')
    await page.screenshot(
        {'path': '.' + fourFormLocation + '\overImg\分会名单报告.png', 'quality': 100,
         'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
    await frameDom.click('#links_1')
    time.sleep(10)
    close = await page.querySelector('.ui-dialog-titlebar-close')
    if close == None:
        time.sleep(10)
        close = await page.querySelector('.ui-dialog-titlebar-close')
    await close.click()
    time.sleep(20)

    # 第二个开始
    print("第二个开始")
    await mkdir(r'.' + fourFormLocation + '\会员资格到期报告')
    aa = os.getcwd() + fourFormLocation + '\会员资格到期报告'
    # print('当前文件的路径', aa)
    cdp = await page.target.createCDPSession()
    await cdp.send('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': aa})  # 设置下载路径


    await page.waitForSelector('[href="#ui-tabs-3"]')
    await page.click('[href="#ui-tabs-3"]')

    time.sleep(5)

    await page.waitForSelector('#chapter_Membership_Dues_Report_Form #button')
    await page.click('#chapter_Membership_Dues_Report_Form #button')
    time.sleep(10)
    frame = page.frames
    await page.screenshot(
        {'path': '.' + fourFormLocation + '\startImg\会员资格到期报告.png', 'quality': 100,
         'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
    frameDom = searchIframe(frame, page)
    if frameDom == None:
        time.sleep(10)
        frame = page.frames
        await page.screenshot(
            {'path': '.' + fourFormLocation + '\startImg\会员资格到期报告.png', 'quality': 100,
             'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
        frameDom = searchIframe(frame, page)
    print(frameDom, "获取指定iframe")
    time.sleep(10)
    await frameDom.waitForSelector('#links_1')
    await page.screenshot(
        {'path': '.' + fourFormLocation + '\overImg\会员资格到期报告.png', 'quality': 100,
         'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
    await frameDom.click('#links_1')
    time.sleep(10)
    close = await page.querySelector('.ui-dialog-titlebar-close')
    if close == None:
        time.sleep(10)
        close = await page.querySelector('.ui-dialog-titlebar-close')
    await close.click()
    time.sleep(20)

    # 第三个开始
    print("第三个开始")
    await mkdir(r'.' + fourFormLocation + '\分会红绿灯报告')
    aa = os.getcwd() + fourFormLocation + '\分会红绿灯报告'
    # print('当前文件的路径', aa)
    cdp = await page.target.createCDPSession()
    await cdp.send('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': aa})  # 设置下载路径
    await page.waitForSelector('[href="#ui-tabs-17"]')
    await page.click('[href="#ui-tabs-17"]')

    time.sleep(5)

    await page.waitForSelector('#reportDateChapterTrafficLights')
    await page.click('#reportDateChapterTrafficLights')
    time.sleep(2)
    await page.waitForSelector('#ui-datepicker-div .ui-priority-primary')
    await page.click('#ui-datepicker-div .ui-priority-primary')
    time.sleep(5)
    await page.waitForSelector('#chapter_Chapter_Traffic_Lights  #button')
    await page.click('#chapter_Chapter_Traffic_Lights  #button')
    time.sleep(10)
    frame = page.frames
    await page.screenshot(
        {'path': '.' + fourFormLocation + '\startImg\分会红绿灯报告.png', 'quality': 100,
         'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
    frameDom = searchIframe(frame, page)
    if frameDom == None:
        time.sleep(10)
        frame = page.frames
        await page.screenshot(
            {'path': '.' + fourFormLocation + '\startImg\分会红绿灯报告.png', 'quality': 100,
             'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
        frameDom = searchIframe(frame, page)
    print(frameDom, "获取指定iframe")
    time.sleep(10)
    await frameDom.waitForSelector('#links_1')
    await page.screenshot(
        {'path': '.' + fourFormLocation + '\overImg\分会红绿灯报告.png', 'quality': 100,
         'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
    await frameDom.click('#links_1')
    time.sleep(10)
    close = await page.querySelector('.ui-dialog-titlebar-close')
    if close == None:
        time.sleep(10)
        close = await page.querySelector('.ui-dialog-titlebar-close')
    await close.click()
    time.sleep(20)

    # 第四个开始
    print("第四个开始")
    await mkdir(r'.' + fourFormLocation + '\会员年龄报告')
    aa = os.getcwd() + fourFormLocation + '\会员年龄报告'
    # print('当前文件的路径', aa)
    cdp = await page.target.createCDPSession()
    await cdp.send('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': aa})  # 设置下载路径
    await page.waitForSelector('[href="#ui-tabs-18"]')
    await page.click('[href="#ui-tabs-18"]')

    time.sleep(5)

    await page.waitForSelector('#chapter_Length_of_Membership_Report #button')
    await page.click('#chapter_Length_of_Membership_Report #button')
    time.sleep(10)
    frame = page.frames
    await page.screenshot(
        {'path': '.' + fourFormLocation + '\startImg\会员年龄报告.png', 'quality': 100,
         'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
    frameDom = searchIframe(frame, page)
    if frameDom == None:
        time.sleep(10)
        frame = page.frames
        await page.screenshot(
            {'path': '.' + fourFormLocation + '\startImg\会员年龄报告.png', 'quality': 100,
             'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
        frameDom = searchIframe(frame, page)
    print(frameDom, "获取指定iframe")
    time.sleep(10)
    await frameDom.waitForSelector('#links_1')
    await page.screenshot(
        {'path': '.' + fourFormLocation + '\overImg\会员年龄报告.png', 'quality': 100,
         'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
    await frameDom.click('#links_1')
    time.sleep(10)
    close = await page.querySelector('.ui-dialog-titlebar-close')
    if close == None:
        time.sleep(10)
        close = await page.querySelector('.ui-dialog-titlebar-close')
    await close.click()
    time.sleep(20)
    print("四张表完成")

#遍历去下载 （修改状态）
async def recursionPrint(optionValueArr,page,index):
        if optionValueArr[index]['state'] == 'NO' and index<(int(len(optionValueArr))):
            print(optionValueArr[index - 1]['state'], optionValueArr[index]['state'], index + 1,
                  optionValueArr[index]['text'], "当前进行的下载项")
            try:
                num = index + 1
                time.sleep(10)
                await page.select('#membershipIdMemberPersonalVP', optionValueArr[index]['value'])  # select 是select固定的方法
                time.sleep(10)
                await page.waitForSelector('#ui-tabs-10 #button')
                await page.click('#ui-tabs-10 #button')
                await page.waitForSelector('#reportsIFrame')
                time.sleep(10)
                frame = page.frames
                await page.screenshot(
                    {'path': './startImg/iframe' + str(num) + '.png', 'quality': 100,
                     'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
                frameDom = searchIframe(frame, page)
                if frameDom == None:
                    time.sleep(10)
                    frame = page.frames
                    await page.screenshot(
                        {'path': './startImg/iframe' + str(num) + '.png', 'quality': 100,
                         'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
                    frameDom = searchIframe(frame, page)
                print(frameDom, "获取指定iframe")
                # DownUrl = frameDom.url
                # print(DownUrl)
                time.sleep(10)
                # await page.goto(DownUrl)  # 这一块主要打开文件下载url会让页面关闭，加了try
                await frameDom.waitForSelector('#links_1')
                await page.screenshot({'path': './overImg/over' + str(num) + '.png', 'quality': 100, 'fullPage': True})
                await frameDom.click('#links_1')
                time.sleep(10)
                close = await page.querySelector('.ui-dialog-titlebar-close')
                if close == None:
                    time.sleep(10)
                    close = await page.querySelector('.ui-dialog-titlebar-close')
                # print(close)
                await close.click()
                time.sleep(20)
                optionValueArr[index]['state']="OK"
                print("文件" + str(num) + "下载完成")
                # print(optionValueArr[index]['state'],'完成状态')
                index+=1
                if index == int(len(optionValueArr)):
                    return
                await recursionPrint(optionValueArr, page, index)
            except :
                print("文件" + str(num) + "下载失败 重新下载")
                optionValueArr[index]['state']="NO"
                time.sleep(5)
                await recursionPrint(optionValueArr, page, index)
        else:
            return

#指定用户
async def assignUserPrint(list,page,assignUser):
    userObj = None
    for i, men in enumerate(list):
        strings = men['text'].replace(" ", '')
        # print(men,assignUser,men['text'],strings)
        if strings==assignUser:
            userObj=men
    print(userObj,userObj['value'],userObj['text'],'指定人的')
    try:
        await page.select('#membershipIdMemberPersonalVP', userObj['value'])  # select 是select固定的方法
        time.sleep(2)
        await page.waitForSelector('#ui-tabs-10 #button')
        await page.click('#ui-tabs-10 #button')
        await page.waitForSelector('#reportsIFrame')
        time.sleep(5)
        frame = page.frames
        await page.screenshot(
            {'path': './startImg/userIframe.png', 'quality': 100,
                     'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
        frameDom = searchIframe(frame, page)
        # print(frameDom)
        if frameDom == None:
            time.sleep(5)
            frame = page.frames
            await page.screenshot(
                        {'path': './startImg/userIframe.png', 'quality': 100,
                         'fullPage': True})  # 打印去掉就找不到iframe了  不知道怎么回事
            frameDom = searchIframe(frame, page)
        print(frameDom, "获取指定iframe")
                # DownUrl = frameDom.url
                # print(DownUrl)
        time.sleep(5)
                # await page.goto(DownUrl)  # 这一块主要打开文件下载url会让页面关闭，加了try
        await frameDom.waitForSelector('#links_1')
        await page.screenshot({'path': './overImg/userOver.png', 'quality': 100, 'fullPage': True})
        await frameDom.click('#links_1')
        time.sleep(10)
        close = await page.querySelector('.ui-dialog-titlebar-close')
        if close == None:
            time.sleep(10)
            close = await page.querySelector('.ui-dialog-titlebar-close')
        # print(close)
        await close.click()
        time.sleep(10)
        userObj['state'] = "OK"
        print("文件指定人" + assignUser + "下载完成")
    except :
            print("文件指定人下载错误")
            userObj['state'] = "NO"
            time.sleep(5)
            await assignUserPrint(list,page,assignUser)

# 寻找iframe
def searchIframe(iframe, page):
    # global nowIframe
    # await page.waitForSelector('#reportsIFrame')
    # iframe = page.frames
    # print(iframe, nowIframe, "值")
    for i in iframe:
        if i.name == 'reportsIFrame':
            return i
    # print(nowIframe, "找到了？")
    # if nowIframe == None:
    #     time.sleep(10)
    #     searchIframe(iframe, page)
    # else:
    #     return nowIframe

#文件路径的处理
async def mkdir(path):
    folder = os.path.exists(path)
    # print(folder)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        # print("---  OK  ---")
    else:
        print("---  There is this folder!  ---")

if __name__ == '__main__':
    # 将下面这句放在所有想输出到文本文档的 print 函数之前
    sys.stdout = Logger('out_log.txt')
    with open('config.json', 'r', encoding='utf8') as fp:
        allJson = json.load(fp)
        nowIframe = None
        username =  allJson['username']
        password = allJson['passWord']
        idsList = None
        if  'idsList' in allJson:
            idsList = allJson['idsList']
        url = allJson['url']
        urlTwo = allJson['urlTwo']
        exepath = allJson['exePath']
        downloadPath = allJson['downloadPath']  # 创建文件 保存
        startDate = allJson['startDate']
        overDate = allJson['overDate']
        assignUser = allJson['assignUser']
        fourFormLocation = allJson['fourFormLocation']
        print(username, password, url, urlTwo, exepath, downloadPath, startDate, overDate,assignUser,fourFormLocation,"拿到配置信息")
        if idsList != None and len(idsList) != 0 :
            for i, item in enumerate(idsList):
                print(i, item,"多个用户账户时，当前的账户！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
                asyncio.get_event_loop().run_until_complete(
                    getData(item['username'],item['passWord'], url, exepath, urlTwo, downloadPath, startDate, overDate, assignUser,fourFormLocation))
        else:
            asyncio.get_event_loop().run_until_complete(
                getData(username, password, url, exepath, urlTwo, downloadPath, startDate, overDate,assignUser,fourFormLocation))
