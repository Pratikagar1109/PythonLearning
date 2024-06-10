number=int(input('enter the number'))

while( number > 0):
    r=int(number % 10)
    print(r ,end=" ")
    number=int(number/10)