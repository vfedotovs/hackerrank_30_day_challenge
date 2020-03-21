
def answer(n):

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
    doctest.testfile("04_test.txt", verbose=True, report=True)
    # doctest.testmod(verbose=True)
