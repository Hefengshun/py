# 集合的创建{}  集合中的元素不允许重复  (可变序列)
# 是没有value值得
t = { 1 , 23 , 4 }

# 使用内置函数set( )
s = set( range( 6 ) )
print( s )
# 也可以列表转集合  （可以去重）
# s = set( [ 1 , 2 , 3 , 4 , 5 , 6 , 32 , 2 , 1 ] )
# print( s )      #{32, 1, 2, 3, 4, 5, 6}  去重复了  因为哈希值的缘故重新排列了
# 字符串的转
# s = set( "hefengshun" )
# print( s )      #{'f', 'n', 'e', 'h', 's', 'g', 'u'}


# 定义空集合
# s={}  #type为字典（dict）不可以这样使用
# ** ** **
# s = set( )  只可以这样定义


# 集合的关系
# issubset()   A.issubset(B)   判断一个集合是否是另一个集合的子集
# issupset() 判断一个集合是否是另一个集合的超集
# isdisjoint() 判断两个结合是否有交集
# intersection()  与  &  等价        找出集合的交集
# union() 与 | 等价     集合的并集
# difference()  与 - 等价   A.difference(B)  意思是把相等的先去掉，A剩下的元素
# symmetric_difference()  与^ 等价      意思是相同的去掉之后，组成一个新的集合


# 集合的生成式
# { 表达式 for i in range( 1 , 10 ) }  集合生成式
# [ 表达式 for i in range( 1 , 10 ) ]  列表生成式
