from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    ##Detects the collision with up and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() ##Needs to bounce_y

    ##Detects collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x() ##Needs to bounce_x

    ##Detects the ball passing without hitting paddle right
    if ball.xcor() > 375:
        ball.past_side_walls()
        scoreboard.l_point()

    ##Detects the ball passing without hitting paddle left
    if ball.xcor() < -375:
        ball.past_side_walls()
        scoreboard.r_point()
  



screen.exitonclick()

