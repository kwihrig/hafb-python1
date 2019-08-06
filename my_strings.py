"""
File Info Here
"""


def main():
    """
    test function
    :return: none
    """
    s1 = "This is super cool"
    print("Size of s1", len(s1))
    # concatenation "+")
    s2 = "Weber" + "State" + "University"
    print(s2)
    # if you need to join large strings, use the join () method
    # instead of + operator
    teams = ["Real Madrid", "Barcelona", "Manchester United"]
    record = ":".join(teams)
    # print (record)
    # Split record
    print("Split rec", record.split(":"))
    # Partitioing Strings
    # you can use the "dummy" object: _
    departure, separator, arrival = "London:Edinburgh".partition(":")
    print(departure, arrival)
    t = "London:Edinburgh".partition(":")
    print(t, type(t))
    # String formatting using format()
    print("The age of {0} is {1}".format("Mario",34))
    print("The age of {0} is {1}, and the birthday of {0} is {2}".format("Mario",34, "August 12th"))
    # Omitting the index
    print('the best numbers are {} and {}' .format(4,22))



if __name__ == '__main__':
    main()
    exit(0)
