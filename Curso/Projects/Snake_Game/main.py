from turtle import Screen
from snake import Snake
from food import Food
from screen_decorator import Screen_Decorator
from score import Score

SCREEN_SIZE = 640
BACKGROUND_COLOR = "Black"

class Game():

    def __init__(self):    
        self.screen = Screen()
        self.adjust_screen()
        self.score = Score()
        self.decoration = Screen_Decorator()
        self.snake = Snake()
        self.food = Food()
        self.game_is_on = True


    def adjust_screen(self):
        self.screen.setup(width=SCREEN_SIZE,height=SCREEN_SIZE)
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.tracer(0)

        
    def adjust_inputs(self):
        self.screen.onkey(key="w",fun=self.snake.up)
        self.screen.onkey(key="d",fun=self.snake.right)   
        self.screen.onkey(key="s",fun=self.snake.down)
        self.screen.onkey(key="a",fun=self.snake.left)
        self.screen.onkey(key="r",fun=None)
        self.screen.onkey(key="Escape",fun=self.screen.bye)


    def reset(self):
        self.game_is_on = True
        self.decoration.draw()
        self.score.reset()
        self.food.reset()
        self.snake.reset()
        self.screen.onkey(key="r",fun=None)
        self.game_loop()
        

    def snake_eat(self):
        def _is_snake(self):
            if self.snake.check_distance_from_body(self.food.item):
                return True
            return False
        
        self.snake.grow()
        self.food.teleport()
        while _is_snake(self):
            self.food.teleport()
        self.score.update_score()


    def game_loop(self):
        if self.game_is_on:
            self.snake.move()

            if self.snake.check_distance(self.food.item):
                self.snake_eat()
            if self.snake.check_wall_colission() or self.snake.check_self_collision():
                self.game_is_on = False
                self.snake.disappear()
                self.food.disappear()
                self.screen.onkey(key="r",fun=self.reset)
                self.score.print_end()
            self.screen.ontimer(self.game_loop,self.snake.speed)
            self.screen.update()


    def start(self):
        self.screen.listen()
        self.adjust_inputs()
        self.game_loop()
        self.screen.exitonclick()


if __name__ == "__main__":
    game = Game()
    game.start()