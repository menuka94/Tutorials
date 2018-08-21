# public => member_name
# protected => _member_name
# private => __member_name


class Car:
    number_of_wheels = 4
    _color = "Black"
    __year_of_manufacture = 2017


class BMW(Car):
    def __init__(self):
        print("Protected attribute color:", self._color)


car = Car()
print("Public attribute no_of_wheels:", car.number_of_wheels)
bmw = BMW()
# print("Private attribute year_of_manufacture:", car.__year_of_manufacture) # throws error
print("Private attribute year_of_manufacture:", car._Car__year_of_manufacture)  # works fine
