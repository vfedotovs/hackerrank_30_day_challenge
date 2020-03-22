
# string = "abcd"


def convert(str1):
    """
    >>> convert(3)
    3
    >>> convert("za")
    Bad String
    """
    try:
        i = int(str1)
        print(i)
    except ValueError:
        # Handle the exception
        print("Bad String")


if __name__ == "__main__":
    # S = input().strip()
    # print(convert(S))

    import doctest
    doctest.testmod(verbose=True)
