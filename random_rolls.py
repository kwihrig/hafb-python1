"""
Simulate 6000 rolls of a die (1-6)
"""
import random

def roll_die(num):
    """
    Random roll of adie
    :param num:number of rolls
    :return: a list of frequencies
    Index 0 maps to 1
    Index 1 maps to 2
    etc
    """
    freq = [0] * 6         # list initial values to 0
    for roll in range(num):
        n = random.randint(1, 6)
        freq[n - 1] += 1
#        print(random.randint(1, 6))
    return freq
    print (freq)


def main():
    """
    test function
    :return: none
    """
    num = int(input("How many times you need to roll: "))
    l = roll_die(num)
    for roll, total in enumerate(l):
        print ("total roll sof {} = {}".format(roll+1, total))


#    for roll in range(10):
#       print (random.randrange(1,7))


if __name__ == '__main__':
    main()
    exit(0)
