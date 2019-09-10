import random

num_to_guess =  random.randint(1,101)
print(num_to_guess)
guess_count = 10

while guess_count > 0:
    guess_count -= 1
    print("You have", guess_count , "gueeses left ")
    num = int(input("Please enter number (1 -100): "))
    if num == num_to_guess:
        print("You have gussed number correctly !!!")
        break
    if num > num_to_guess:
        print("Your number is to big ...")
        
    if num < num_to_guess:
        print("Your number is to small ...")