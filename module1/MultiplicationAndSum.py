# a=int(input('enter the first number'))
# b=int(input('enter the second number'))

# c=a*b;
# if(c < 1000):
#     print(c)
# else:
#     print(a+b)

#########################################

def multiply_sum(num1,num2):
    
    num3=num1*num2
    if num3 <=1000:
        return num3
    else:
        return num1+num2
    
a=int(input('enter the first number'))
b=int(input('enter the second number'))

result=multiply_sum(a,b)
print("the result is", result)

