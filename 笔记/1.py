# from os import close, name
# from typing import Text, Type, ValuesView

# print()用于输出 多个单词不换行输出中间需要加逗号
# 也可输入表达式 计算为4
# print(3+1) 
# print("sdds");
# print(250)


# 输出的目的地有屏幕 文件
# 1.输出到文件 open() 用于打开文件
# 意思是打开（这里必须是c盘外的其它盘）D盘里的 Text文件  如果没有有创建 a+ 


# open("D:/text.txt","a+") #代表没有文件夹的情况下就创建 存在就在文件后面追加


# 用一个变量hourlies接收

# hourlies=open("D:/text.txt","a+")


# 用输出print方法把heferngshun输出到jailhouse这个变量里  而这个变量是一个文件夹  等同于输出道text里


# print("headhunting",file=hourlies)

# 用close方法输出后关闭


# hourlies.close()


# 2.反义字符
# 反斜杠: \\
# 单引号: \'
# 双引号: \"
# 换行: \n
# 回的: \r
# 水平制表符: \t  一组四个字符的位置 如果填满了就会离下一个出现4个字符的空位置  如果没有填满剩余几个就是空几个字符的位置 然后显示下一个
# 退格: \b
# r后者R 显示原本的样子  注意结尾的时候不能是一个反斜杠\
# print(r"he\shunning")


# 3.变量赋值
# 变量有三部分组成 1.id 2.type 3.value
nam = '何风顺'
# 直接获取Value
# print(nam)
# 获取id
# print("标识",id(nam))
# 获取Type
# print("类型",type(nam))
