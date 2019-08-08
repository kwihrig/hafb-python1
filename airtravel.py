"""
A flight class. Model for aircraft flights
"""

class Flight:
    """
    A flight with a particular passenger aircraft
    """
    def __init__(self, number):
        """
        Initializes flight number
        :param number: flight number
        :raise: ValueError (for invalid format)
        """
        # implementation details begin with '_'
        # validate flight number
        # 5 chars long, AADDD A-> ALPHA, D-> Digit
        if len(number) != 5:
            raise ValueError("Invalid flight number length {} "
                             .format(number))
        if not number[:2].isalpha():
            raise ValueError("No airline code {}"
                             .format(number))
        if not number[:2].isupper():
            raise ValueError("Not uppercase {}"
                             .format(number))
        if not number[2:].isdigit():
            raise ValueError("Invalid route code {}"
                             .format(number))

        # for char in number:
        #     char = number.decode('utf-8').split()  # split with space as default
        #       print(words)

        self._number = number  # if a variable begins with one underscore, it is a private variable

    def number(self):
        """
        Flight Number
        :return: flight number
        """
        return self._number


def main():
    """
    test function
    :return: none
    """

    print("Done")


if __name__ == '__main__':
    main()
    exit(0)