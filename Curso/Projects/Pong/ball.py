from turtle import Turtle
from random import randint,choice
# POSSITIVE_RANGE : -45 .. 45
# POSSITIVE_RANGE : 225 .. -225

class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("Purple")
        self.shapesize(0.7)
        self.x_move = 5
        self.y_move = choice([10,-10])
        # self.random_start()

    def random_start(self):
        self.angle = randint(-45,45) + choice([0,0,180,-180])
        print(self.angle)
        self.setheading(self.angle)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def bounce(self):
        self.y_move *= -1