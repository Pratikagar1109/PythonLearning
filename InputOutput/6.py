with open("test.txt","r") as fp:
    lines=fp.readlines()

with open("newtest.txt","w") as fp:
    count=0
    for line in lines:
        if count == 4:
            count=count+1
            continue
        else:
            fp.write(line)
            count=count+1