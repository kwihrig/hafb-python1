"""
Use flight class
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp


def make_flight():
    flight = Flight("SN066", Aircraft("G-EUP", "Airbus A319",
                                  num_rows=22,
                                  num_seats_per_row=6))
    pp(flight._seating)
    flight.allocate_seat("1A", "Guido Van Rossum")  # Python creator
    flight.allocate_seat("6C", "Rasmus Lerdorf")  # php author
    flight.allocate_seat("05D", "Bjare")  # C++
    flight.allocate_seat("6F", "Larry")  # Created Perl
    flight.allocate_seat("20E", "Yukihiro")  # Wrote Ruby
    return flight

def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}" \
            " Flight: {1} " \
            " Seat: {2} " \
             "Aircraft: {1} " \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = "+" + "-" * (len(output) -2) + "+"
    border = "|" + " " * (len(output) -2) + "|"
    lines  = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()



def main():
    """
    test function
    :return: none
    """

    flight_1 = make_flight()
    pp(flight_1._seating)
    print("Available seats: ",
       flight_1.num_av_seats())


    # f2 = Flight("S13")
    # print(f2, f2.number())

    # f3 = Flight("ab345")
    # print(f3, f3.number())
    # f2 = Flight("SN013")
    # print(f2, f2.number(), f2.airline())

    #Could use: Flight.number(f)

    # a1 = Aircraft("G-EUP", "Airbus A319",
    #               num_rows=22,
    #               num_seats_per_row=6)
    # print(a1.registration(), a1.model())
    # print(a1.seating_plan())
    # pp(a1._seating)

    print("done")


if __name__ == '__main__':
    main()
    exit(0)