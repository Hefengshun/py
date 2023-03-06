# 实例名=类名()
class Studet :
    home = "河南"

    def __init__( self , name , age ) :
        self.name = name  # self.name 称为实例属性 ，进行了一个赋值，将局部变量的name的值赋给了实例属性
        self.age = age
        print( "我使用__init__修饰,所以我是初始化方法" )

    # 实例方法   # 实例方法本身就有一个默认参数self
    def show( self ) :
        print( "学生在吃饭" )


# 创建Student类的对象
stu1 = Studet( "张三" , 20 )  # 这里 把参数传给了初始化方法  同时也调用了__init__实例属性
print( stu1.name , stu1.age )  # 张三 20
stu1.show( )  # 学生在吃饭  18行与19行起到的效果相同
Studet.show( stu1 )  # 这里注意 传进去的一定是Student的对象  因为实例化方法接收的参数是本身
