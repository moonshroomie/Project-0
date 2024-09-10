import time
import sys
import os

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

def makeAGuess(userGuess):
    global word
    hint = ""
    word_chars = list(word)
    user_chars = list(userGuess)

    # First pass: check for correct positions
    for i in range(len(word)):
        if user_chars[i] == word_chars[i]:
            hint += "G"
            word_chars[i] = None
            user_chars[i] = None
        else:
            hint += "-"  # Initially mark as not in word

    # Second pass: check for wrong positions
    for i in range(len(userGuess)):
        if user_chars[i] is not None:
            if user_chars[i] in word_chars:
                hint = hint[:i] + "Y" + hint[i+1:]
                word_chars[word_chars.index(user_chars[i])] = None
    return hint

word = "spook"

class playWordle:
    
  def playWordle():
    global word
    print()
    typewriter_effect("Welcome to Wordle!", delay=0.05, color=Colors.CYAN)
    print()
    typewriter_effect("You have 6 attempts to guess the word correctly.", delay=0.03, color=Colors.YELLOW)
    typewriter_effect("Each guess must be a valid 5-letter word.", delay=0.03, color=Colors.YELLOW)
    typewriter_effect("Each time you guess, a hint will tell you how many letters you've guessed correctly.", delay=0.03, color=Colors.YELLOW)
    typewriter_effect("A 'G' represents a letter in the word and in the correct spot.", delay=0.03, color=Colors.YELLOW)
    typewriter_effect("A 'Y' represents a letter in the word but in the wrong spot.", delay=0.03, color=Colors.YELLOW)
    typewriter_effect("A '-' represents a letter not in the word in any spot.", delay=0.03, color=Colors.YELLOW)

    while True:
          for i in range(6):
            print()
            guess = input("Put your guess here: ").lower()
            hint = makeAGuess(guess)
            print(hint)
            if hint == "GGGGG":
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
                    # If the player wants to play again, the loop will restart from the beginning 
          if play_again != 'e':
                return False   

playWordle.playWordle()
