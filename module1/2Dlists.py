list=[2,2,4,6,7,4,8,1]
uniques=[]
for number in list:
    if number not in uniques:
        uniques.append(number)
print(uniques)