import random
import string

# import words list variable from wordsForHangman.py file
from wordsForHangman import words

def get_valid_word(words):
    word = random.choice(words) # Randomly chooses something from the Words List
    while('-' in word or ' ' in word):
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # Get all the letters in the words as a set/list
    alphabet = set(string.ascii_uppercase) # Get all the 26 letters of English Language in uppercase
    used_letters = set() # Set of used letters by user

    lives = len(word)

    while (len(word_letters) > 0 and lives > 0):
        # Print the Letters that are used for the user
        # .join(['a', 'b', 'cd']) --> 'a b cd'
        print('\nYou have used these letters: ', ' '.join(used_letters))

        # What the current word is (i.e. W - R D) using - and letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        print(f"You have {lives} lives left!")
        user_input = input("Enter Letter: ").upper()

        if (user_input in alphabet - used_letters):
            used_letters.add(user_input)

            if (user_input in word_letters):
                word_letters.remove(user_input)

            else:
                lives = lives - 1

        elif (user_input in used_letters):
            print("You have already used the letter. Please try again!")

        else:
            print("Invalid character. Please try again!")
    
    if (len(word_letters) == 0):
        print(f"You have guessed the word {word} correctly!")

    else:
        print("You lost all your lives!")
        print(f"The word was {word}. Better Luck Next Time!")
    
hangman()