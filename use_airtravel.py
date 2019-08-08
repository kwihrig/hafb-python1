"""
Use flight class
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp


def main():
    """
    test function
    :return: none
    """
    f1 = Flight("SN066", Aircraft("G-EUP", "Airbus A319",
                  num_rows=22,
                  num_seats_per_row=6))
    print(f1._seating)
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