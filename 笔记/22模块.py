# 导入模块
# import 模块名称 [as 别名]
# form 模块名称 import 函数/变量/类
# import math
#
# # 如果这个模块别的地方用了
# if __name__ == '__main__' :  # 把print( math.pi )这一句话 放到main下就不会在导入模块的程序了执行
#     print( math.pi )  # 此时这句话也只会在 运行这个程序的时候执行
#
# from math import pi  # 这里代表只导入了 math 里的pi
#
# print( math.pi )

# py中的包
# 包含__init__.py文件的目录称为包
# 使用import时 后面只能跟 包名 或者模块名

# 使用 from 可以导入包，模块，变量


# py中一些常用的内置模块
# 与py 解析器及其环境的操作
# import sys
#
# print( sys.getsizeof( 24 ) )
# print( sys.getsizeof( 25 ) )
# print( sys.getsizeof( True ) )

# 提供时间相关的函数
# import time
#
# print( time.time( ) )  # 秒
# print( time.localtime( time.time( ) ) )  # 当前时间


# os模块 与os.path模块用于对目录或文件进行操作
# import os

# os.system( "notepad.exe" )   #打开记事本
# os.system( "calc.exe" )  # 打开计算器

# 直接调用可执行文件
# 原本路径 E:\Program Files (x86)\Kingsoft\WPS Office
# 有\  要转义  换成两个\\  并且后面加上 运行的程序比如(ksolaunch.exe)
# os.startfile( "E:\\Program Files (x86)\\Kingsoft\\WPS Office\\ksolaunch.exe" )
# 这样就把wps 打开了


# os里面的方法
# getcwd()返回当前的工作目录
# listdir(path) 返回指定路径下的文件和目录信息
# lis = os.listdir( "../笔记" )
# print( lis )  # 返回笔记下面的目录信息

# os.mkdir("目录" )  创建一个目录
# os.makedirs(目录/目录/... )  创建多级目录
# os.rmdir(目录 )  删除目录
# os.removedirs( 目录/目录/...)  删除多级目录
# os.chdir( path )  设置为当前工作目录


# os.path模块
import os.path

# print( os.path.abspath( "1.py" ) )  #返回路径
# print( os.path.exists( "1.py" ) )  #判断是否存在  是一个bool值
# print( os.path.join( "E:\\" , "1.py" ) )  # 进行了一个路径拼接的操作
# print( os.path.split( "1.py" ) )  #分离出文件名 与扩展名
# print( os.path.basename( "路径" ) #提取文件名
# print( os.path.dirname("路径" )  # 提取文件路径，不包括文件名
# print( os.path.isdir( "路径" )  判断是否为路径
