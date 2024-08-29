class playWordle:
  word = "booob"

  def makeAGuess(userGuess):
    global word

    hint = ""
    for i in range(len(word)):
      if userGuess[i] == word[i]:
        hint += ("G")
      elif userGuess[i] in word[i]:
        hint += ("Y")
      else:
        hint += ("-")
    return hint
    

  print("Let's play wordle! /n Guess the Wordle in 6 tries. Each guess must be a valid 5-letter word. For each guess, a hint will tell you how many letters you've guessed correctly. A G represents a letter in the word and in the correct spot.. A Y represents a letter in the word but in the wrong spot. A - represents a letter not in the word in any spot. \n Guess below! \n")

  for i in range(6):
    guess = input("Put your guess here: ").lower()

    hint = makeAGuess(guess)

    print(hint)
    if hint == "GGGGG":
      print("You Won!")
      break
  if hint != "GGGGG":
    print("You Lost")
    

  print("Let's play wordle! /n Guess the Wordle in 6 tries. Each guess must be a valid 5-letter word. For each guess, a hint will tell you how many letters you've guessed correctly. A G represents a letter in the word and in the correct spot.. A Y represents a letter in the word but in the wrong spot. A - represents a letter not in the word in any spot. \n Guess below! \n")
