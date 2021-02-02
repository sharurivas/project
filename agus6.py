lista=[[0,1,0],[1,0,1],[1,1,1]]

def function4(lista):
    if (lista[0][0]==lista[0][1]==lista[0][2] or
            lista[1][0]==lista[1][1]==lista[1][2] or 
            lista[2][0]==lista[2][1]==lista[2][2] or
            lista[0][0]==lista[1][0]==lista[2][0] or
            lista[0][1]==lista[1][1]==lista[2][1] or
            lista[0][2]==lista[1][2]==lista[2][2] or
            lista[0][0]==lista[1][1]==lista[2][2] or
            lista[0][2]==lista[1][1]==lista[2][0]):
            print(1)
    else:
        print(0)

function4(lista)