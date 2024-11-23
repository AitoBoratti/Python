from turtle import Turtle

class Player(Turtle):
    STEPS = 15
    def __init__(self):
        super().__init__(shape="turtle")
        self.up()
        self.goto(x=0,y=-280)
        self.color("white")
        self.left(90)
        self.shapesize(0.85)

    def move_up(self):
        self.forward(self.STEPS)

    def move_down(self):
        if self.ycor() > -280:
            self.backward(self.STEPS)

    def reset(self):
        self.goto(x=0,y=-280)