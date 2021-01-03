

def data_types(int1, float1, str1):
    """
    >>> data_types(12, 4.0, "is the best place to learn and practice coding!")
    16
    8.0
    HackerRank is the best place to learn and practice coding!
    >>> data_types(20, 5.0, "is the best place to learn and practice coding!")
    25
    10.0
    HackerRank is the best place to learn and practice coding!
       
"""

    # Print the sum of both integer variables on a new line.
    print(int(int1 + float1))

    # Print the sum of the double variables on a new line.
    print(float1 * 2)

    # Concatenate and print the String variables on a new line
    print("HackerRank " + str1)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
