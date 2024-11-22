from turtle import Screen, Turtle
from screen_decorator import Screen_Decorator
from paddle import Paddle
from ball import Ball
from paddle_ia import Paddle_IA
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

ia = Paddle_IA(ball=ball,paddle=paddle2)
ia2 = Paddle_IA(ball=ball,paddle=paddle1)

screen.listen()
screen.onkeypress(key="w",fun=paddle1.go_up)
screen.onkeypress(key="s",fun=paddle1.go_down)
screen.onkeypress(key="Up",fun=paddle2.go_up)
screen.onkeypress(key="Down",fun=paddle2.go_down)


def check_paddle_collision():
    correction = 60
    x_compensation = 5
    paddle_hitbox = 25
    if ((ball.distance(y=paddle1.ycor()             ,x=paddle1.xcor()+x_compensation)  < paddle_hitbox) or  
        (ball.distance(y=paddle1.ycor() +correction ,x=paddle1.xcor()+x_compensation)  < paddle_hitbox) or
        (ball.distance(y=paddle1.ycor() -correction ,x=paddle1.xcor()+x_compensation)  < paddle_hitbox) or
        (ball.distance(y=paddle2.ycor()             ,x=paddle2.xcor()-x_compensation)  < paddle_hitbox) or
        (ball.distance(y=paddle2.ycor() +correction ,x=paddle2.xcor()-x_compensation)  < paddle_hitbox) or
        (ball.distance(y=paddle2.ycor() -correction ,x=paddle2.xcor()-x_compensation)  < paddle_hitbox)):
        return True
    return False

game_is_on = True
def game_loop():
    if game_is_on:
        screen.update()
        ball.move()
        ia.adjust_position()
        ia2.adjust_position()
        if  (ball.ycor() > 270 or ball.ycor() < -270):
            ball.bounce()
        if check_paddle_collision():
            ball.bounce_on_paddle()
            ball.can_bounce = True
    screen.ontimer(game_loop,(10))


game_loop()
screen.exitonclick()