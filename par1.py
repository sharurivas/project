lista= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Par(lista):
    nuevaLista=[]
    listaFinal=[]
    for x in lista:
        if x%2==0:
            nuevaLista.append(x)      #elementos pares
            
    for x in range(len(nuevaLista)):     #range es para que en el for se itere en cada numero desde 0 hasta el len de nueva lista
        listaFinal.append(nuevaLista[len(nuevaLista)-1-x])   #como el primer valor de x es cero, entonces a lista final le asigno el ultiom de la nueva lista que es len-1
    return listaFinal     #return es para que me devuelva lo que quiero, no lo escribe y todo lo de dsps no ejecuta
    
        
v = Par(lista)
print(v)
