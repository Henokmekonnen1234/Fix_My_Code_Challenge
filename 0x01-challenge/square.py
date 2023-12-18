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
        """ this will initialize the instances

        Attr:
            args (tuple): tuple variable contain values
            kwargs (dict): dict variable contain pair of key and values
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square

        Returns:
            int: return the area of the square
        """
        return self.width ** 2

    def PermiterOfMySquare(self):
        """this will calculate the perimeter of the square

        Returns:
            int: returns the perimeter of the square
        """
        return (self.width * 2) * 2

    def __str__(self):
        """this will show the str representation below when
            the class called

        Returns:
            str: return the below string when the class called
        """
        return "{} * {}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
