# def update(string,number,len):
#   if(number < len):
#    for i in range(len):
#      if(i<number):
#        continue
#      else:
#        print(string[i]) 
 
# str=input('enter the string')
# num=int(input('enter the number of character to be removed'))
# len=len(str)

# update(str,num,len)


##############################################################
def update(string,number):
    x=string[number: ]
    print(x)


str=input('enter the string')
num=int(input('enter the number of character to be removed'))
len=len(str)

if(num < len):
    update(str,num)
