from turtle import Turtle
from random import randint,choice
# POSSITIVE_RANGE : -45 .. 45
# POSSITIVE_RANGE : 225 .. -225

SPEED = 8
class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("Purple")
        self.up()
        self.shapesize(0.7)
        self.random_start()
        self.x_move = SPEED
        self.y_move = choice([SPEED,-SPEED])
        # self.random_start()

    def random_start(self):
        angle = randint(-45,45) + choice([0,0,180,-180])
        self.setheading(angle)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def bounce(self):
        self.y_move *= -1
        
    def bounce_on_paddle(self):
        self.x_move *= -1
