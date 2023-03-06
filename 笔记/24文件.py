# 内置函数open()创建文件对象
# 被创建的文件名 = 创建文件的函数 （要创建文件或打开文件的名称  [ 打开模式默认只读，默认编码格式  ] ）
# 常用的文件打开模式
# r为读
# file = open( "D:/text.txt" , "r" )
# print( file.readlines( ) )
# file.close( )


# w为写
# 如果文件有那么就把原又内容替换掉  没有则创建
# file = open( "D:/text.txt" , "w" )
# file.write( "哈士奇" )
# file.close( )


# a为追加  没有文件则创建  有则往后面追加
# file = open( "D:/text.txt" , "a" )
# file.write( "哈士奇" )
# file.close( )

# b  以二进制打开文件 不能单独使用  需要与其它一起使用 比如 rb ， wb
# 拷贝
file = open( "D:/text.txt" , "rb" )  # 先用二进制读取
file2 = open( "D:/text2.txt" , "wb" )  # 在创建text2  并与下一行代码写进去
file2.write( file.read( ) )  # 把rb读出的内容 写到file2里 也就是text2里
file.close( )
file2.close( )

# +表示以读写方式打开  不能单独使用  a+ .....


# 文件对象的一些常用方法
# read( number )
# 读取number个字节或字符内容返回  不写 则读全部
# readline()
# 读取文件一行的内容
# readlines( )
# 读取多行内容
# write()
# 将srt写入文件
# writelines()
# 将字符串列表写进去  不添加换行符
# seek(offset[whence])
# offset 问方向  规定正负   whence不同的值代表不同 0默认 开头计算 1:当前位置开始计算  2:文件尾开始计算
# tell()
# 返回当前指针的位置
# flush()
# 把缓冲区的内容写入文件  不关闭文件
# close()
# 关闭文件


# walk()方法
# walk()  可以遍历指定目录下的所有文件 以及目录  类似递归
# 详细用法见案例
