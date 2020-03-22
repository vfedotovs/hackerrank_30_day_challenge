

def then_multiples(x):
    """
    >>> then_multiples(2)
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
    2 x 4 = 8
    2 x 5 = 10
    2 x 6 = 12
    2 x 7 = 14
    2 x 8 = 16
    2 x 9 = 18
    2 x 10 = 20
        """
    for i in range(1, 11):
        print(f'{x} x {i} = {x*i}')


if __name__ == '__main__':
    n = int(input())
    then_multiples(n)

    import doctest
    doctest.testmod(verbose=True)
