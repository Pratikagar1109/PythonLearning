n=int(input('enter the number of elements in the list'))
lst=[]
print('enter the elements in the list')
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
   
first_num=lst[0]
last_num=lst[n-1]

if first_num == last_num:
    print('true')
else:
    print('false')