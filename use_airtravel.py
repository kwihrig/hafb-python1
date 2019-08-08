"""
Use flight class
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp


def make_flight():
    f1 = Flight("SN066", Aircraft("G-EUP", "Airbus A319",
                                  num_rows=22,
                                  num_seats_per_row=6))
    pp(f1._seating)
    f1.allocate_seat("1A", "Guido Van Rossum")  # Python creator
    f1.allocate_seat("6C", "Rasmus Lerdorf")  # php author
    f1.allocate_seat("05D", "Bjare")  # C++
    f1.allocate_seat("6F", "Larry")  # Created Perl
    f1.allocate_seat("20E", "Yukihiro")  # Wrote Ruby
    return f1

def main():
    """
    test function
    :return: none
    """

    f1 = make_flight()
    pp(f1._seating)

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