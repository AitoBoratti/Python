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

game_is_on = True
timer_id = None
# def restart():
#     global game_is_on,food,snake,score
#     screen.reset()
#     decoration = Screen_Decorator()
#     food = Food()
#     snake = Snake()
#     score = Score()
#     game_is_on = True
#     game_loop()



def adjust_inputs():
    screen.onkey(key="w",fun=snake.up)
    screen.onkey(key="d",fun=snake.right)   
    screen.onkey(key="s",fun=snake.down)
    screen.onkey(key="a",fun=snake.left)
    screen.onkey(key="y",fun=reset)
    screen.onkey(key="r",fun=reset)
    screen.onkey(key="n",fun=screen.bye)


def reset():
    global game_is_on
    game_is_on = True
    
    decoration.draw()
    score.reset()
    food.reset()
    snake.reset()
    game_loop()
    

def snake_eat():
    def _is_snake():
        if snake.check_distance_from_body(food.item):
            return True
        return False
    
    
    snake.grow()
    food.teleport()
    while _is_snake():
        food.teleport()
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
        screen.ontimer(game_loop,snake.speed)
        screen.update()

# screen.onkey(key="w",fun=snake.up)
# screen.onkey(key="d",fun=snake.right)   
# screen.onkey(key="s",fun=snake.down)
# screen.onkey(key="a",fun=snake.left)

"""--------------------"""
# screen.onkey(key="y",fun=reset)
# screen.onkey(key="n",fun=screen.bye)



screen.listen()
game_loop()
adjust_inputs()
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