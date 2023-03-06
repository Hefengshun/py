# 封装
# class Student :
#     def __init__( self , name , age ) :
#         self.name = name
#         self.__age = age  # 前面加上下划线就不能在类的外面使用  实现了一个封装  方法也是一样的
#
#     def show( self ) :
#         print( self.name , self.__age )
#
#
# a = Student( "张三" , 18 )
# a.show( )
# # print( a.age )  # Student' object has no attribute 'age'  已经报错了
# print( a._Student__age )  # 18  这种写法是可以访问的_Student__age


# 继承
# class 子类类名(父类1，父类2....):


# class Por :
#     def __init__( self , name , age ) :
#         self.name = name
#         self.age = age
#
#     def show( self ) :
#         print( self.name , self.age )  # 但是在这里xuehao就不能输出了 可以进行方法的重写  让Studet里有一个show()
#
#
# class Studet( Por ) :
#     def __init__( self , name , age , xuehao ) :
#         super( ).__init__( name , age )
#         self.xuehao = xuehao
#
#     def show( self ) :  # 这里就实现了重写
#         super( ).show( )  # 用super方法调用了Por里面的show方法然后再打印xuehao
#         print( self.xuehao )
#
#
# stu = Studet( "张三" , 18 , 101 )
# stu.show( )  # 此时Student就继承了Por里面的show方法 张三 18


# object类 是所有类的父类  内置函数dir()可以查看指定对象所有属性
class Por :
    def __init__( self , name , age ) :
        self.name = name
        self.age = age

    def show( self ) :
        print( self.name , self.age )  # 但是在这里xuehao就不能输出了 可以进行方法的重写  让Studet里有一个show()

    def __str__( self ) :  # __str__这个方法
        return '我的名字是{0}，我今年{1}岁了'.format( self.name , self.age )
        # format  插值


print( dir( Por ) )  # 这样就看见了  有很多都是继承object的

a = Por( "张三" , 18 )
print( a )  # 我的名字是张三，我今年18岁了  这里就调用了 __str__这个方法


# 多态


class Animal( object ) :
    def eat( self ) :
        print( "动物会吃" )


class Dog( Animal ) :
    def eat( self ) :
        print( "够吃骨头" )


class Cat( Animal ) :
    def eat( self ) :
        print( "猫吃鱼" )


class Por :
    def eat( self ) :
        print( "人吃五谷茶凉" )


# 定义一个函数
def fun( obj ) :
    obj.eat( )


# 开始调用函数
fun( Dog( ) )  # 够吃骨头
fun( Cat( ) )  # 猫吃鱼
fun( Animal( ) )  # 动物会吃
print( "----------------------" )
fun( Por( ) )  # 人吃五谷茶凉  # 它没有继承Animal但是也可以用
# py是一门动态语言  它只关心里面是否有这个方法  有就可以  所以上面分别把自己的类传到函数里调用了eat方法
