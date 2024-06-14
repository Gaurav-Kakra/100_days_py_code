from game_data import data
import random
from art import *
#from replit import clear

print(logo)

l = []  # creating a empty list to compare the followers count
g = []  # creting a empty list to store the latest entry if the prediction is right
score = 0  # creating a variable to store the scores
start = 0  # creating a variable to compare the list l
counter = 0  # creating a variable to print the logo in the for loop

def clear():
    print("\n" * 100)

def selector():
    """"Creating the function to randomly select from game data"""
    r = random.randint(0, 49)
    return data[r]


# creating for loop to iterate the first two entries
for j in range(0, 2):
    s1 = selector()
    g.append(s1)
    # print(g)
    for i in s1:
        if i != "follower_count":
            print(f"{i}: {s1[i]}")
        else:
            l.append(s1[i])
    if counter == 0:
        print(vs)
        counter = counter + 1


def reselect_random_data():
    """"This function helps select a random new data from game data"""
    s2 = selector()
    g.append(s2)
    for i in s2:
        if i != "follower_count":
            print(f"{i}: {s2[i]}")
        else:
            l.append(s2[i])


def high_low():
    """This function performs the evaluation of the prediction of followers"""
    global score
    sel = input("\nWho has more followers ? Choose 'a' or 'b'")
    if l[start] > l[start + 1] and sel == "b":
        return f"You lost ! Your final score is {score}"
    elif l[start] < l[start + 1] and sel == "a":
        return f"You lost ! Your final score is {score}"
    elif l[start] > l[start + 1] and sel == "a":
        clear()
        score = score + 1
        l.remove(l[start + 1])
        g.remove(g[start + 1])
        for i in g[0]:
            a = g[0]
            if i != "follower_count":
                print(f"{i}: {a[i]}")
        print(vs)
        reselect_random_data()
        return high_low()
    elif l[start] < l[start + 1] and sel == "b":
        clear()
        score = score + 1
        l.remove(l[start])
        g.remove(g[start])
        for i in g[0]:
            a = g[0]
            if i != "follower_count":
                print(f"{i}: {a[i]}")
        print(vs)
        reselect_random_data()
        return high_low()


print(high_low())

