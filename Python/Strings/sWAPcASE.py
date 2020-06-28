def swap_case(s):
    
    k=''
    
    for i in s:
        x = ord(i)
        
        if x>=97 and x<=122:
            y=x-32
            k+=chr(y)
        elif x>=65 and x<=90:
            y=x+32
            k+=chr(y)
        else:
            k+=chr(x)        
    
    return k
