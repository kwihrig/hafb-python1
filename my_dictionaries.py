"""
Learn about dictionaries
"""


def main():
    """
    test function
    :return: none
    """
    urls = {
        "google":"www.google.com",
        "yahoo":"www.yahoo.com",
        "twitter":"www.twitter.com",
        "wsu":"www.weber.edu"
    }

    print (urls, type(urls))
    # access by key:[key]
    print (urls["wsu"])
    # build dict with dict() constructor
    names_age = [('Alice', 32), ('Mario', 23), ('Hugo', 21)]
    d = dict(names_age)
    print(d)
    # another method)
    phonetic = dict(a='alpha', b='bravo', c='charlie', d='delta')
    print (phonetic)
    # make a copy
    e = phonetic.copy()
    print (e)
# updating a dict






if __name__ == '__main__':
    main()
    exit(0)
