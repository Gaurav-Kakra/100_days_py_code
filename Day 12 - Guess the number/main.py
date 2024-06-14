import random
from art import logo
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
number = random.randint(1,100)
#print(number)

print("Welcome to number guessing game !")
tries = input("Do you want to play easy or hard level ?")
if tries == "easy":
  i = 10
else:
  i = 5

def guess_game():
  print(logo)
  if tries == "easy":
    for j in range(0,i):
      guess = int(input("Guess the number: "))
      if guess == number:
        return(f"You have guessed it right. The number is {number} and you took {j+1} guesses")
      else:
        if guess > number:
          print(f"{guess} it too high and you have {i-j-1} guesses left")
        else:
          print(f"{guess} is too low and you have {i-j-1} guesses left")
    return(f"You have exhauseted your guesses, the number was {number}")
  elif tries == "hard":
    for j in range(0,i):
      guess = int(input("Guess the number: "))
      if guess == number:
        return(f"You have guessed it right. The number is {number} and you took {j+1} guesses")
        break
      else:
        if guess > number:
          print(f"{guess} it too high and you have {i-j-1} guesses left")
        else:
          print(f"{guess} is too low and you have {i-j-1} guesses left")
    return(f"You have exhauseted your guesses, the number was {number}")

print(guess_game())