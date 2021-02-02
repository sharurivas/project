def repetead(list1,list2):
    newlist=[]
    conj={}
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                newlist.append(list2[j])
    conj=set(newlist)
    listafinal=list(conj)
    return listafinal


print(repetead([1,2,2,2,4],[5,5,5,2]))