"""
File Info Here
"""

def egg(var):
    """
    dummy function returns variable back to user
    :param var: input object
    :return: input object
    """
    return var

def sum_two(num1, num2):
    """
    sum 2 input objects
    :param num1: object 1
    :param num2: object 2
    :return: sum of objects
    """
    return num1 + num2



def main():
    """
    test function
    :return: none
    """

    c = [6,10,20]
    e = egg(c)
    print (c is e)
    #n1 = 3
    #n2 = 9
    n1 = "hot"
    n2 = "dog"
    print(n1," + ", n2, " = ", sum_two(n1, n2))


if __name__== '__main__':
        main()
        exit(0)
