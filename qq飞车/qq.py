# -*- coding : utf-8-*-
import tkinter as tk
import random
import threading
import time

import tkinter
from tkinter.messagebox import *

window = tkinter.Tk()
# window.iconphoto(True, tkinter.PhotoImage(file='qq.png'))
window.withdraw()  # 退出默认 tk 窗口


def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('系统提示！')
    window.geometry("360x120" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text='上号 上号！',  # 标签的文字
             bg='white',  # 背景颜色
             font=('楷体', 17),  # 字体和字体大小
             width=30, height=5  # 标签长宽
             ).pack()  # 固定窗口位置
    window.mainloop()


threads = []
result = askquestion('QQ飞车', '上号玩游戏?')
print(result)
if result == 'no':
    result = askyesno('不要选错了', '这个是错误的选择，确定还要继续吗？')
    if result:
        for i in range(50):  # 需要的弹框数量
            t = threading.Thread(target=dow)
            threads.append(t)
            time.sleep(0.1)
            threads[i].start()
    else:
        result = askquestion('QQ飞车', '上号玩游戏?')
        if result:
            tkinter.messagebox.showerror('Windows错误', 'Windows被攻击正在搭建防火墙')
else:
    for i in range(5):
        tkinter.messagebox.showerror('Windows错误', 'Windows被攻击正在搭建防火墙')
