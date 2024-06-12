number=input('enter the phone number')
numbers={
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR"
}
output =" "
for c in number:
 output+= numbers.get(c,"!!") + " "

print(output)
 
             