"""
Simulate 6000 rolls of a die (1-6)
"""
import random
import statistics


def roll_die(num):
    """
    Random roll of a die
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


def main():
    """
    test function
    :return: none
    """
    num = int(input("How many times you need to roll: "))
    result = roll_die(num)
    for roll, total in enumerate(result):
        print ("total rolls of {} = {}".format(roll+1, total))

    print("Average = {}".format(sum(result)/len(result)))
    print("Mean = {}".format(statistics.mean(result)/len(result)))
    print("Median = {}".format(statistics.median(result)/len(result)))



#    for roll in range(10):
#       print (random.randrange(1,7))


if __name__ == '__main__':
    main()
    exit(0)
