from abc import ABC, abstractmethod
from functions import check_color_input
from functions import InputInt
import pyglet
class GeometricFigure(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_area(self):
        pass

class Color:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

class Rectangle(GeometricFigure):
    def __init__(self, color):
        super().__init__(color)
        print("Enter the width of the rectangle:")
        self.width = int(InputInt())
        print("Enter the height of the rectangle:")
        self.height = int(InputInt())

    def get_area(self):
        return self.width * self.height

    def get_info(self):
        return f"Rectangle, color: {self.color.color}, width: {self.width}, height: {self.height}, square: {self.get_area()}"

class Trapezoid(GeometricFigure):
    def __init__(self, color):
        super().__init__(color)
        print("Enter the base a of the trapezoid: ")
        self.a = int(InputInt())
        print("Enter the base b of the trapezoid: ")
        self.b = int(InputInt())
        print("Enter the height of the trapezoid: ")
        self.h = int(InputInt())
    def get_area(self):
        return ((self.a + self.b) / 2) * self.h

    def get_info(self):
        return f"Trapezoid, color: {self.color.color}, Base a: {self.a}, Base b: {self.b}, square: {self.get_area()}"

def function_task4():
    check = False
    while check == False:
        bl = False
        color = ""
        while bl == False:
            color = input("Input Color for Rectangle")
            bl = check_color_input(color)
        rect = Rectangle(color)
        window = pyglet.window.Window(width=700, height=700)
        rectangle = pyglet.shapes.Rectangle(x=500, y=500, width=rect.width, height=rect.height)
        if rect.color == "White":
            rectangle.color = (255, 255, 255)
        elif rect.color == "Black":
            rectangle.color = (0, 0, 0)
        elif rect.color == "Red":
            rectangle.color = (255, 0, 0)
        elif rect.color == "Green":
            rectangle.color = (0, 255, 0)
        elif rect.color == "Blue":
            rectangle.color = (0, 0, 255)
        elif rect.color == "Yellow":
            rectangle.color = (255, 255, 0)
        elif rect.color == "Orange":
            rectangle.color = (255, 165, 0)
        elif rect.color == "Purple":
            rectangle.color = (128, 0, 128)
        elif rect.color == "Pink":
            rectangle.color = (255, 192, 203)

        bl = False
        color_trap = ""
        while bl == False:
            color_trap = input("Input Color for Rectangle")
            bl = check_color_input(color_trap)
        trap = Trapezoid(color_trap)
        triangle1 = pyglet.shapes.Triangle(x=100, y=100, x2=(trap.a-trap.b)/2+100, y2=100, x3=(trap.a-trap.b)/2+100, y3=100+trap.h)
        triangle2 = pyglet.shapes.Triangle(x=100+trap.a, y=100, x2=100+trap.a-(trap.a-trap.b)/2, y2=100, x3=100+trap.a-(trap.a-trap.b)/2, y3=100+trap.h)

        rectangle2 = pyglet.shapes.Rectangle(x=100+(trap.a-trap.b)/2, y=100, width=trap.b, height=trap.h)
        if trap.color == "White":
            rectangle2.color = (255, 255, 255)
            triangle2.color = (255, 255, 255)
            triangle1.color = (255, 255, 255)
        elif trap.color == "Black":
            rectangle2.color = (0, 0, 0)
            triangle2.color = (0, 0, 0)
            triangle1.color = (0, 0, 0)
        elif trap.color == "Red":
            rectangle2.color = (255, 0, 0)
            triangle2.color = (255, 0, 0)
            triangle1.color = (255, 0, 0)
        elif trap.color == "Green":
            rectangle2.color = (0, 255, 0)
            triangle2.color = (0, 255, 0)
            triangle1.color = (0, 255, 0)
        elif trap.color == "Blue":
            rectangle2.color = (0, 0, 255)
            triangle2.color = (0, 0, 255)
            triangle1.color = (0, 0, 255)
        elif trap.color == "Yellow":
            rectangle2.color = (255, 255, 0)
            triangle2.color = (255, 255, 0)
            triangle1.color = (255, 255, 0)
        elif trap.color == "Orange":
            rectangle2.color = (255, 165, 0)
            triangle2.color = (255, 165, 0)
            triangle1.color = (255, 165, 0)
        elif trap.color == "Purple":
            rectangle2.color = (128, 0, 128)
            triangle2.color = (128, 0, 128)
            triangle1.color = (128, 0, 128)
        elif trap.color == "Pink":
            rectangle2.color = (255, 192, 203)
            triangle2.color = (255, 192, 203)
            triangle1.color = (255, 192, 203)
        @window.event
        def on_draw():
            window.clear()
            rectangle.draw()
            triangle1.draw()
            triangle2.draw()
            rectangle2.draw()
        pyglet.app.run()
        try:
            window.set_fullscreen().save("image.png")
        except:
            print("smth gone Incorrect")
        print("If you want to stop this task write 'stop', else task will rerun")
        str = input()
        if str == "stop":
            return