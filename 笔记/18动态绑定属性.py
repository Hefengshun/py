class Student :
    def __init__( self , name , age ) :
        self.name = name
        self.age = age

    def ect( self ) :
        print( self.name , "吃了早饭" )


a = Student( "张三" , 18 )
a.ect( )
a.name2 = "王五"
print( a.name2 )  # 动态绑定了一个属性


# 写出一个函数 绑定到类上之后就是一个方法了
def show( ) :
    print( "定义一个函数" )


a.show = show  # a.show是绑定到类上的属性  后面的show则是上面的函数
a.show( )  # 现在这个函数就是类的一个方法
