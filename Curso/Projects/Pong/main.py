from turtle import Screen, Turtle
from screen_decorator import Screen_Decorator
from paddle import Paddle
from ball import Ball
import time as t
screen = Screen()
screen.setup(600,600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
line = Screen_Decorator()

paddle1 = Paddle("left")
paddle2 = Paddle("right")
ball = Ball()

screen.listen()
screen.onkeypress(key="w",fun=paddle1.go_up)
screen.onkeypress(key="s",fun=paddle1.go_down)
screen.onkeypress(key="Up",fun=paddle2.go_up)
screen.onkeypress(key="Down",fun=paddle2.go_down)
screen.onkeypress(key="a",fun=ball.move)
screen.onkeypress(key="d",fun=ball.bounce)

game_is_on = True
while game_is_on:
    t.sleep(0.055)
    screen.update()
    ball.move()

    if  (ball.ycor() > 270 or ball.ycor() < -270):
        ball.bounce()
    print(f"Print Paddle1: Distance: {ball.distance(paddle1)}")
    print(f"Print Paddle2: Distance: {ball.distance(paddle2)}")
    if ball.distance(paddle1) < 3 or ball.distance(paddle2) < 3:
        ball.bounce()
screen.exitonclick()