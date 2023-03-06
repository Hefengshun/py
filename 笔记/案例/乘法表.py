for hang in range( 1 , 10 ) :
    for item in range( 1 , hang + 1 ) :
        print( item , "*" , hang , "=" , int( hang * item ) , end="\t" )
    print( end="\n" )
