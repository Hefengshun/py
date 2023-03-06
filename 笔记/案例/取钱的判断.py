money = 1000
s1 = int( input( "请输入取的钱数" ) )
if s1 <= money :
    money = money - s1
    print( "取款成功余额为:" , money )
else :
    print( "余额不足，剩余钱数为：" , money )
