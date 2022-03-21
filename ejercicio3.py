lista= []
lista= [1,2,2,4,5,6,7,7,7,8,9,10,1]

def function(lista):
    listafinal=[[]]
    for i in range(len(lista)):
        if lista[i]!=lista[i-1] and i>0:
            listafinal.append([lista[i]])
        else:
            listafinal[-1].append(lista[i])

    return listafinal
print(function(lista))
