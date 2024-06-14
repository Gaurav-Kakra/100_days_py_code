rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

i = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

c = random.randint(0, 2)

if i == 0 and c == 1:
    print(rock)
    print("\n")
    print("Computer chose: ")
    print("\n")
    print(paper)
    print("\n")
    print("You lose")
elif i == 1 and c == 2:
    print(paper)
    print("\n")
    print("Computer chose: ")
    print("\n")
    print(scissors)
    print("\n")
    print("You lose")
elif i == 2 and c == 0:
    print(scissors)
    print("\n")
    print("Computer chose: ")
    print("\n")
    print(rock)
    print("\n")
    print("You lose")
elif i == 1 and c == 0:
    print(paper)
    print("\n")
    print("Computer chose: ")
    print("\n")
    print(rock)
    print("\n")
    print("You win")
elif i == 2 and c == 1:
    print(scissors)
    print("\n")
    print("Computer chose: ")
    print("\n")
    print(paper)
    print("\n")
    print("You win")
elif i == 0 and c == 2:
    print(rock)
    print("\n")
    print("Computer chose: ")
    print("\n")
    print(scissors)
    print("\n")
    print("You win")
elif i == c:
    if i == 0:
        print(rock)
        print("\n")
        print("Computer chose: ")
        print("\n")
        print(rock)
        print("\n")
        print("It is a draw")
    elif i == 1:
        print(paper)
        print("\n")
        print("Computer chose: ")
        print("\n")
        print(paper)
        print("\n")
        print("It is a draw")
    elif i == 2:
        print(scissors)
        print("\n")
        print("Computer chose: ")
        print("\n")
        print(scissors)
        print("\n")
        print("It is a draw")


else:
    print("You chose an invalid number, you lose !")