"""
Use flight class
"""
from airtravel import Flight

def main():
    """
    test function
    :return: none
    """
    f = Flight("SN066")
    print(f.number())
    f2 = Flight("SN013")
    print(f2, f2.number())
    #Could use: Flight.number(f)

if __name__ == '__main__':
    main()
    exit(0)