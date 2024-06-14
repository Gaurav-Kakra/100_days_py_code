#from replit import clear
# HINT: You can call clear() to clear the output in the console.
import art
import os

def clear():
    print("\n" * 100)

print(art.logo)
endgame = True
bido = []
m = 0
count = 0

while endgame:
    bidders = {}
    name = input("What is your name ?")
    bid = int(input("What is your bid ? $"))
    bidders["name"] = name
    bidders["bid"] = bid
    bido.append(bidders)
    choice = input("Are there any other bidders ? Type 'yes' or 'no' ")
    if choice == 'no':
        endgame = False
    clear()

print(bido)
for b in bido:
    for b1 in b:
        if b1 == 'bid':
            if m < b[b1]:
                m = b[b1]
                n = bido[count]['name']
    count += 1

print(m)
print(n)

print(f"The highest bid was of {n} for ${m}.")


