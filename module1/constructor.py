class Point:
    def __init__(self,x,y):
          self.x=x
          self.y=y

    def draw(self):
          print("drawing")
    def write(self):
          print("wreiting")


point1=Point(10,20)

print(point1.x)
print(point1.y)

point2=Point(12,56)
point2.draw()

