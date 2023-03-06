# class A :
#     pass
#
#
# class B :
#     pass
#
#
# class C( A , B ) :
#     def __init__( self , name , age ) :
#         self.name = name  # 实例化属性
#         self.age = age
#
#
# x = C( "张三" , 18 )  # 实例化对象
#
# # 类的特殊属性
# print( x.__dict__ )  # {'name': '张三', 'age': 18} 实例化属性的字典
# print( C.__dict__ )  # 类对象可以看到 属性 以及方法的字典
# print( x.__class__ )  # 输出对象的类型
# print( C.__bases__ )  # 输出的是父类的元组
# print( C.__base__ )  # 输出的是第一个父类    C(A,b)里面的A
# print( C.__mro__ )  # 类的层次结构
# print( A.__subclasses__( ) )  # 输出A的子类  列表形式
#
# # 类的特殊方法
# a = 20
# b = 100
# c = a + b  # 相当于调用了__add__()方法
# d = a.__add__( b )
# print( c , d )  # 120 120
#
#
# # 两个对象的加法
# class Student :
#     def __init__( self , name ) :
#         self.name = name
#         print( self.name )
#
#     def __add__( self , other ) :
#         return self.name + other.name
#
#     def __len__( self ) :
#         return len( self.name )
#
#
# stu1 = Student( "张三" )
# stu2 = Student( "李四" )
# s = stu1 + stu2  # 这里用加法，类里面必须要定义一个__add__方法  并且return出来
# # s = stu1.__add__( stu2 )  # 与上面一样  但是类里也必须定义add
# print( s )  # 张三李四
#
# # __len__()方法
# lst = [ 1 , 23 , 323 , 21 , 3 , 21 , 3 , 23 ]
# print( len( lst ) )  # 8
# print( lst.__len__( ) )  # 8
# print( len( stu1 ) )  # 2   类里面必须要定义一个__len__方法  并且return  len()出来
#

# __new__()方法 与__init__()方法
class Person( object ) :
    def __new__( cls , *args , **kwargs ) :  # 把Person( )传到了object里  并创建了obj
        print( '__new__被调用执行了，cls的id值为{0}'.format( id( cls ) ) )
        obj = super( ).__new__( cls )
        print( '创建的id对象为{0}'.format( id( obj ) ) )
        return obj  # 这个返回给了self

    def __init__( self , name , age ) :
        print( "self的id值为{0}".format( id( self ) ) )
        # 用于对象的方法初始化使用
        self.name = name
        self.age = age
        # 这里初始化方法完成后给了p1


print( 'object这个类对象的id为：{0}'.format( id( object ) ) )
print( "Person这个类对象的id为：{0}".format( id( Person ) ) )
# 创建Person的实例对象
p1 = Person( "张三" , 20 )  # 这里它就会执行__new__方法把 Person( "张三" , 20 )传给了cls
# 然后创建一个obj对象  这个obj对象就是p1  也就是__init__里面的self
print( "p1这个实例对象的id地址为：{0}".format( id( p1 ) ) )
# 由执行结果可以看出 创建的obj对象与__init__里面的self 和 p1这个实例对象是一个
