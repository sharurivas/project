def maxIndex(list):
    maximo=max(list)
    for i in range(len(list)):
        if list[i]==maximo:
            return i

def function8(lista):
    listavacia=[0]*(max(lista)+1)
    for x in lista:
        listavacia[x]+=1
    return maxIndex(listavacia)
    

print(function8([1,2,3,3,3,3,3,3,3,3,4,4,4,4,5,5,5,5,6]))