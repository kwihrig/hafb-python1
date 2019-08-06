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
    departure, separator, arrival = "London:Edinburgh".partition(":")
    print(departure, arrival)



if __name__ == '__main__':
    main()
    exit(0)
