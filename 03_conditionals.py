
def answer(n):
    """
    >>> answer(3)
    'Weird'
    >>> answer(24)
    'Not Weird'
    """
    if n % 2 == 0 and n > 20:
        return "Not Weird"
    if n % 2 == 0 and n <= 20 and n > 5:
        return "Weird"
    if n % 2 == 0 and n < 6 and n > 1:
        return "Not Weird"
    if n % 2 != 0:
        return "Weird"


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
