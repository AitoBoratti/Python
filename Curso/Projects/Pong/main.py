from turtle import Screen, Turtle
from screen_decorator import Screen_Decorator
from paddle import Paddle
from ball import Ball
from paddle_ia import Paddle_IA
from score import Score

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

ia = Paddle_IA(ball=ball,paddle=paddle2)
ia2 = Paddle_IA(ball=ball,paddle=paddle1)

screen.listen()
screen.onkeypress(key="w",fun=paddle1.go_up)
screen.onkeypress(key="s",fun=paddle1.go_down)
screen.onkeypress(key="Up",fun=paddle2.go_up)
screen.onkeypress(key="Down",fun=paddle2.go_down)

game_is_on = True


def check_paddle_collision():
    paddle_width = 20
    paddle_height = 100
    ball_radius = 7  # Ajusta según el tamaño real de la pelota

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


def game_loop():
    if game_is_on:
        screen.update()
        ball.move()
        
        
        # ia.adjust_position()
        # ia2.adjust_position()
        
        
        if  (ball.ycor() > 270 or ball.ycor() < -270):
            ball.bounce()
            
        if check_paddle_collision():
            ball.bounce_on_paddle()
            ball.can_bounce = True
            
        if  (ball.xcor() > 300):
            score.increment_left()
            ball.reset()
            
        if  (ball.xcor() < -300):
            score.increment_right()
            ball.reset()
            
            
        screen.ontimer(game_loop,(10))


game_loop()
screen.exitonclick()