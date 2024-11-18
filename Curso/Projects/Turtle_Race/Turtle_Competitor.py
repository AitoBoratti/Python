import turtle as t

class Turtle_Competitor:
    def __init__(self,ycor,color) -> None:
        self.id = color
        self.DEFAULT_X = -450
        self.DEFAULT_Y = ycor
        self.turtle = t.Turtle("turtle")
        self.turtle.penup()
        self.turtle.color(color)
        self.reset()
    
    def run(self, speed):
        self.turtle.forward(distance=speed)

    def reset(self):
        self.turtle.teleport(self.DEFAULT_X,y=self.DEFAULT_Y )