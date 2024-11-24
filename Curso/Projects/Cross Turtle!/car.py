from turtle import Turtle
from random import choice,randint

class Car(Turtle):
    COLORS = ["darkred", "darkblue", "darkgreen", "goldenrod", "saddlebrown", "indigo", "teal", "darkorange", "slateblue", "olive"]   
    STEPS = 2
    ACCELERATION = .5
    def __init__(self, side) -> None:
        super().__init__(shape="square")
        self.shapesize(1.1,3)
        self.up()
        self.color(choice(self.COLORS))
        self.x_limit = -330

        # Logic based on the side
        if side == 1:
            self.aling = 1
            self.teleport_logic = lambda : self.xcor() < self.x_limit
            self.steps = -self.STEPS
        else: 
            self.aling = -1
            self.x_limit *= -1
            self.teleport_logic = lambda : self.xcor() > self.x_limit
            self.steps = self.STEPS


        self.random_teleport()


    def random_teleport(self):
        aling = self.aling
        new_x = (randint(5,14) * 70) * aling
        new_y = (randint(1,9) * 26) * aling
        self.color(choice(self.COLORS))
        self.goto(new_x,new_y)
    

    def move_forward(self):
        self.forward(self.steps)
        if self.teleport_logic():
            self.random_teleport()

    
    def accelerate(self):
        self.steps += self.ACCELERATION if self.steps > 0 else -self.ACCELERATION
    