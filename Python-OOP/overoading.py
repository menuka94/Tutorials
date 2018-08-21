class Square:
    def __init__(self, side):
        self.side = side

    def __add__(self, other):
        return self.side * 4 + other.side * 4


squareOne = Square(5)
squareTwo = Square(10)

print("Sum of sides of the two squares:", squareOne + squareTwo)
