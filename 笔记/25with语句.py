# with语句（上下文管理器）
# 不论什么原因跳出with块都能确保关闭文件  达到释放资源的目的
with open( "D:/text.txt" , "r" ) as file :  # as 后面是别名 相当于给了一个变量
    print( file.read( ) )
# 这样写就不用手动关闭
