from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return 0


class Square(Shape):
    side = 4

    def area(self):
        print(self.side ** 2)


class Rectangle(Shape):
    width = 5
    length = 10

    def area(self):
        print(self.width * self.length)


square = Square()
square.area()

rectangle = Rectangle()
rectangle.area()

shape = Shape()  # throws error
