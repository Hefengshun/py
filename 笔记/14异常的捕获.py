# try :
#     n1 = int( input( "请输入第一个数字" ) )
#     n2 = int( input( "请输入第二个数字" ) )
#     result = n1 / n2
#     print( result )
# except ZeroDivisionError :
#     print( "不能除以0" )
# except ValueError :
#     print( "只能输入数字" )
# print( "程序结束" )

# 二               出现异常执行except  未出现执行 else
# try :
#     n1 = int( input( "请输入第一个数字" ) )
#     n2 = int( input( "请输入第二个数字" ) )
#     result = n1 / n2
# except BaseException as e :
#     print( "出错了" )
#     print( e )
# else :
#     print( "结果为" , result )

# 三

try :
    n1 = int( input( "请输入第一个数字" ) )
    n2 = int( input( "请输入第二个数字" ) )
    result = n1 / n2
except BaseException as e :
    print( "出错了" )
    print( e )
else :
    print( "结果为" , result )
finally :  # 不管是否异常都执行
    print( "执行结束" )
