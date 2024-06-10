print('Printing current and previous number in a range(10)')
a=0
b=0
sum=a+b
for number in range(10):
    sum=a+b
    print('current number'+' '+str(a)+' '+'previous number'+' '+str(b)+' '+'Sum:'+' '+ str(sum))
    b=a
    a=a+1

