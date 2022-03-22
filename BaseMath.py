from typing import *


class MathError(Exception):
    pass


class ImprovedNumber:
    pi = 3.1415926535898
    superscripts = {"-": "⁻",
                    "1": "¹",
                    "2": "²",
                    "3": "³",
                    "4": "⁴",
                    "5": "⁵",
                    "6": "⁶",
                    "7": "⁷",
                    "8": "⁸",
                    "9": "⁹",
                    "0": "⁰"}
    """
    Number class which allows for floating point error-less decimal arithmetic as well as extra features like standard
    form. Works using exact values like pi
    """

    def __init__(self, num: int or float):
        """
        :param num: The number for the class. This will be returned as a readable number format however within the code
        is stored as an integer and a multiplier.
        """
        if type(num) not in (int, float):
            raise TypeError("parameter 'num' needs to be of type 'int' or 'float'.")
        self.multiplier = 0
        self.int_num = num
        while int(self.int_num) != self.int_num:
            self.int_num *= 10
            self.multiplier += 1
        self.int_num = int(self.int_num)

    def standard_form(self, sig_figs: int = 3, unicode_superscript: bool = True) -> str:
        """
        Returns the number in standard form as a string
        :param sig_figs: How many significant figures the standard form is given to.
        :param unicode_superscript: How do you want the code to be returned?
        :return: The standard form of the value as a string format. May add a standard form class
        """
        if len(str(self.int_num)) < self.multiplier:  # Negative power of 10
            ten_power = len(str(self.int_num)) - self.multiplier
            if unicode_superscript:
                return str(self.int_num)[0] + "." + str(self.int_num)[1:sig_figs] + "×10" + "".join(
                    ImprovedNumber.superscripts[i] for i in str(ten_power))


def random_func_gen(length: int, func: Callable) -> str:
    from random import randint
    returned = ""
    for i in range(length):
        temp = randint(0, 1000) / (10 ** randint(0, 10))
        print(str(temp) + " " * (17 - len(str(temp))) + "      ", end="")
        temp_class = ImprovedNumber(temp)
        returned += str(temp) + " " * (17 - len(str(temp)))
        print(str(func(temp_class)) + "\n")
        returned += str(func(temp_class)) + "\n"
    return returned


if __name__ == '__main__':
    print(random_func_gen(length=1000, func=lambda x: ImprovedNumber.standard_form(self=x)))
