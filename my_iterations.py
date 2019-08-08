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
    # Note: if you need to use the object again, you need to regenerate it, or you get a 0 value.
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print("Sum of first thousand prime numbers", sum(thousand_primes))
# other built-ins used with itertools: any ("or"), all ("and")
    print(any([False, False, True]))
    print(all([False, False, True]))
    print("Are there any primes between 1328-1361?", any(is_prime(x) for x in (range(1328, 1362))))



if __name__ == '__main__':
    main()
    exit(0)