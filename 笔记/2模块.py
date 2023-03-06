# 数据类型
#  分别有 int bool str float

# n1=1.1
# n2=2.2
# print(n1+n2)
# from decimal import Decimal
# print(Decimal("1.1")+Decimal("2.2"))


# bool 里有true（1） false（0） 是可以转成整数计算的
# 也可以用True+1  结果为二
# print(True+1)


# str类型可以用(" str ")  (' str ')  (""" str """) (''' str ''')
# 用三双引号 三（单/双）引号时可以在代码编写的地方起到换行效果 代码什么样子输出就什么样子 列：
# str3 = """何
# 风顺"""
# print(str3)
# let = open("D:/text.txt", "a+")
# print(str3, file=let)


name = "何风顺"
age = 18
# print(name + age)
# 这样相加是报错的 需要转型相加
# print(name + str(age)) 这样是可以的


# str转int是报错的 因为字符串为小数串
