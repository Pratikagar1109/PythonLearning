from random import *
import os
u_pwd= input ("enter a password")
pwd=['a','b','c','d','e','f','g','h','i','j','1','2','3','4','5','6']

pw=""
while pw != u_pwd:
    pw=""
    for letter in range(len(u_pwd)):
        guess_pwd=pwd[randint(0,len(pwd) - 1 )]

        pw=str(guess_pwd)+str(pw)
        
        print(pw)
        print("cracking password.........Please waittt")
        os.system("cls")
print("your password is :",pw)