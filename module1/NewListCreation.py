list1=[]
list2=[]
n1=int(input('enter the number of elemets in the first list'))
print('enter the values in the first list')
for i in range(0,n1):
    num1=int(input())
    list1.append(num1)

n2=int(input('enter the number of elemets in the second list'))
print('enter the values in the second list')
for i in range(0,n2):
    num2=int(input())
    list2.append(num2)

resultlist=[]
for  i in range(0,n1):
    if(list1[i] % 2 != 0):
        resultlist.append(list1[i])

for  i in range(0,n2):
    if(list2[i] % 2 == 0):
        resultlist.append(list2[i])


n3= len(resultlist)
for  i in range(0,n3):
        print(resultlist[i] ,end=" ")


