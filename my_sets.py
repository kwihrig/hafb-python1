"""
Learn about sets
an unordered collection of unique, immutable objects
Define it using {} but no key needed
You can use the set constructor to make one
"""


def main():
    """
    test function
    :return: none
    """
    p={6, 78, 21, 45}
    print(p, type(p))
    data = [1, 3, 5, 2, 88, 3, 1]
    print(data, type(data))
    # eliminated dups
    sdata = set(data)
    print(sdata, type(sdata))
    # iterate with for loop
    for item in sdata:
        print(item)
    # Supports membership testing: oin, not in
    print(5 in sdata)
    # Adding elemetns to sets: Add and Update
    sdata.add(45)
    print(sdata)
    sdata.update([2, 99, 44, 33, 1, 2, 88])
    print(sdata)
    # Removing elements
    # remove() method: rasies KeyError if not found
    sdata.remove(44)
    print(sdata)
#   discard () method : does not raise any error
    sdata.discard(77)
    print(sdata)
    # Copying sets
    bk_data= sdata.copy()
    print(bk_data is sdata)
    print(bk_data == sdata)
    ######### Define some sets
    blue_eyes = {"olivia", "Harry", "lily", "jack"}
    blond_hair = {"Harry", "Jack", "Amelia", "Mia", "Joshua"}
    smell_hcn = {"Harry", "Amelia"}
    taste_ptc = {"Harry", "Lily", "Amelia", "Lola"}
    o_type = {}









if __name__ == '__main__':
    main()
    exit(0)
