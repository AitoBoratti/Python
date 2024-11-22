from turtle import Turtle
from random import choice,uniform
from time import time
SPEED_LIMIT = 2.9
INITIAL_SPEED = 5
class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("Purple")
        self.up()
        self.speed("fastest")
        self.shapesize(0.7)
        self._speed = INITIAL_SPEED
        self.x_move = choice([-self._speed,self._speed])
        self.y_move = choice([-self._speed,self._speed])
        self.acceletarion = 0
        self.last_time_variation = 0


    def move(self):
        new_x = self.xcor() + (self.x_move + self.acceletarion)
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)


    def variation(self):
        variation = uniform(-5, 5)
        self.setheading(self.heading() + variation)


    def bounce(self):
        self.y_move *= -1
        self.variation()
        
    def accelerate(self):
        if self.acceletarion >= 0 and self.acceletarion < SPEED_LIMIT:
            self.acceletarion += .1
        elif self.acceletarion < 0 and self.acceletarion > -SPEED_LIMIT:
            self.acceletarion -= .1

        if self.x_move > 0 and self.acceletarion < 0:
            self.acceletarion *= -1
        elif self.x_move < 0 and self.acceletarion > 0 :
            self.acceletarion *= -1

    def bounce_on_paddle(self):
        if time() - self.last_time_variation > 1:
            self.x_move *= -1
            self.accelerate()
            self.variation()
            self.last_time_variation = time()
            
    def reset(self):
        self.x_move *= -1
        self.y_move = 0 
        self.x_move = 0
        self.acceletarion = 0
        self.home()

    
    def serve(self,side):
        self.y_move = choice([-INITIAL_SPEED,INITIAL_SPEED])
        self.x_move = INITIAL_SPEED  if (side == "right") else -INITIAL_SPEED
        self.variation()