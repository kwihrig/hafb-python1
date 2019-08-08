"""
A flight class. Model for aircraft flights
"""

class Flight:
    """
    A flight with a particular passenger aircraft
    """
    def __init__(self, number):
        # implementation details begin with '_'
        self._number = number # if a variable begins with one underscore, it is a private variable

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