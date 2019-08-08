"""
A flight class. Model for aircraft flights
"""

class Flight:
    """
    A flight with a particular passenger aircraft
    """
    def __init__(self, number, aircraft):
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
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + \
                        [{letter:None for letter in seats} for _ in rows]

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

    def allocate_seat(self, seat, passenger):
        """
        Allocate Seat to passenger
        :param seat: seat designator such as '12C', '21F'
        :param passenger: passenger name
        :return: seat & name
        """
        rows, seat_letter = self._aircraft.seating_plan()
        letter = seat[-1]    # to extract last character for seat
        if letter not in seat_letter:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid row".format(row_text))
        if row not in rows:
            raise ValueError("Invalid row {}".format(row))

        if self._seating[row][letter] is not None:
            raise ValueError("Seat Taken Dude {}".format(seat))
        # Assign the seat
        self._seating[row][letter] = passenger

    def num_av_seats(self):
        """
        Seats not filled
        :param: self
        :return: qty of empty seats
        """
        return sum(sum (1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_class(self, card_printer):
        """
        printing device
        :param: self
        :param stuff for card
        :return:
        """
       for passenger, seat in sorted(self._passenger_seats()):
           pass
    # this one is incomplete as well

    def _passenger_seats(self):
        """
        printing device
        :param: self
        :param stuff for card
        :return:
        """
        # I stopped typing here - i need to leave



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

    def seating_plan(self):
        """
        Seats available
        :param
        :return: seat only
        """
        return(range(1, self._num_rows + 1),
               "ABCDEFGHJ"[:self._num_seats_per_row])


def main():
    """
    test function
    :return: none
    """

    print("Done")


if __name__ == '__main__':
    main()
    exit(0)