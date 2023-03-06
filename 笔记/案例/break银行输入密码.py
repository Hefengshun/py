# a = 0
# while a < 3 :
#     p = input( "请输入密码" )
#     if p == "123456" :
#         input( "请输入金额" )
#         break
#     else :
#         a += 1
#         print( "还剩余：" , 3 - a , "次机会" )

# while 与 eles使用
a = 0
while a < 3 :
    p = input( "请输入密码" )
    if p == "123456" :
        input( "请输入金额" )
        break
    else :
        a += 1
        print( "还剩余：" , 3 - a , "次机会" )
else :
    print( "输入全部错误" )

# 二  for in
# for a in range( 3 ) :
#     p = input( "请输入密码" )
#     if p == "123456" :
#         input( "请输入金额" )
#         break
#     else :
#         print( "还剩余：" , 2 - a , "次机会" )

# for 与 eles使用
# for a in range( 3 ) :
#     p = input( "请输入密码" )
#     if p == "123456" :
#         input( "请输入金额" )
#         break
#     else :
#         print( "还剩余：" , 2 - a , "次机会" )
# else :
#     print( "输入全部错误" )
