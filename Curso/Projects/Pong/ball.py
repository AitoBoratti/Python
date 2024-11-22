from turtle import Turtle
from random import choice,uniform
SPEED = 5
class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("Purple")
        self.up()
        self.speed("fastest")
        self.shapesize(0.7)
        self._speed = SPEED
        self.x_move = choice([-SPEED,SPEED])
        self.y_move = choice([-SPEED,SPEED])
        self.can_bounce = True

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)


    def variation(self):
        variation = uniform(-5, 5)
        self.setheading(self.heading() + variation)


    def bounce(self):
        self.y_move *= -1
        self.variation()
        

    def bounce_on_paddle(self):
        if self.can_bounce:
            self.x_move *= -1
            self.variation()
            self.can_bounce = False
            
    def reset(self):
        self.can_bounce = True
        self.bounce_on_paddle()
        self.home()