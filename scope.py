"""
Learn about scoping in Python
"""
count = 0   # global cbject


def show_count():
    """
    Display current count
    :return: none
    """
    print(count)


def set_count(num):
    num=0
    """
    set global counter to input
    :param num: input number
    :return: none
    """
    global count
    count = num


def main():
    """
    test function
    :return: none
    """
    show_count()
    set_count(9)
    show_count()
#    print(count)




if __name__ == '__main__':
    main()
    exit(0)
