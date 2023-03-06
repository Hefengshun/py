# lst = [ "1" , "2" , "ho" , 7 ]
# print( lst.index( "ho" ) )  #可以获取索引  ： 正向索引为0开始 负向从n到-1：如果有出个只返回找到的第一个
# print( lst.index( "ho" , 1 , 2 ) )  #在指定的范围查找
# 也可以这样创建
# list( [ "1" , "2" , "ho" , 7 ] )


# 列表的操作
# 列表名[start:stop:step]  #切片出来的数组是一个新的数组
# lst = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]
# print( lst[ 1 :4 :1 ] )  #start开始的地方  stop结束的地方(不包括自己)  step代表步长

# 当step为负数时
# lst = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]
# print( lst[ : :-1 ] )    #先将列表反转 依次输出
# print( lst[ 7 : :-1 ] )     #当然这里的 start 与 stop也将反过来


# 列表中的append extend insert 切片
# lst = [ 1 , 2 , 3 , 4 , ]
# lst2 = [ 5 , 6 ]
# lst.append( 100 )   #向末尾增加  添加之后就是一个新数组
# lst.append( lst2 )          #[1, 2, 3, 4, [5, 6]]
# lst.extend( lst2 )              #[1, 2, 3, 4, 5, 6]
# lst.insert( 1 , 20 )        #在lst索引为1的后面插入20   [1, 20, 2, 3, 4]
# lst[ 1 : : ] = lst2           #从索引为1的开始切到最后  切掉之后把 lst2 填上去
# print( lst )


# 列表中的删除元素
# lst = [ 1 , 2 , 3 , 4 , 2 ]
# lst2 = [ 5 , 6 ]
# lst.remove( 2 )         #[1, 3, 4, 2]  移除一个原素  只删除第一个
# lst.pop( 1 )              #[1, 3, 4, 2]  根据索引移除原素
# lst[ 1 :3 ] = [ ]           #[1, 4, 2]  应为切片会返回一个新的列表 切完之后给个空返回的就是切剩下的就不会新数组
# lst.clear( )               # []  清除列表
# del lst                      #  把列表删除
# print( lst )


# 列表的修改
# lst = [ 1 , 2 , 3 , 4 , 2 ]
# lst[ 2 ] = 100      #[1, 2, 100, 4, 2] 修改
# lst[ 1 :2 ] = [ 100 , 200 , 300 , 400 ]  #把索引1开始到2（不包括2）的位置修改了一下  切掉又补上了
# print( lst )


# 列表的排序  sort()方法       与  sorted内置函数
# lst = [ 1 , 5 , 3 , 8 , 2 ]
# lst.sort( )      #[1, 2, 3, 5, 8]   默认升序  在原列表上修改的
# lst.sort( reverse=True )        #[8, 5, 3, 2, 1]  降序排列
# lst2 = sorted( lst )            #[1, 2, 3, 5, 8] 会产生一个新的列表     lst传进去 lst2 接收
# lst2 = sorted( lst , reverse=True ) #[8, 5, 3, 2, 1]   把reverse=True 也传进去
# print( lst2 )


# 列表生生成式  [ i * i for i in range( 1 , 10 ) ]
# for前面为列表表达式  后面则是循环生成1到9
# lst = [ i for i in range( 1 , 10 ) ]
# print( lst )    #[1, 2, 3, 4, 5, 6, 7, 8, 9] 生成列表
# lst = [ i * i for i in range( 1 , 10 ) ]
# print( lst )        #[1, 4, 9, 16, 25, 36, 49, 64, 81]
