import os

path = os.getcwd( )
lis = os.walk( path )
# walk()  可以遍历指定目录下的所有文件 以及目录  类似递归
# print( lis )  # 打印一个迭代器对象  返回的是元组
for dirpath , dirname , filename in lis :
    # print( dirpath )  #路径
    # print( dirname )  #案例下的idea文件
    # print( filename ) #案例下py文件
    # print( "------------" )
    for dir in dirname :
        print( os.path.join( dirpath , dir ) )  # 案例下的idea文件
    print( "------------------------------------" )
    for dir in filename :
        print( os.path.join( dirpath , dir ) )  # 案例下的idea文件
