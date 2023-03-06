# 字典是py数据结构之一  （与js对象差不多）
# 与 列表一样是可变序列（可变序列就是可以增删改查）
# 与键值对的方式储存变量
# 字典名 = { "键" : 值 , "键" : 值 , "键" : 值 , }


# 字典的创建
# 1.使用花括号创建
# dog = { "哈士奇" : "8岁了" , "柴犬" : "6岁了" }
# print( dog )        #{'哈士奇': '8岁了', '柴犬': '6岁了'}
# 2.用内置函数dict( )创建
# dd = dict( name="哈士奇" , name2="柴犬" )
# print( dd )         #{'name': '哈士奇', 'name2': '柴犬'}


# 字典中元素的获取
# 1.使用[]  2.使用get()方法
# dog = { "哈士奇" : "8岁了" , "柴犬" : "6岁了" }
# print( dog[ "哈士奇" ] )       #8岁了
# print( dog[ "哈士" ] )        #KeyError: '哈士'  没有时会报错 keyError说没有这个键
# print( dog.get( "哈士奇" ) )       #8岁了
# print( dog.get( "哈士" ) )      # None  没有时  打印出 nono 没找到  （不报错）
# print( dog.get( "哈士" , 100 ) )  #100 现在的none 改成了100  意思是当键对应的值不存在时，会提供一个值（100是自己定义的）


# 字典的判断以及修改
# dog = { "哈士奇" : "8岁了" , "柴犬" : "6岁了" }
# print( "哈士奇" in dog )  #True
# 删除指定的键值对
# del dog[ "哈士奇" ]
# print( dog )        #{'柴犬': '6岁了'}
# 清空 clear()
# dog.clear( )
# print( dog )        #{}  清空
# 添加
# dog[ "旺财" ] = "4岁了"
# print( dog )    #{'哈士奇': '8岁了', '柴犬': '6岁了', '旺财': '4岁了'}
# 修改元素的值
# dog[ "旺财" ] = "4岁了"   #开始添加
# dog[ "旺财" ] = "6岁了"   #现在修改
# print( dog )   #{'哈士奇': '8岁了', '柴犬': '6岁了', '旺财': '6岁了'}


# 字典的三个方法  keys()  values() itrms()
# dog = { "哈士奇" : "8岁了" , "柴犬" : "6岁了" }
# print( dog.keys( ) )    #dict_keys(['哈士奇', '柴犬'])
# print( dog.values( ) )  #dict_values(['8岁了', '6岁了'])
# print( dog.items( ) )   #dict_items([('哈士奇', '8岁了'), ('柴犬', '6岁了')])
# 可以将其转换成列表
# dog = { "哈士奇" : "8岁了" , "柴犬" : "6岁了" }
# item = dog.keys( )
# print( list( item ) )  #['哈士奇', '柴犬']


# 字典的遍历
# dog = { "哈士奇" : "8岁了" , "柴犬" : "6岁了" }
# 这里的item代表每一个keys
# 原理也是根据每个keys来获取对应的values
# for item in dog :
#     print( item , dog[ item ] , dog.get( item ) )


# 字典的生成式
# upper() 内置函数可以全部转换成大写
# zip(key,value)    zip()内置函数 打包成一个元组
# { key.upper():value  for key,value in  zip(数组1,数组2)}
