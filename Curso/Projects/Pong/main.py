# from turtle import Screen
# from screen_decorator import Screen_Decorator
# from paddle import Paddle
# from ball import Ball
# from paddle_ia import Paddle_IA
# from score import Score
# from start_menu import Menu

# X_LIMIT = 300
# Y_LIMIT = 280
# SCREEN_SIZE = 600

# screen = Screen()
# screen.setup(SCREEN_SIZE, SCREEN_SIZE)
# screen.tracer(0)
# screen.bgcolor("black")
# screen.title("Pong")
# screen.listen()

# # Variables globales
# game_is_on = True
# keys = {"w": False, "s": False, "Up": False, "Down": False}

# score = None
# line = None
# paddle1 = None
# paddle2 = None
# ball = None
# ia1 = None
# ia2 = None
# menu = Menu()


# def adjust_inputs():
#     # Registrar eventos para las teclas de los jugadores
#     screen.onkeypress(lambda: key_down("w"), "w")
#     screen.onkeypress(lambda: key_down("s"), "s")
#     screen.onkeypress(lambda: key_down("Up"), "Up")
#     screen.onkeypress(lambda: key_down("Down"), "Down")
#     screen.onkeyrelease(lambda: key_up("w"), "w")
#     screen.onkeyrelease(lambda: key_up("s"), "s")
#     screen.onkeyrelease(lambda: key_up("Up"), "Up")
#     screen.onkeyrelease(lambda: key_up("Down"), "Down")
#     screen.onkeypress(key="1", fun=None)
#     screen.onkeypress(key="2", fun=None)
#     screen.onkeypress(key="3", fun=None)


# def key_down(key):
#     """Marca una tecla como presionada."""
#     keys[key] = True


# def key_up(key):
#     """Marca una tecla como no presionada."""
#     keys[key] = False


# def start_game(option):
#     global line, paddle1, paddle2, ball, ia1, ia2, score
#     score = Score()
#     line = Screen_Decorator()
#     paddle1 = Paddle("left")
#     paddle2 = Paddle("right")
#     ball = Ball()
#     if option == 1:
#         ia2 = Paddle_IA(ball=ball, paddle=paddle2, side="right")
#     elif option == 3:
#         ia1 = Paddle_IA(ball=ball, paddle=paddle1, side="left")
#         ia2 = Paddle_IA(ball=ball, paddle=paddle2, side="right")
#     menu.hide()
#     adjust_inputs()
#     game_loop()


# def check_paddle_collision():
#     paddle_width = 20
#     paddle_height = 110
#     ball_radius = 10  # Ajusta según el tamaño real de la pelota

#     # Límites de la primera paleta (paddle1)
#     paddle1_top = paddle1.ycor() + paddle_height / 2
#     paddle1_bottom = paddle1.ycor() - paddle_height / 2
#     paddle1_right = paddle1.xcor() + paddle_width / 2
#     paddle1_left = paddle1.xcor() - paddle_width / 2

#     # Límites de la segunda paleta (paddle2)
#     paddle2_top = paddle2.ycor() + paddle_height / 2
#     paddle2_bottom = paddle2.ycor() - paddle_height / 2
#     paddle2_right = paddle2.xcor() + paddle_width / 2
#     paddle2_left = paddle2.xcor() - paddle_width / 2

#     # Verificar colisión con paddle1
#     if (paddle1_bottom <= ball.ycor() <= paddle1_top and
#             paddle1_right >= (ball.xcor() - ball_radius) >= paddle1_left):
#         return True

#     # Verificar colisión con paddle2
#     if (paddle2_bottom <= ball.ycor() <= paddle2_top and
#             paddle2_left <= (ball.xcor() + ball_radius) <= paddle2_right):
#         return True

#     return False


# def serve(side):
#     ball.serve(side)
#     screen.onkey(key="space", fun=None)


# def game_loop():
#     global game_is_on

#     if game_is_on:
#         screen.update()
#         ball.move()

#         # Movimiento de las IA, si están activas
#         if ia1 is not None:
#             ia1.adjust_position()
#         if ia2 is not None:
#             ia2.adjust_position()

#         # Movimiento de los jugadores
#         if keys["w"]:
#             paddle1.go_up(10)
#         if keys["s"]:
#             paddle1.go_down(10)
#         if keys["Up"]:
#             paddle2.go_up(10)
#         if keys["Down"]:
#             paddle2.go_down(10)

#         # Rebote en los límites
#         if ball.ycor() > Y_LIMIT or ball.ycor() < -Y_LIMIT:
#             ball.bounce()

#         # Colisiones con las paletas
#         if check_paddle_collision():
#             ball.bounce_on_paddle()

