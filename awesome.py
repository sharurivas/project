def awesome(list):
    count=0
    for i in range(1, len(list)-1):
        if list[i-1]%2==0 and list[i]%list[i+1]==0:
            count+=1
    return count


print(awesome([800,400,200,100,50,25,5,1]))
