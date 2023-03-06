# 导入 异常  这些东西用到后续当中可以把异常存入到错误日志中
import traceback

try :
    print( 10 / 0 )
except :
    traceback.print_exc( )
    # traceback.print_exc( )  这里就是报出异常的东西
