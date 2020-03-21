

def solve(meal_cost, tip_percent, tax_percent):
    """
    >>> solve(12.0 , 20, 8)
    15
    """
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    tot = meal_cost + tip + tax
    print(round(tot))


meal_cost = 12.0
tip_percent = 20
tax_percent = 8

# solve(meal_cost, tip_percent, tax_percent)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