#         # Puntos anotados
#         if ball.xcor() > X_LIMIT:
#             score.increment_left()
#             ball.reset()
#             if ia2 is not None:
#                 ia2.loose = True
#             else:
#                 screen.onkey(fun=lambda x="right": serve(x), key="space")

#         elif ball.xcor() < -X_LIMIT:
#             score.increment_right()
#             ball.reset()
#             if ia1 is not None:
#                 ia1.loose = True
#             else:
#                 screen.onkey(fun=lambda x="left": serve(x), key="space")

#         # Repetir el bucle después de 10 ms
#         screen.ontimer(game_loop, 10)


# screen.listen()
# screen.onkeypress(key="1", fun=lambda x=1: start_game(x))
# screen.onkeypress(key="2", fun=lambda x=2: start_game(x))
# screen.onkeypress(key="3", fun=lambda x=3: start_game(x))
# screen.onkeypress(key="Escape", fun=screen.bye)

# screen.exitonclick()





from turtle import Screen
from screen_decorator import Screen_Decorator
from paddle import Paddle
from ball import Ball
from paddle_ia import Paddle_IA
from score import Score
from random import choice
from start_menu import Menu


X_LIMIT = 300
Y_LIMIT = 280
SCREEN_SIZE = 600

screen = Screen()
screen.setup(SCREEN_SIZE,SCREEN_SIZE)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
game_is_on = True


keys = {"w" : False, "s" : False, "Up" : False, "Down": False}

score = None
line = None
paddle1 = None
paddle2 = None
ball = None
ia1 = None
ia2 = None
menu = Menu()


def key_up(key):
    keys[key]=False
def key_down(key):
    keys[key]=True
    



def adjust_inputs():
    screen.onkeypress(key="w",fun=lambda x="w":key_down(x))
    screen.onkeypress(key="s",fun=lambda x="s":key_down(x))
    screen.onkeypress(key="Up",fun=lambda x="Up":key_down(x))
    screen.onkeypress(key="Down",fun=lambda x="Down":key_down(x))
    
    screen.onkeyrelease(key="w",fun=lambda x="w":key_up(x))
    screen.onkeyrelease(key="s",fun=lambda x="s":key_up(x))
    screen.onkeyrelease(key="Up",fun=lambda x="Up":key_up(x))
    screen.onkeyrelease(key="Down",fun=lambda x="Down":key_up(x))
    
    
    screen.onkeypress(key=1,fun= None)
    screen.onkeypress(key=2,fun= None)
    screen.onkeypress(key=3,fun= None)
    
def start_game(option):
    global line,paddle1,paddle2,ball,ia1,ia2,score
    score = Score()
    line = Screen_Decorator()
    paddle1 = Paddle("left")
    paddle2 = Paddle("right")
    ball = Ball()
    if option == 1:
        ia2 = Paddle_IA(ball=ball,paddle=paddle2,side="right")
    elif option == 3:
        ia1 = Paddle_IA(ball=ball,paddle=paddle1,side="left")
        ia2 = Paddle_IA(ball=ball,paddle=paddle2,side="right")
    menu.hide()
    adjust_inputs()
    game_loop()


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
        
        if ia1 is not None: 
            ia1.adjust_position()
        
        if ia2 is not None:
            ia2.adjust_position()
        
        
        
        if keys["w"]:
            paddle1.go_up(7)
        if keys["s"]:
            paddle1.go_down(7)
        if keys["Up"]:
            paddle2.go_up(7)
        if keys["Down"]:
            paddle2.go_down(7)
        
        
        
        
        if  (ball.ycor() > Y_LIMIT or ball.ycor() < -Y_LIMIT):
            ball.bounce()
            
        if check_paddle_collision():
            ball.bounce_on_paddle()
            
        if  (ball.xcor() > X_LIMIT):
            score.increment_left()
            ball.reset()
            if ia2 != None:
                ia2.loose = True
            else:
                screen.onkey(fun= lambda x = "right" :serve(x),key="space")
            
        elif  (ball.xcor() < -X_LIMIT):
            score.increment_right()
            ball.reset()
            if ia1 != None:
                ia1.loose = True
            else:
                screen.onkey(fun= lambda x = "left" :serve(x),key="space")
            
            
        screen.ontimer(game_loop,(10))


screen.listen()
screen.onkeypress(key="1",fun=lambda x=1 :start_game(x))
screen.onkeypress(key="2",fun=lambda x=2 :start_game(x))
screen.onkeypress(key="3",fun=lambda x=3 :start_game(x))
screen.onkeypress(key="Escape",fun=screen.bye)

screen.exitonclick()