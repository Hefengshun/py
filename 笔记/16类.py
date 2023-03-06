class Studet :
    home = "河南"

    def __init__( self , name , age ) :
        self.name = name  # self.name 称为实例属性 ，进行了一个赋值，将局部变量的name的值赋给了实例属性
        self.age = age
        print( "我使用__init__修饰,所以我是初始化方法" )

    # 实例方法
    def show( self ) :  # 实例方法本身就有一个默认参数self
        print( "学生在吃饭" )

    @staticmethod
    def metnod( ) :  # 没有任何参数
        print( "我使用staticmethod修饰,定义了静态方法" )

    @classmethod
    def cm( cls ) :  # 类方法本身就有一个默认参数cls
        print( "我使用classmethod修饰,定义了类方法" )


def sh( ) :
    print( "我写在外面，所以我是一个函数" )


# 类属性的使用
print( Studet.home )  # 河南

# 类方法的的使用
Studet.cm( )  # 我使用classmethod修饰,定义了类方法

# 静态方法的使用
Studet.metnod( )  # 我使用staticmethod修饰,定义了静态方法  （没有任何参数）
