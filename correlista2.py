

def function(lista,numero):
    y=0
    for x in lista:
        if x==numero:
            y = y+1
    return y

print(function([1,2,3,4,4,4,5,6,4],4))
