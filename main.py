from random import randint
from time import sleep
from os import system
import sys

# Function to clear console window
def clear():
  if sys.platform != "win32":
    system("clear")
  else:
    system("cls")

def main():
  print("Number Guessing Game by Talin Sharma talinsharma.dev@gmail.com")

  # Declare constants
  MIN_NUMBER = randint(1, 1000)
  MAX_NUMBER = randint(MIN_NUMBER, 1000)
  SECRET_NUMBER = randint(MIN_NUMBER, MAX_NUMBER)
  NUMBER_OF_GUESSES = randint(5, 15)

  # Start Game
  sleep(1)
  clear()
  print("I have thought of a number between {} and {}. You have {} guesses to guess the number.\n\nGood Luck!".format(MIN_NUMBER, MAX_NUMBER, NUMBER_OF_GUESSES))  
  sleep(1.5)

  # Ask for guess number 1
  guessCount = 1
  guess = int(input("Guess {}: ".format(guessCount)))
  
  while guess != SECRET_NUMBER: # Keep asking until guess is correct. Increment number of guesses.
    guessCount += 1

    if guessCount > NUMBER_OF_GUESSES: # End game if you ran out of guesses
      print("You ran out of guesses. The secret number was {}.".format(SECRET_NUMBER))
      exit()

    if guess < SECRET_NUMBER: # If guess less than number, tell player
      print("Your guess it too low. Try again!\n")
    else: # If guess is more than number, tell player
      print("Your guess is too high. Try again!\n")
    guess = int(input("Guess {}: ".format(guessCount)))

  # Inform player of correct guess.
  clear()
  print("Yay!\nYou guessed correctly! The secret number was {}. It took you {}/{} guesses to figure it out!".format(SECRET_NUMBER, guessCount, NUMBER_OF_GUESSES))
  sleep(2)

main()