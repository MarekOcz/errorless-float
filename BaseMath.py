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
        if num != int(num):
            x = len(str(num).split(".")[1])
            self.multiplier = x
            self.int_num = int(num * (10 ** x))
        else:
            self.multiplier = 0
            self.int_num = int(num)

    def standard_form(self, sig_figs: int = 3, unicode_superscript: bool = True) -> str:
        """
        Returns the number in standard form as a string
        :param sig_figs: How many significant figures the standard form is given to.
        :param unicode_superscript: How do you want the code to be returned?
        :return: The standard form of the value as a string format. May add a standard form class
        """
        if self.multiplier > 0:
            if unicode_superscript:
                return str(self.int_num)[0] + "." + str(self.int_num)[1:sig_figs] + "×10⁻" + "".join(
                    ImprovedNumber.superscripts[i] for i in str(self.multiplier))


if __name__ == '__main__':
    pass