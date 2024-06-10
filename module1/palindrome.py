number=int(input('enter the number to be checked'))
num=number
ans=0
while(number > 0):
    r=number % 10
    ans=ans*10+r
    number=number //10
if(num == ans):
    print('palindrome')
else:
    print('not a palindrome')