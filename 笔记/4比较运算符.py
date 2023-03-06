# 比较运算符里 is （is not)比较的是id
# 而==则比较的是value
# ls1 = [ 1 , 23 , 4 , ]
# ls2 = [ 1 , 23 , 4 , ]
# print( ls1 is ls2 )  #flass
# print( ls1 is not ls2 ) #true
# print( ls1 == ls2 )  #true


a , b = 1 , 2
# print( a == 1 and b == 2 ) # true
# print( a == 1 and b < 2 ) #false 有一项为false  直接判定为false


# or 或者
# print( a == 1 or b == 2 ) true
# print( a == 1 or b < 2 ) true
# print( a != 1 or b == 2 ) true  有一项为true  直接判定为true
# print( a != 1 or b != 2 ) false


# not 对bool类型取反
f = True
f1 = False
# print( not f ) false
# print( not f1 ) true


# in 在什么什么里
p = "hefengshun"
# print( "he" in p ) ture
# not in 不在什么什么里
# print( "he" in p ) false
