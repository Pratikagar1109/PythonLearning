n=int(input('enter the number of elements in the list'))
lst=[]
print('enter the elements in the list')
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
for i in range(0,n):
    if (lst[i] % 5 == 0):
        print(lst[i])