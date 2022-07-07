import random
from colorama import Fore, Style
from os import system
from time import sleep
from PyDictionary import PyDictionary


words = ["S H A K Y", "C L U M P", "S L A S H", "C L A C K", "S C I O N", "B I G O T", "C R U E L", "S Q U A D", "S H R U G", "C R A Z E", "S A U C E", "S T U N K", "P U L S E", "I N L A Y", "G L E A N", "E D G E D", "H A V O C", "E A V E S", "D A N C E", "S P O R E", "S P I T E", "T R U C E", "E X I S T", "Q U I C K", "D R E A M", "P R O X Y", "S O B E R"]


# to clear the console
def clear():
  sleep(1)
  _ = system('clear')
  print('''
                    _ _     
__ __ _____ _ _ __| | |___ 
\ V  V / _ \ '_/ _` | / -_)
 \_/\_/\___/_| \__,_|_\___|
               
''')


# function to check whether it's a real word
def check_if_real(guess):
    dictionary = PyDictionary()
    if dictionary.meaning(guess,True) is None:
      return False
    else:
      return True
      

# function to accept the input
def word_input ():
  x = 0
  while x == 0:
    guess = input("Enter your guess.\n").upper()
    print()
    length = len(guess)
    if length != 5:
      print("You can't enter a word that isn't\nexactly 5 letters! smh\n")
    else:
      if check_if_real(guess) == False:
        print("That's not a real word. smh.\n")
      else:
        x = 1
        return(guess)


def game():
  # creating a blank list
  blank = ["_","_","_","_","_"]
  blanks = []
  for i in range (0,6):
    blanks.append(blank)

  # selecting a random word, splitting the letters, joining the letters
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
    
    # printing the full list
    for a in range(0,6):
      for b in range(0,5):
        print(blanks[a][b] + " ", end = '')
        print(Style.RESET_ALL, end = '')
      print()
    print("\n")

  # winning & losing prompt
  if win == True:
    print("That's the word! Wow, I kinda wasn't\nexpecting you to win. Good job, you\nare amazing, you know all the words,\nhere's your star ⭐\n")
  else:
    if tries_left == 0:
      print(f"The word is {word}.\nLooks like you suck at this game!\nDo you even know any words?\nIt's just five letters it's really\nnot that hard.\n")

  again = input("Try again with a different word?\nType YES or NO\n").upper()
  if again == "YES":
    print()
    print("Okay, I'll try to go easy on you this time.\n")
    clear()
    print('''_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _

''')
    game()
  else:
    clear()
    print("Thanks for playing! <3\n\nFollow me on Github:\nhttps://github.com/volde-morticia\n\nIf you have any feedback\nlet me know!")

    
# options to either start the game or to view instructions
def options():
  option = input('''
?      -  how to play
start  -  start the game

''').upper()
  print()

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
    option = input("Enter START to start the game.\n\n").upper()

  if option == "START":
    clear()
    print('''_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _

''')
    game()

  if option != "?" and option != "START":
    print("Invalid input. smh.")
    options()

    
# title
print('''
                    _ _     
__ __ _____ _ _ __| | |___ 
\ V  V / _ \ '_/ _` | / -_)
 \_/\_/\___/_| \__,_|_\___|
               
''')
options()


# to add:
# if the letter exists only once, highlight it only once and not twice