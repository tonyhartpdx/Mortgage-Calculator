(a,b,c) = 1,1,1
solved = False

while True:
# a block    
    pass
    
    while True:
    # b block    
        pass
        
        # c block
        c = (1000 - (a + b))
        if (a**2 + b**2 == c**2):
            solved = True
            break

        else:
            b += 1
            if b > 998:
                break
    
    if solved == True: 
        break
    else:
        a += 1
        b = 1
        if a > 998: 
            break

print a,b,c
x = a*b*c
print x
