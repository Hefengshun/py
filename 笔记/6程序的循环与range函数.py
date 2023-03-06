# range是一个迭代器 具有三个参数
# 参数1个时  参数为x时 就带表从0开始 每次加一步 加到x  用list（）打印变量可以看到数组
# 参数2个时  第一个参数代表开头  第二个代表结束 也是每次加一步
# 参数3个时  第三个参数则代表  每次加的步数是几


# p = range( 10 )     #这里代表从0开始到9的10个数字
# print( p )                #range(0, 10)
# print( list( p ) )        #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 两位参数时
# p = range( 2 , 10 )
# print( p )   #range(2, 10)
# print( list( p ) )         # [2, 3, 4, 5, 6, 7, 8, 9]


# 三位参数时
# p = range( 2 , 10 , 2 )
# print( p )                   #range(2, 10, 2)
# print( list( p ) )           #[2, 4, 6, 8]


# while循环语句  while是判断n+1次 条件为ture时执行n次
# a = 1
# b = 0
# while a < 4 :
#     print( a )
#     b += a
#     a += 1
# 一定要改变a之前就加给b 不然就是不对的
# print( b )


# for in 循环
# for i in "hefengshun" :   #输出字符串
#     print( i )    #结果为一行一个字母  到结束
# for i in range( 1 , 101 , 4 ) :            #输出迭代对象
#    print( i )   #依次输出list


# 如果 只想循环5次 又用到变量就可以不用声明变量 用_带替
# for _ in range( 5 ) :
# print( "何风顺" )   #结果为打印5次名字
