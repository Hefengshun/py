class Cpu :
    pass


class Disk :
    pass


class Computer :
    def __init__( self , cpu , disk ) :
        self.cpu = cpu
        self.disk = disk


# 变量的赋值

cpu1 = Cpu( )
cpu2 = cpu1
print( cpu1 , cpu2 )  # 内存地址是相同的的

# 类对象的浅拷贝
disk = Disk( )  # 创建一个硬盘类的对象
Computer = Computer( cpu1 , disk )  # 创建一个计算机类的对象

# 浅拷贝  拷贝时 对象的子对象内容不拷贝  因此源对象的与拷贝对象会用一个子对象    子对象就一个占用了一个空间
import copy

Computer2 = copy.copy( Computer )
print( Computer , Computer.cpu , Computer.disk )
print( Computer2 , Computer2.cpu , Computer2.disk )

# 深拷贝   拷贝时  对象的子对象也进行拷贝  子对象的地址就不一样  相当于生成了两个  分别占用了空间
Computer3 = copy.deepcopy( Computer )
print( Computer , Computer.cpu , Computer.disk )
print( Computer3 , Computer3.cpu , Computer3.disk )
