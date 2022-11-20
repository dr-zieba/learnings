import numpy as np
from PIL import Image

class Square(object):
    def __init__(self, x, y, side_width, color):
        self.x = x
        self.y = y
        self.side_width = side_width
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x : self.x + self.side_width, self.y : self.y + self.side_width] = self.color

class Rectangle(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.width, self.y: self.y + self.height] = self.color


class Canvas(object):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((self.width, self.height,3), dtype=np.uint8)
        self.data[:] = self.color

    def make_image(self, image_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)


canvas = Canvas(600,600,(255,255,255))

square = Square(50,50,100,(122,45,0))
square.draw(canvas)

rec = Rectangle(100,100,50,80,(200,132,5))
rec.draw(canvas)

canvas.make_image('test.png')

