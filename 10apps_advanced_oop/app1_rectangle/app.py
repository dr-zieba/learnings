from random import randint

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

a = Point(randint(0,9),randint(0,9))
c = Point(randint(10,19),randint(10,19))


rectangle = Rectangle(a,c)

print(f"Coordinates: \n{rectangle.lowleft.x} \n{rectangle.lowleft.y} \n{rectangle.upright.x} \n{rectangle.upright.y}")

user_point = Point(float(input("Type x: ")), float(input("Type y: ")))

print(f"Your points: x= {user_point.x} y= {user_point.y}")

print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))