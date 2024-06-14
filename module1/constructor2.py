class Person:
    def __init__(self,name):
        self.name=name
    
    def talk(self):
        print(f"{self.name} is talking")

person1=Person("Pratik")

person1.name="Shakshi"
person1.talk()
