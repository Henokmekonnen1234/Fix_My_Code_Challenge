#!/usr/bin/python3
"""
In this class the area and perimeter will be callculated
"""


class Square:
    """ in this class area and perimeter will be callculated

    Atributes:
        width (int): is the length of the square
    """
    width = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width ** 2

    def PermiterOfMySquare(self):
        return (self.width * 2) * 2

    def __str__(self):
        return "{} * {}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
