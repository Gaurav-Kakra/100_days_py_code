print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

#door_input = input("You waited and somebody took you to the island with their boat. There are three doors, 'red','yellow','green'. Which door do you want to open ?").lower()

left_right_input = input("You are in the cross road ? Where do you want to go ? Type 'left' or 'right'").lower()
if left_right_input == 'right':
    print('Game Over ! The road led to forest where you were bitten by venomous snake')
else:
    swim_wait_input = input("You have a river in front of you ? Do you want to 'wait' or 'swim' ?").lower()
    if swim_wait_input == 'swim':
        print('Game Over ! You were eaten by hungry crocodiles')
    else:
        door_input = input("You waited and somebody took you to the island with their boat. There are three doors, 'red','yellow','green'. Which door do you want to open ?").lower()
        if door_input == 'red':
            print('Game Over ! You were burnt due to fire')
        elif door_input == 'yellow':
            print('Game Over ! You got lost in the desert')
        else:
            print('Congratulations ! You have found the treasure, enjoy')