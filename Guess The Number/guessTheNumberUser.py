import random

def guess(x):
    low = 1
    high = x
    user_response = ''
    if(low == high):
        print("Invalid Upper Bound. Please set a number greater than 1")

    while(user_response != 'c'):
        computer_guess = random.randint(low, high)
        print(f"My guess is {computer_guess}.")
        user_response = input("Is my guess High 'h', Low 'l', Correct 'c'").lower()

        if(user_response == 'h'):
            high = computer_guess - 1

        elif(user_response == 'l'):
            low = computer_guess + 1

    print(f"{computer_guess} is the correct guess!")

upper_bound = int(input("Set an upper bound: "))
guess(upper_bound)