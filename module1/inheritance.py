class Mammal:
     
     def __init__(self,name):
         self.name=name


     def walk(self):
        print(f"{self.name} is walking")



class Dog(Mammal):  # using parenthesis and adding the class name which we want to inherit 
   pass             # if we dont want to add any methods/function in the class we can write pass it doesnt mean anything 



class cat(Mammal):
    pass


dog1=Dog("leo")

dog1.walk()


cat1=cat("bandar")

cat1.walk()

