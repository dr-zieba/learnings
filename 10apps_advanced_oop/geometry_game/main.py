from random import randint
import turtle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


class GuiRectangle(Rectangle):
    def draw_figure(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)


class GuiPoint(Point):
    def draw_point(self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size=5)


a = Point(randint(0, 99), randint(0, 99))
c = Point(randint(100, 199), randint(100, 199))
figure = GuiRectangle(a, c)


user_point = GuiPoint(float(input("Type x: ")), float(input("Type y: ")))
print(f"Your points: x= {user_point.x} y= {user_point.y}")

#print(f"Coordinates: \n{rectangle.point1.x} \n{rectangle.point1.y} \n{rectangle.point2.x} \n{rectangle.point2.y}")
my_turtle = turtle.Turtle()
figure.draw_figure(my_turtle)
user_point.draw_point(my_turtle)
turtle.done()


