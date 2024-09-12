import time
import sys
import os

"""
This module defines a set of ANSI escape codes for various colors, as well as a function to clear the screen and a function to create a typewriter effect when printing text.

The `Colors` class defines a set of constants that represent different ANSI color codes, which can be used to change the color of text in the terminal.

The `clear_screen()` function checks the operating system and clears the screen using the appropriate command (`cls` for Windows, `clear` for other systems).

The `typewriter_effect()` function takes a string of text and prints it character by character with a specified delay, creating a typewriter-like effect. The text can also be colored using the ANSI color codes from the `Colors` class.

The `makeAGuess()` function takes a user's guess for the Wordle game and compares it to the actual word. It returns a string of hints indicating which letters are in the correct position, in the word but in the wrong position, or not in the word at all.
"""
class Colors:
      BLACK = '\033[30m'
      RED = '\033[31m'
      GREEN = '\033[32m'
      YELLOW = '\033[33m'
      BLUE = '\033[34m'
      MAGENTA = '\033[35m'
      CYAN = '\033[36m'
      WHITE = '\033[37m'
      BRIGHT_BLACK = '\033[90m'
      BRIGHT_RED = '\033[91m'
      BRIGHT_GREEN = '\033[92m'
      BRIGHT_YELLOW = '\033[93m'
      BRIGHT_BLUE = '\033[94m'
      BRIGHT_MAGENTA = '\033[95m'
      BRIGHT_CYAN = '\033[96m'
      BRIGHT_WHITE = '\033[97m'
      RESET = '\033[0m'

def clear_screen():
    # Check if the system is Windows
    if os.name == 'nt':
        os.system('cls')  # Clear screen for Windows
    else:
        os.system('clear') 

def typewriter_effect(text, delay=0.1, color=Colors.RESET):
      for char in text:
          sys.stdout.write(f"{color}{char}{Colors.RESET}")
          sys.stdout.flush()  # Ensures the output is displayed immediately
          time.sleep(delay)
      print() 

# not sure why but my wordle stopped working so i had AI regenerate it for me
def makeAGuess(userGuess):
    global word
    hint = ""
    word_chars = list(word)
    user_chars = list(userGuess)

    # First pass: check for correct positions
    for i in range(len(word)):
        if user_chars[i] == word_chars[i]:
            hint += "X"
            word_chars[i] = None
            user_chars[i] = None
        else:
            hint += "-"  # Initially mark as not in word

    # Second pass: check for wrong positions
    for i in range(len(userGuess)):
        if user_chars[i] is not None:
            if user_chars[i] in word_chars:
                hint = hint[:i] + "O" + hint[i+1:]
                word_chars[word_chars.index(user_chars[i])] = None
    return hint


word = "field"

class playWordle: # not sure why but my wordle stopped working so i had AI regenerate it for me
    
  def playWordle():
        """
        Plays a game of Wordle, where the user has 6 attempts to guess a 5-letter word.
        
        The game provides hints to the user after each guess, indicating which letters are in the correct position (X), in the word but in the wrong position (O), or not in the word at all (-).
        
        The user can play the game repeatedly by pressing 'E' to play again after losing or winning.
        """
        global word
        while True:
            print()
            typewriter_effect("Welcome to Wordle!", delay=0.05, color=Colors.CYAN)
            print(f"""{Colors.YELLOW}
    You have 6 attempts to guess the word correctly.
    Each guess must be a valid 5-letter word.
    Each time you guess, a hint will tell you how many letters you've guessed correctly.
    A 'X' represents a letter in the word and in the correct spot.
    A 'O' represents a letter in the word but in the wrong spot.
    A '-' represents a letter not in the word in any spot.
    Good luck!
                {Colors.RESET}""")

            for i in range(6):
                print()
                guess = input("Put your guess here: ").lower()
                hint = makeAGuess(guess)
                print(hint)
                if hint == "XXXXX":
                    print()
                    typewriter_effect("You Won!", delay=0.04, color=Colors.BRIGHT_GREEN)
                    return True

            print()
            typewriter_effect("You Lost!", delay=0.04, color=Colors.BRIGHT_RED)
            while True:
                play_again = input("Press 'E' to play again: ").lower()
                if play_again == 'e':
                    clear_screen()
                    break
                else:
                    typewriter_effect("Invalid Input. Press 'E' to continue.", delay=0.05, color=Colors.RED)
                    print()
            if play_again != 'e':
                return False

playWordle.playWordle()