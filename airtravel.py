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

        self._number = number  # implementation details begin with '_'
        #   if a variable begins with one underscore, it is a private variable

    def number(self):
        """
        Flight Number
        :return: flight number
        """
        return self._number

    def airline(self):
        """
        Airline code
        :return: airline code, 2 digits
        """
        return self._number[:2]


class Aircraft:
    """
    Registration, model, num_rows, num_seats_row
    """
    def __init__(self, registration, model,
                 num_rows, num_seats_per_row):
        """
        Aircraft
        :param
        :raise: ValueError (for invalid format)
        """
        # internal attributes/variables
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        """
        Registration
        :param
        :return: registration only
        """
        return self._registration

    def model(self):
        """
        Registration
        :param
        :return: model only
        """
        return self._model

def main():
    """
    test function
    :return: none
    """

    print("Done")


if __name__ == '__main__':
    main()
    exit(0)