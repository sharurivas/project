lista1=[1,2,3,6,7,8,9,10]
lista2=[1,2,3,4,5,6,7,8,9,10]

def function3(lista1,lista2):
    nuevalista=[]
    for i in range(len(lista2)):
        for l in range(len(lista1)):
            if lista2[i]==lista1[l]:
                nuevalista.append(1)
                break
            else:
                if lista1[l]==lista1[-1]: nuevalista.append(0)
    
    return nuevalista

print(function3(lista1,lista2))
