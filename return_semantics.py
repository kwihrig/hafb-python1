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

# Req'd parameters must come first
# Optional parameters after req'd parameters
def sum_two(num1, num2=8):
    """
    sum 2 input integer objects
    :param num1: object 1
    :param num2: object 2 (optional), default is = 8
    :return: sum of objects
    """
    total = num1 + num2
    print(num1," + ", num2, " = ", total)
    return num1 + num2



def main():
    """
    test function
    :return: none
    """

    c = [6,10,20]
    e = egg(c)
    print (c is e)
    n1 = 3
    n2 = 9
    sum_two(n1, n2)
    sum_two(n1)


    print("Only one input", sum_two(n1))

if __name__== '__main__':
        main()
        exit(0)
