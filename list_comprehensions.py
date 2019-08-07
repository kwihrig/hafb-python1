"""
Learn list comprehensions
Readable, expressive, and effective.
"""
from math import factorial, sqrt
from pprint import pprint as pp


def main():
    """
    test function
    :return: none
    """
    words = "Today I am very happy to learn about list comprehensions".split()
    print(words)
    data = []    # empty list
    for word in words:
        # Some analysis
        data.append(word)

    # "filter" data
    print (data)

    # Task: find the length in digits of the first 20 factorials
    info = [] #empty list
    for x in range(200):
        #print(factorial(x))
        info.append(len(str(factorial(x))))
    pp(info)
    #use a list comprehension: []
    info2 = [len(str(factorial(x))) for x in range(200)]
    pp(info2) # We tried pp with a second argument to print the type as well, as in
    # pp(info2, type(info2)), but pp doesn't take 2 arguments, only 1.

    # Set comprehensions: ()
    info3 = {len(str(factorial(x))) for x in range(200)}
    pp(info3)

# Dictionary Comprehensions
    nba_teams = {'jazz':'slc', 'warriors':'oakland', 'lakers':'LA', 'clippers':'LA'}
    pp(nba_teams)
    teams_nba = {city:team for team, city in nba_teams.items()}
    pp(teams_nba) # in this example, we lose the clippers because they are from the same city?

    # Filter Predicates
    primes = [x for x in range(10001) if is_prime(x)]
    print(len(primes), primes)

def is_prime(num):
    """
    finds primes
    :param num: number to test
    :return: true for prime numbers
    false for non-primes
    """

    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True





if __name__ == '__main__':
    main()
    exit(0)
