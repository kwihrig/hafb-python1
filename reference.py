"""
Learn about references
"""

def modify(k):
    """
    Modify the contents of a list
    :param k: input list
    :return: nothing
    """
    # list are passed by reference
    k.append(39)
    print("k= ", k)



def main():
    """
    test function
    :return: none
    """
    m= [9,15,24]
    print("Before m= ", m)
    modify(m)
    print("After m= ", m)



if __name__== '__main__':
        main()
        exit(0)
