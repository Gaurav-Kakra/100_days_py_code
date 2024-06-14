import turtle as turtle_module
import random
import colorgram

timmy_the_turtle = turtle_module.Turtle()
timmy_the_turtle.shape("turtle")
turtle_module.colormode(255)

colors = colorgram.extract('image.jpg',25)
rgb_colors = []

for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(rgb_colors)
color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44)]

dot_size = 20
dot_spacing = 50
num_rows = 10
num_columns = 10

timmy_the_turtle.penup()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)

for row in range(10):
    for col in range(10):
        timmy_the_turtle.dot(20,random.choice(color_list))
        timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(90)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(180)
    timmy_the_turtle.forward(500)
    timmy_the_turtle.setheading(0)


##Challenge 1
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

##Challenge 2
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

##Challenge 3
# for _ in range(3,11):
#     timmy_the_turtle.pencolor(random.random(), random.random(), random.random()) ##randomly chosing RGB colors
#     for j in range(_):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/_)

##Challenge 4
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed(0)
# for _ in range(100):
#     angle = random.choice([0, 90, 180, 270])
#     timmy_the_turtle.setheading(angle) ##moving to east, west, north, south
#     timmy_the_turtle.pencolor(random.random(), random.random(), random.random())  ##randomly chosing RGB colors
#     timmy_the_turtle.forward(30)

##Challenge 5
# timmy_the_turtle.speed(0)
# timmy_the_turtle.pensize(2)
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         timmy_the_turtle.pencolor(random.random(), random.random(), random.random())
#         timmy_the_turtle.circle(100)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)
#
# draw_spirograph(5)


sc = turtle_module.Screen()
sc.exitonclick()