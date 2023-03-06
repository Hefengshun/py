# 6!
# def fac( n ) :
#     if n == 1 :
#         return 1
#     else :
#         return n * fac( n - 1 )
#
#
# print( fac( 6 ) )  # 720


# 斐波那契数列
def f( n ) :
    if n == 1 :
        return 1
    elif n == 2 :
        return 1
    else :
        return f( n - 1 ) + f( n - 2 )


print( f( 6 ) )  # 8

# 输出前6项的
for i in range( 1 , 7 ) :
    print( f( i ) )  # 1 2 3 5 8
