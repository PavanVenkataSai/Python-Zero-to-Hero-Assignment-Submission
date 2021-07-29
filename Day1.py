li = [int(i) for i in input("Enter values : ").split()]
#Method - 1
for j in range(len(li)):
    for i in range(j+1,len(li)):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
print(li)



#Method - 2
#By using a sorted built in function.
li = [int(i) for i in input("Enter values : ").split()]
print(sorted(li,reverse=True))
