lista=[[1],[2,2,2],[3],[8,8,8],[9],[10]]

def function2(lista):
    nuevalista=[]
    for i in range(len(lista)):
        for l in lista[i]:
            nuevalista.append(l)
    return nuevalista
    
print(function2(lista))