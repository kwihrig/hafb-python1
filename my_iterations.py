"""
When working with iterators, generators, etc,
Look at the documentation for the itertools module
"""
from itertools import islice, count, chain
from list_comprehensions import is_prime



def main():
    """
    test function
    :return: none
    """
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000) # Returns a list of first 1000 primes
    print(thousand_primes, type(thousand_primes))
    print("list of first thousand prime numbers", list(thousand_primes))
    # Note: if you need to use the object again, you need to regenerate it, or you get a 0 value.
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print("Sum of first thousand prime numbers", sum(thousand_primes))
# other built-ins used with itertools: any ("or"), all ("and")
    print(any([False, False, True]))
    print(all([False, False, True]))
    print("Are there any primes between 1328-1361?", any(is_prime(x) for x in (range(1328, 1362))),
          list(x for x in range(1328, 1362) if is_prime(x)))
    # Check if all names in an iterable are in the title form: first letter capitalized
    names = ["London", "New York", "ogden"]
    print(all(name == name.title() for name in names))
    # Another built-in: zip
    sunday = [2, 2, 5, 7, 9, 10, 9, 6, 4, 4]
    monday = [12, 14, 14, 15, 15, 16, 13, 10, 9]
    tuesday = [13, 14, 15, 15, 16, 17, 16, 16, 12, 12]
#    wednesday = [15, 15, 16]
    # monday = [12, 14, 14, 15, 15, 16, 13, 10, 9]
    # monday = [12, 14, 14, 15, 15, 16, 13, 10, 9]
    # Calculate min, max, ave for 3 days
    for temps in zip(sunday, monday, tuesday):
        print("min={:4.1f}, max={:4.1f}, avg={:4.1f}".format(
            min(temps), max(temps), sum(temps)/len(temps) ))

    # Chain




if __name__ == '__main__':
    main()
    exit(0)