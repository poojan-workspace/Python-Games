import random

def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0

    while (user_guess != random_number):
        # Taking user input as an integer because it by default
        # takes user_guess as a string and we cannot compare a string
        # with an integer in if conditions.
        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        if(user_guess > random_number):
            print("Guess a lower number!")
        
        elif(user_guess < random_number):
            print("Guess a higher number!")

        elif(user_guess == random_number):
            print(f"{user_guess} is the correct guess!!!")

guess(10)