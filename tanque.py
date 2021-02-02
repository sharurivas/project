def function5(k,l,r,t,x,y):
    a=k
    for i in range(t):
        a=a-x+y 
        if l<a<r:
            continue
        else: 
            return 0
    return 1   

print(function5(50, 30, 70, 19, 1, 2))