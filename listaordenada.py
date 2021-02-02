lista[5,6,7,3,2,0,9,1]

def function6(lista)
    for i in range(len(lista))
        if lista[i]>=lista[0]:
            lista[0]=lista[i]
        else