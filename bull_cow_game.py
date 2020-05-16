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
    """
    Function generates 4 random nonrepeating digit list in range from 0-9  
    
    Parameters: none taken
    
    Return: list with 4 ints
    """
    number_list = []
    while len(number_list) < 4:
        number = random.randrange(0, 9)
        if number not in number_list:
            number_list.append(number)
    return number_list


def get_user_guess():
    """
    Function collects 4 digit string from stdin
    
    Parameters: none taken
    
    Return: 4 digit string
    
    Rise exception: 
         # Validation #1 for exact len of 4 : will catch if not equal 4 len
         # Validation #2 for is numeric : will catch if entered value is not number    
    """
    possible_choises = [1,2,3,4,5,6,7,8,9,0]
    required_len = 4
    input_is_valid = False
    while input_is_valid is False
        user_guess = input("\nEnter 4 numbers:") 
        # Validation #1 for exact len of 4
        if len(user_guess) != required_len:
            print("Entered number count is more or less than 4 please try again. "
        # Validation #2 for is numeric
        if user_guess.isnumeric():
            input_is_valid = True
         else:
            print("Entered value does not contain 4 numbers please try again. "
    return user_guess

number_to_guess = gen_random_ints()

# TODO: @vfedotovs review code below                  
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


attempt_count = 0
while attempt_count < 20:
    ug = get_user_guess()
    if check_win(number_to_guess, ug) is True:
        print("You have guessed all 4 numbers in ", attempt_count, " attempts !!!")
        break
    else:
        cow_count = check_cows(number_to_guess, ug)
        bull_count = check_bulls(number_to_guess, ug)
        print("You have ", cow_count, " cows, ", bull_count, " bulls ")
    attempt_count += 1

 print("You have lost game guess count is more than 20 ... ")
