# --------- Guess the Word
import random 

word_list = [
    "apple",
    "banana",
    "chocolate",
    "elephant",
    "fireplace",
    "giraffe",
    "hamburger",
    "internet",
    "jazz",
    "kangaroo",
    "lemonade",
    "mountain",
    "notebook",
    "oxygen",
    "pineapple",
    "quicksilver",
    "restaurant",
    "strawberry",
    "telephone",
    "umbrella",
    "volcano",
    "watermelon",
    "xylophone",
    "yacht",
    "zeppelin"
]

print("____________Welcome to Hangman______________")
print("_____You have 12 chances to guess the word____")
playing = True

while playing:
    secret_word = random.choice(word_list)
    sw_list = list(secret_word)
    hw_list = ["_"] * len(secret_word)
    chances = 12
    guesses = []
    
    print("\n", " ".join(hw_list))  # Initial display of the hidden word with spaces

    while chances > 0:
        guess = input("\nWhat letter will you try? ").lower()
        
        if guess in guesses:
            print("You've already guessed that letter. Try again.")
            continue
        
        guesses.append(guess)

        if guess in sw_list:
            for index, char in enumerate(sw_list):
                if char == guess:
                    hw_list[index] = guess
        else:
            chances -= 1
        
        hidden_word = " ".join(hw_list)
        
        if "_" not in hw_list:
            print("\nYou got it! The word was:", secret_word)
            break
        else:
            print("\n~~~~~~~~~    " + str(chances) + " chances remaining    ~~~~~~~~~")
            print("\nYou have tried: " + " ".join(guesses))
            print(hidden_word)
    
    if "_" in hw_list:
        print("The correct word was:", secret_word)
    
    print("===========================================")
    play_again = input("Do you want to play again? (y/n): ").lower()
    print("===========================================")
    
    if play_again != "y":
        playing = False



'''
Goup related tasks into functions:
	•	Game Setup:
	•	Initialize variables like the word list, secret word, and guesses.
	•	Input Handling:
	•	Get a valid letter from the player.
	•	Game Logic:
	•	Check if the letter is correct.
	•	Update the display for the hidden word.
	•	Check if the game is won or lost.
	•	Display:
	•	Show the hidden word and guesses.
	•	Game Flow:
	•	Handle starting a new game or ending the program.


Further enhance this game by:
	•	Adding a scoring system.
	•	Supporting difficulty levels (e.g., fewer or more chances).
	•	Handling input for full-word guesses.
	•	Using classes (object-oriented programming) for even better organization.
'''

