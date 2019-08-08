"""
When working with iterators, generators, etc,
Look at the documentation for the itertools module
"""
from itertools import islice, count
from list_comprehensions import is_prime




def main():
    """
    test function
    :return: none
    """
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type(thousand_primes))
    print("list of first thousand prime numbers", list(thousand_primes))
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print("Sum of first thousand prime numbers", sum(thousand_primes))


if __name__ == '__main__':
    main()
    exit(0)