p = int( input( "请输入消费金额" ) )
s = input( "您是会员吗：y/n" )
if s == "y" :
    if 100 < p < 200 :
        print( "给您打9折，请支付：" + str( int( p * 0.9 ) ) )
    elif 200 < p < 300 :
        print( "给您打8折，请支付：" + str( int( p * 0.8 ) ) )
    elif 300 < p < 400 :
        print( "给您打7折，请支付：" + str( int( p * 0.7 ) ) )
else :
    print( "您好，您一共消费：" + str( p ) + "元" )
