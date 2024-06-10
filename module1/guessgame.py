
secret_number=12
i=0
while i<3:
    guess_num=int(input('guess'))
    i=i+1
    if secret_number == guess_num:
        print('you won ')
        break
else:
    print('you lost')