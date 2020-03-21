# Read a full line of input from stdin and save it to our
# dynamically typed variable, input_string.


def hello(s):
    """
    >>> hello("Welcome to 30 Days of Code!")
    Hello, World.
    Welcome to 30 Days of Code!

    """
    print('Hello, World.')
    print(input_string)


# input_string = input()
input_string = "Welcome to 30 Days of Code!"

# Print a string literal saying "Hello, World." to stdout.
# print(hello(input_string))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
