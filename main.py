import random
from colorama import Fore, Style
from os import system
from PyDictionary import PyDictionary
from content import words, title, dashes

# to clear the console
def clear():
  _ = system('clear')
  print(title)

# to play game again
def play_again():
  again = input("Try again with a different word?\nType YES or NO\n").upper()
  if again == "YES":
    print()
    print("Okay, I'll try to go easy on you this time.\n")
    clear()
    print(dashes)
    game()
  else:
    clear()
    print("Thanks for playing! <3\n\nFollow me on Github:\nhttps://github.com/volde-morticia\n\n")
  
  
# game end messages
def endgame(win, tries_left, word):
  if win == True:
    print("That's the word! Good job, you\nare amazing, you know all the words,\nhere's your star ⭐\n")
  else:
    if tries_left == 0:
      print(f"You lost! The word is {word}.\n")
  play_again()
  
# to print the full list of words
def print_list(blanks):
  for a in range(0,6):
    for b in range(0,5):
      print(blanks[a][b] + " ", end = '')
      print(Style.RESET_ALL, end = '')
    print()
  print("\n")
  return

# to check whether input is a real word
def check_if_real(guess):
    dictionary = PyDictionary()
    if dictionary.meaning(guess,True) is None:
      return False
    else:
      return True
      
# to accept the input and check if it's valid
def word_input ():
  x = 0
  while x == 0:
    guess = input("Enter your guess.\n").upper()
    print("\nProcessing...\n\n")
    length = len(guess)
    if length != 5:
      print("You can't enter a word that isn't\nexactly 5 letters!\n")
    else:
      if check_if_real(guess) == False:
        print("That's not a real word.\n")
      else:
        x = 1
        return(guess)

def game():
  # creating a blank list
  blank = ["_","_","_","_","_"]
  blanks = []
  for i in range (0,6):
    blanks.append(blank)

  # selecting a random word
  # splitting the letters of the word into a list
  # joining the letters together to get a whole word
  word_space = random.choice(words)
  word_list = word_space.split(" ")
  word = ""
  for x in word_list:
    word += x

  tries_left = 6
  win = False
  while tries_left > 0 and win == False:
    guess_list = []
    guess = word_input()
    if guess == word:
      win = True
    for n in range(0,5):
      c = guess[n]
      if c in word:
        if c == word[n]:
          c2 = Fore.GREEN + c
        else:
          c2 = Fore.YELLOW + c
      else:
        c2 = c
      guess_list.append(c2)
      
    tries_left -= 1
    blanks[5-tries_left] = guess_list

    clear()
    
    print_list(blanks)

  endgame(win, tries_left, word)

# example to explain the intructions
def example():
  ex_word = "WATER"
  ex_guess = "RAYON"
  ex_guess_list = []
  
  for n in range(0,5):
    c = ex_guess[n]
    if c in ex_word:
      if c == ex_word[n]:
        c2 = Fore.GREEN + c
      else:
        c2 = Fore.YELLOW + c
    else:
      c2 = c
    ex_guess_list.append(c2)

  print(f"EXAMPLE:\n\nLet's say the word you have to guess is: {ex_word}\n\nAnd a guess that you make is: {ex_guess}\n")
        
  for i in range(0,5):
    print(ex_guess_list[i] + " ", end = '')
    print(Style.RESET_ALL, end = '')

  print(f"\n\nHere, the letter 'R' is yellow,\nbecause in the word '{ex_word}',\nthere is an 'R', but not at the\nsame position as '{ex_guess}'.\nThe letter 'A' is green, because\nit exists in the word '{ex_word}' at the\nsame position as '{ex_guess}'\n\n")
  
  option = input("Enter ST to start the game.\n\n").upper()
  if option == "ST":
    clear()
    print(dashes)
    game()

  else:
    print("Invalid input.")
    options()
  
# options to either start the game or to view instructions
def options():
  option = input('''
?      -  how to play
st  -  start the game

''').upper()
  print()

  # game instructions
  if option == "?":
    green = Fore.GREEN + "green"
    yellow = Fore.YELLOW + "yellow"
    clear()
    print("HOW TO PLAY:\n")
    print(f"Guess the word in SIX tries.\nEach guess must be a 5-letter word.\nHit enter to submit the word.\n\nIf the colour of a letter is {yellow}", end = '')
    print(Style.RESET_ALL, end = '')
    print(f",\nit exists in the word in a different\nspot.\nIf the colour of a letter is {green}", end = '')
    print(Style.RESET_ALL, end = '')
    print(",\nit exists in the word at the same\nspot.")
    print("If a letter is neither of those\ncolours, it doesn't exist in the\nword.\n")
    option = input("Enter EX to view an example, OR\nEnter ST to start the game.\n\n").upper()

  if option == "EX":
    clear()
    example()
  elif option == "ST":
    clear()
    print(dashes)
    game()

  if option != "?" and option != "ST" and option != "EX":
    print("Invalid input.")
    options()

# title
print(title)
options()
