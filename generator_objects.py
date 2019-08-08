"""
Generator objects are acros between comprehensions and generator functions.
Syntax is very similar to list comprehension, but with parenthesis:
    (expr(item) fo ritem in iterable)
"""
from list_comprehensions import is_prime



def main():
    """
    test function
    :return: none
    """
    # list with first 1 million sq numbers
    m_sq = (x*x for x in range(1, 1000001))
    print(m_sq, type(m_sq))
    print('sum of first 1M squares is:', sum(m_sq))
    print('sum of first 1M squares is:', sum(x*x for x in range(1, 1000001)))
    # sum of primes from 1 - 10K
    print('sum of prime numbers from 1 to 10K:',
          sum(x for x in range(1, 10001) if is_prime(x)))



if __name__ == '__main__':
    main()
    exit(0)