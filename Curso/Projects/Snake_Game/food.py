from turtle import Turtle
from random import randint

LIMITS = 14
class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("Green")
        self.shapesize(0.6,0.6)
        self.teleport()

    def _get_cords(self):
        return((randint(-LIMITS,LIMITS)*20,randint(-LIMITS,LIMITS)*20))
    
    
    def teleport(self):
        new_x,new_y = self._get_cords()
        self.goto(x=new_x,y=new_y)


    def disappear(self):
        self.hideturtle()
    def reset(self):
        self.showturtle()
        self.teleport()