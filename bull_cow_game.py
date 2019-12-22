import random

"""
### GAME RULES ###
For every digit that the user guessed correctly in the correct place,
they have a “cow”.

For every digit the user guessed correctly in the wrong place
is a “bull.”

Every time the user makes a guess, tell them how many “cows” and “bulls”
they have.

Once the user guesses the correct number, the game is over.

Keep track of the number of guesses the user makes throughout
the game and tell the user at the end.
"""


def gen_random_ints():
    alist = []
    while len(alist) < 4:
        x = random.randrange(0, 9)
        if x not in alist:
            alist.append(x)
    return alist


number_to_guess = gen_random_ints()
# print(number_to_guess)


def get_user_guess():
    #print("\nEnter 4 numbers:")
    user_guess = input("\nEnter 4 numbers:")  # collect string so we caniterate over it
    return user_guess

    # TODO: error checking needed for invalid input not str and len count not 4
    # test what happens if user enters 8888 if bull cow is displayed correctly


def check_win(number_to_guess: list, ug: str):
    A = number_to_guess
    if A[0] == int(ug[0]) and A[1] == int(ug[1]) and \
       A[2] == int(ug[2]) and A[3] == int(ug[3]):
        return True


def check_cows(number_to_guess: list, ug: str):
    B = number_to_guess
    cows = 0
    for i in range(len(B)):  # i is index
        if B[i] == int(ug[i]):
            cows += 1
    return cows


def check_bulls(number_to_guess: list, ug: str):
    bulls = 0
    C = number_to_guess
    for i in range(len(C)):  # i is index
        if C[i] != int(ug[i]) and (int(ug[i]) in C):
            bulls += 1

    return bulls


count = 0

while count < 20:

    ug = get_user_guess()
    if check_win(number_to_guess, ug) is True:
        print("You have guessed all 4 numbers in ", count, " attempts !!!")
        break
    else:
        cow_count = check_cows(number_to_guess, ug)
        bull_count = check_bulls(number_to_guess, ug)
        print("You have ", cow_count, " cows, ", bull_count, " bulls ")

    count += 1
# print("Yuu have reached guess count limit ... ")
