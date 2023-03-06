# （字符串，元组） 不可变序列  可以切片
t = "hello"
# print( t.index( "l" ) )       # 2      第一次出现的位置  不存在 -1
# print( t.find( "l" ) )        # 2      第一次出现的位置   找不到报错
# print( t.rindex( "l" ) )      # 3     最后一次的出现的位置   找不到报错
# print( t.rfind( "l" ) )       # 3     最后一次的出现的位置  不存在 -1


# 大小写的转换
# print( t.upper( ) )           #HELLO     全大写       产生新的
# print( t.lower( ) )           #hello    全小写        产生新的
# print( t.swapcase( ) )        #HELLO    小写转大写 大写转小写
# print( t.capitalize( ) )      #Hello   第一个大写其余小写
# print( t.title( ) )           #Hello   每个单词的第一个转大写 其余小写


# 内容对齐操作
# print( t.center( 20 , "*" ) )       #居中  第一个代表宽度  第二个填充内容
# print( t.ljust( 10 , "*" ) )        #左对齐
# print( t.rjust( 10 , "*" ) )        #右对齐
# print( t.zfill( 10 ) )              #右对齐 此方法只接收一个参数 （长度）左边用0填充


# 字符串的分割
# t = "dawda,weewar,erttr,weqe"
# 左边开始
# print( t.split( "," ) )                       #['dawda', 'weewar', 'erttr', 'weqe']
# print( t.split( "," , maxsplit=1 ) )          # ['dawda', 'weewar,erttr,weqe']
# 右边开始
# print( t.rsplit( "," ) )                      # ['dawda', 'weewar', 'erttr', 'weqe']
# print( t.rsplit( "," , maxsplit=1 ) )         # ['dawda,weewar,erttr', 'weqe']


# 判断字符串的一些方法
# t = "dawdaweewarerttrweqe"
# print( t.isidentifier( ) )       # 判断字符串是不是合法标识符
# print( t.isspace( ) )            # 判断字符串是否全部由空字符组成（回车，换行，水平字符表）
# print( t.isalpha( ) )            # 判断字符串全部为字母
# print( t.isnumeric( ) )          # 判断字符串全部为数字
# print( t.isalnum( ) )            # 判断字符串全部由数字字母组成
# print( t.isdecimal( ) )          # 判断是否由10进制的数组组成


# 字符串的替换
s = "哈士奇"
# print( s.replace( "士" , "土" ,2) )   #  哈土奇  第一个参数找到 第二个替换内容 第三个参数是替换次数（我们这里只有一个士所以只替换了一次）
s = [ "哈" , "士" , "奇" ]
# print( "".join( s ) )                 # 哈士奇   用于连接  前面空字符串用于连接
# print( "|".join( s ) )                # 哈|士|奇
# print( "|".join( "hfs" ) )            #h|f|s  先变成字符串序列 在连接


# 字符串的切片
# s = "hahaha"
# s1 = s[ :5 ]
# print( s1 )           #hahah


# 格式化字符串
# %s 字符串          %i或者%d 整数           %f浮点数
name = "哈士奇"
age = 6
# 第一种写法
# print( "%s今年%i岁了" % (name , age) )                #哈士奇今年6岁了
# 第二种写法 {}
# print( "{0}今年{1}岁了".format( name , age ) )        # 哈士奇今年6岁了  注意是点出的
# 第三种写法
# print( f"{name}今年{age}岁了" )                       #哈士奇今年6岁了      注意前面写一个f


# print( "%10d" % 99 )                  #%10d 这里的10代表了宽度
# print( "%.3f" % 3.1415926 )           # %.3f 表示显示3位小数
# print( "%10.3f" % 3.1415926 )         #%10.3f 总宽度为10 小数点为3位


# print( "{0:.3}".format( 3.1415926 ) )         #{0:.3}表示一共显示3位数
# print( "{0:.3f}".format( 3.1415926 ) )        #{0:.3f} 表示3位小数
# print( "{0:10.3f}".format( 3.1415926 ) )      #在原有的基础上增加了  长度总10


# 字符串的编码与解码
# 编码    encode( encoding="GBK" )
# s = "哈士奇"
# print( s.encode( encoding="GBK" ) )       # 在GBK一个中文占两个字节  b'\xb9\xfe\xca\xbf\xc6\xe6'  前面的b表示二进制
# print( s.encode( encoding="UTF-8" ) )     # 一个中文占三个字节

# 解码
# s = "哈士奇"
# s1 = s.encode( encoding="GBK" )
# print( s1.decode( encoding="GBk" ) )        # 哈士奇
