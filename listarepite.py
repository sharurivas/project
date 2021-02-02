def function7(lista):
    listavacia=[0]*(max(lista)+1)
    for x in lista:
        if listavacia[x]==1:
            return x   
        listavacia[x]=1


print(function7([1,2,3,4,6,7,3]))
        