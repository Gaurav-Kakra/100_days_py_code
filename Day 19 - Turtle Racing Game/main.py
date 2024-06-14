from turtle import Turtle, Screen
import random

is_race_on = False
sc = Screen()
sc.setup(width=500,height=400)
user_bet = sc.textinput(title="What is your bet ?", prompt="Which Turtle will run the race? Pick a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = -70
all_turtles = []

for turtle_index in range(0,6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-230, y=y_pos)
    y_pos = y_pos + 30
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turt in all_turtles:
        if turt.xcor() > 230:
            is_race_on = False
            if turt.pencolor() == user_bet:
                print(f"You have won! The winning turtle is {turt.pencolor()}")
            else:
                print(f"You have lost! The winning turtle is {turt.pencolor()}")
        dist = random.randint(0,10)
        turt.forward(dist)




# def move_forwards():
#     timmy_the_turtle.forward(20)
#
# def move_backwards():
#     timmy_the_turtle.backward(20)
#
# def clear_drawings():
#     timmy_the_turtle.clear()
#     timmy_the_turtle.penup()
#     timmy_the_turtle.home()
#     timmy_the_turtle.pendown()
#
# def turn_left():
#     timmy_the_turtle.left(10)
#
# def turn_right():
#     timmy_the_turtle.right(10)
#
# sc.listen()
# sc.onkey(key="w",fun=move_forwards)
# sc.onkey(key="s",fun=move_backwards)
# sc.onkey(key="c",fun=clear_drawings)
# sc.onkey(key="a",fun=turn_left)
# sc.onkey(key="d",fun=turn_right)
sc.exitonclick()