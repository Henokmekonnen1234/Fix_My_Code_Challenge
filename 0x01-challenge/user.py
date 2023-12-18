#!/usr/bin/python3
"""
User class
this User class will store the user email
"""


class User():
    """ This user class will store the email of the user"""

    def __init__(self, email=None):
        """ This is method will initialize the email value"""
        self.__email = email

    @property
    def email(self):
        """ this is getter  method for the email instance """
        return self.__email

    @email.setter
    def email(self, value):
        """ this method will set the private instance email

        Attr:
            value (any): email of the user
        """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
