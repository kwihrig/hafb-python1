"""
Use flight class
"""

from airtravel import Flight



def main():
    """
    test function
    :return: none
    """
    f = Flight()
    print(f, type(f))
    print(f.number())


if __name__ == '__main__':
    main()
    exit(0)