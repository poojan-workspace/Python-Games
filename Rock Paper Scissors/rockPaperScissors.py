import random

def game():
    continue_playing = 'y'

    while(continue_playing == 'y'):
        user_input = input("Enter 'r' for rock, 'p' for paper, 's' for scissors.")
        computer_input = random.choice(['r', 'p', 's'])

        if(user_input == computer_input):
            print("It's a tie!")
    
        elif((user_input == 'r' and computer_input == 's') or (user_input == 'p' and computer_input == 'r') or (user_input == 's' and computer_input == 'p')):
            print(f"Computer guessed {computer_input}. User Wins!")

        else:
            print(f"Computer guessed {computer_input}. Computer Wins!")

        continue_playing = input("Press 'y' to continue playing.").lower() 

game()