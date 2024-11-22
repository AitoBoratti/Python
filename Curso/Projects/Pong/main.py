from turtle import Screen
from screen_decorator import Screen_Decorator
from paddle import Paddle
from ball import Ball
from paddle_ia import Paddle_IA
from score import Score
from random import choice


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

score = Score()

ia1 = None # Paddle_IA(ball=ball,paddle=paddle1,side="left")
ia2 = Paddle_IA(ball=ball,paddle=paddle2,side="right")

screen.listen()
screen.onkeypress(key="w",fun=paddle1.go_up)
screen.onkeypress(key="s",fun=paddle1.go_down)
screen.onkeypress(key="Up",fun=paddle2.go_up)
screen.onkeypress(key="Down",fun=paddle2.go_down)
screen.onkey(fun= lambda x = choice(["right","left"]) :serve(x),key="space")

game_is_on = True


def check_paddle_collision():
    paddle_width = 20
    paddle_height = 110
    ball_radius = 10  # Ajusta según el tamaño real de la pelota

    # Límites de la primera paleta (paddle1)
    paddle1_top = paddle1.ycor() + paddle_height / 2
    paddle1_bottom = paddle1.ycor() - paddle_height / 2
    paddle1_right = paddle1.xcor() + paddle_width / 2
    paddle1_left = paddle1.xcor() - paddle_width / 2
    
    # Límites de la segunda paleta (paddle2)
    paddle2_top = paddle2.ycor() + paddle_height / 2
    paddle2_bottom = paddle2.ycor() - paddle_height / 2
    paddle2_right = paddle2.xcor() + paddle_width / 2
    paddle2_left = paddle2.xcor() - paddle_width / 2

    # Verificar colisión con paddle1
    if (paddle1_bottom <= ball.ycor() <= paddle1_top and
        paddle1_right >= (ball.xcor() - ball_radius) >= paddle1_left):
        return True

    # Verificar colisión con paddle2
    if (paddle2_bottom <= ball.ycor() <= paddle2_top and
        paddle2_left <= (ball.xcor() + ball_radius) <= paddle2_right):
        return True

    return False


def serve(side):
    ball.serve(side)
    screen.onkey(key="space",fun=None)


def game_loop():
    if game_is_on:

        screen.update()
        ball.move()
        ball.can_bounce = True
        
        # ia1.adjust_position()
        ia2.adjust_position()
        
        
        if  (ball.ycor() > 280 or ball.ycor() < -280):
            ball.bounce()
            
        if check_paddle_collision():
            ball.bounce_on_paddle()
            
        if  (ball.xcor() > 300):
            score.increment_left()
            ball.reset()
            if ia2 != None:
                ia2.loose = True
            else:
                screen.onkey(fun= lambda x = "right" :serve(x),key="space")
            
        elif  (ball.xcor() < -300):
            score.increment_right()
            ball.reset()
            if ia1 != None:
                ia1.loose = True
            else:
                screen.onkey(fun= lambda x = "left" :serve(x),key="space")
            
            
        screen.ontimer(game_loop,(10))


ball.reset()
game_loop()
screen.exitonclick()