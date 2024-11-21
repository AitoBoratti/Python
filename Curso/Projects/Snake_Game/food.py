from turtle import Turtle
from random import randint

LIMITS = 14
POS = (50,50)
class Food:
    def __init__(self):
        self.item = Turtle("circle")
        self.item.penup()
        self.item.color("Green")
        self.item.goto(POS)
        self.item.shapesize(0.6,0.6)
        self.teleport()

    def _get_cords(self):
        return((randint(-LIMITS,LIMITS)*20,randint(-LIMITS,LIMITS)*20))
    def teleport(self):
        new_x,new_y = self._get_cords()
        self.item.goto(x=new_x,y=new_y)
    def disappear(self):
        self.item.hideturtle()
    def reset(self):
        self.item.showturtle()
        self.teleport()