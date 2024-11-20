from turtle import Screen
from snake import Snake
from food import Food
from screen_decorator import Screen_Decorator
from score import Score
import time as t

screen = Screen()
screen.setup(width=640,height=640)
screen.bgcolor("Black")
screen.tracer(0)
score = Score()
decoration = Screen_Decorator()
snake = Snake()
food = Food()


# def restart():
#     global game_is_on,food,snake,score
#     screen.reset()
#     decoration = Screen_Decorator()
#     food = Food()
#     snake = Snake()
#     score = Score()
#     game_is_on = True
#     game_loop()



def snake_eat():
    food.teleport()
    snake.grow()
    score.update_score()


def game_loop():
    global game_is_on
    if game_is_on:
        snake.move()

        if snake.check_distance(food.item):
            snake_eat()
        if snake.check_wall_colission() or snake.check_self_collision():
            game_is_on = False
            snake.disappear()
            food.disappear()
            score.print_end()

        
        screen.update()
        screen.ontimer(game_loop,snake.speed)

screen.listen()
screen.onkey(key="w",fun=snake.up)
screen.onkey(key="d",fun=snake.right)   
screen.onkey(key="s",fun=snake.down)
screen.onkey(key="a",fun=snake.left)
# screen.onkey(key="y",fun=restart)
# screen.onkey(key="n",fun=screen.bye)

game_is_on = True
game_loop()
screen.exitonclick()



# while game_is_on:
#     screen.update()
#     t.sleep(0.1)

#     snake.move()
#     if snake.check_distance(food.item):
#         food.teleport()
#         snake.grow()

#     if snake.check_wall_colission() or snake.check_self_collision():
#         game_is_on = False