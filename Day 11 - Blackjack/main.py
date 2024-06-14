import random
from art import logo
#from replit import clear
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

def clear():
    print("\n" * 100)

def blackjack():
    print(logo)
    cards = ["l1", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    computer = []
    user = []
    blackjack_computer = 0
    blackjack_user = 0
    computer_sum = 0
    user_sum = 0
    l = 2
    j = 2

    #for c in cards[i:]:
    #  print(c)

    for i in range(0, 2):
        computer.append(cards[random.randint(0, len(cards) - 1)])
        user.append(cards[random.randint(0, len(cards) - 1)])

    for c in computer:
        if c == "l1":
            c = 11
        blackjack_computer = c + blackjack_computer

    for c in user:
        if c == "l1":
            c = 11
        blackjack_user = c + blackjack_user

    if blackjack_computer == 22:
        blackjack_computer = 12
        computer[1] = 1
    if blackjack_user == 22:
        blackjack_user = 12
        user[1] = 1

    print(computer[0])
    print(user)

    if blackjack_computer == 21 and blackjack_user == 21:
        return (f"Computer has blackjack {computer}, computer won !")
    elif blackjack_computer == 21:
        return (f"Computer has blackjack {computer}, computer won !")
    elif blackjack_user == 21:
        return (f"You had blackjack {user}, you won !")

    for c in computer:
        if c == "l1":
            c = 11
        computer_sum = c + computer_sum

    for c in user:
        if c == "l1":
            c = 11
        user_sum = c + user_sum

    trigger = input(
        "Do you want to pick a card 'y' or do you want to hold 'n' ?")

    while trigger == 'y' and user_sum < 21:
        user.append(cards[random.randint(0, len(cards) - 1)])
        print(user)
        for c in user[j:]:
            if c == 'l1' and user_sum > 10:
                c = 1
            elif c == 'l1' and user_sum <= 10:
                c = 11
            user_sum = c + user_sum
            if user_sum > 21:
                return (
                    f"You went over 21 i.e. {user_sum} with {user} cards, you lost !"
                )
            elif user_sum == 21:
                return (
                    f"You got blackjack i.e. {user_sum} with {user} cards, you won !"
                )
            j = j + 1
            trigger = input(
                "Do you want to pick a card 'y' or do you want to hold 'n' ?")

    while trigger == 'n' and computer_sum < 16:
        computer.append(cards[random.randint(0, len(cards) - 1)])
        for c in computer[l:]:
            if c == 'l1' and computer_sum > 10:
                c = 1
            elif c == 'l1' and computer_sum <= 10:
                c = 11
            computer_sum = c + computer_sum
            if computer_sum > 21:
                return (
                    f"Computer went over 21 i.e. {computer_sum} with {computer} cards, you won !"
                )
            elif computer_sum == 21:
                return (
                    f"Computer got blackjack i.e. {computer_sum} with {computer} cards, computer won !"
                )
            l = l + 1

    if computer_sum > user_sum and computer_sum < 21 and user_sum < 21:
        return (
            f"Computer got {computer_sum} for {computer} and you got {user_sum} for {user}, computer won !"
        )
    elif computer_sum < user_sum and computer_sum < 21 and user_sum < 21:
        return (
            f"Computer got {computer_sum} for {computer} and you got {user_sum} for {user}, you won !"
        )
    elif computer_sum == user_sum and computer_sum < 21 and user_sum < 21:
        return (
            f"Computer got {computer_sum} for {computer} and you got {user_sum} for {user}, there is draw !"
        )


while input("Do you want to play a game of blackjack? 'yes' or 'no':" ) == "yes":
  clear()
  print(blackjack())


