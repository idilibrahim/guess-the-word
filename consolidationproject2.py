# Game: Word Guessing 

#Import all modules
import random
import matplotlib.pyplot as plt

#define function t read word list from file 
def read_word_list(filename):
    """Read a word list from a file
    Arg: 
        filename (str): the files name that contains the word list.
    Return:
        lists: a list of words read from the file """
    try:
        #try to open the file and read its contents, spliting each line into  list
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        #incase where file is not found
        print(f"Error: File '{filename}' not found.")
        return []
# Word banks for different themes
word_banks = {
    "animals" : "animals.txt" , # filename for animal word list
    "fruits"  : "fruits.txt" , # filename for fruit word list
    "random"  : "random.txt" , # filename for random word list
}

# define a function to choose random word from themes word bank
def choose_word(theme):
    """Choose a random word from the theme's word bank."""
    #get the filename from the themes file wordlist
    filename = word_banks.get(theme, word_banks["random"])
    #reads the file and its word list 
    word_bank = read_word_list(filename)
    if word_bank:
        #if the word list is not empty, choose a random word
        return random.choice(word_bank)
    else:
        # if the word list empty, print message 
        # and choose from default llist
        print("Using default word list.")
        return random.choice(word_banks["random"])
    
# define a function to show the word with
# guessed letters
def display_word(word, guessed_letters):
    """Display the word with guessed letters."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# defines the maiin function of the game
def play_game(theme):
    """Play the word guessing game."""
    # choose random word based on what theme was chose
    word = choose_word(theme)
    guessed_letters = [] # list to store gussed letters
    attempts = 0 # counts number of attempts
    word_guesses = 0 # counts number of word guesses
    max_word_guesses = 3 # 3 is the maxium of word guesses
    guess_history = []  # tracks history, so it could be plotted 

   #prints welcome message and theme of game
    print("Welcome to the Word Guessing Game")
    print("Your job is to guess the secret word!")
    print(f"Theme: {theme.capitalize()}\n")

    # game loop
    while word_guesses < max_word_guesses:
        print("\nWord:", display_word(word, guessed_letters))
        # tells the user for a guess
        guess = input("Enter a letter or guess the whole word: ").lower()

        if len(guess) == 1:  # guess a letter
            if guess in guessed_letters:
                print("You've guessed that letter already!")
            else:
                guessed_letters.append(guess)
                attempts += 1
                count = word.count(guess)
                if count > 0:
                    print(f"Yes, the letter {guess} appears {count} time(s) in the word.")
                else:
                    print(f"No, there are no instances of the letter {guess} in the word.")
                if all(letter in guessed_letters for letter in word):
                    print(f"\nYou've guessed the word '{word}' in {attempts} attempts! Congratulations!")
                    break
        else:  # Guessing the word
            word_guesses += 1
            attempts += 1
            if guess == word:
                print(f"\nYou've guessed the word '{word}' in {attempts} attempts! Congratulations!")
                break
            else:
                print("Unfortunately, that is not the word.")
                if word_guesses >= max_word_guesses:
                    print(f"\nOh no! You used all your word guesses. The word was '{word}'.")
                    break
        
        # Tracks the number of guesses made
        guess_history.append(len(guessed_letters))  

    # Guess plot history
    plt.plot(range(1, len(guess_history) + 1), guess_history)
    plt.xlabel("Attempt Number")
    plt.ylabel("Number of Guesses")
    plt.title("Guess History")
    plt.grid(True)
    plt.show()

#Define main functionn 
def main():
    """Main function to start the game"""
    # tells the user to choose a theme to start the game
    theme = input("Choose a theme (animals, fruits, random): ").lower()
    play_game(theme)

if __name__ == "__main__":
    main()









#Test animal theme 
   # print("Test case: animal theme")
    #play_game ("animals")

#test fruit theme 
   # print("\nTest: fruit theme")
   # play_game("fruits")

# 3 test random theme 
    #print("\nTest: random theme")
   # play_game ("random")
    
