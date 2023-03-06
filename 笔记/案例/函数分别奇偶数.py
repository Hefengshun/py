odd = [ ]
even = [ ]


def fun( num ) :
    for i in num :
        if (i % 2 == 0) :
            odd.append( i )
        else :
            even.append( i )
    print( odd )
    print( even )  # 如果odd even写在里面外面是找不到  可以写外面return出去
    return odd , even


fun( [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ] )
print( odd )
print( even )


# 二
def show( num ) :
    a = [ ]
    b = [ ]
    for i in num :
        if (i % 2 == 0) :
            a.append( i )
        else :
            b.append( i )
    return a , b  # 这里return出的是两个列表


c = [ 123 , 321 , 123 , 2213 , 123 , 12 , 32 , 12 , ]
print( show( c ) )  # ([12, 32, 12], [123, 321, 123, 2213, 123])  输出为一个元组里两个列表
