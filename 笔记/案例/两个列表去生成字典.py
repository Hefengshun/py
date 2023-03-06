lts1 = [ 1 , 2 , 3 ]
lts2 = [ "哈士奇" , "旺财" , "柴犬" ]
p = { key.upper( ) : value for key , value in zip( lts2 , lts1 ) }
print( p )
