from turtle import Turtle

DIRECTIONS = {
    "left": (-285,0),
    "right" : (278,0)
}
SPEED = 10

class Paddle(Turtle):
    def __init__(self,side) -> None:
        super().__init__("square")
        self.up()
        self.setheading(90)
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.goto(DIRECTIONS[side])
        self.speed(0)
        self._speed = SPEED


    def go_up (self, step = SPEED):
        if not self.ycor() >= 240:
            self.forward(step)

    def go_down (self, step = SPEED):
        if not self.ycor() <= -240:
            self.backward(step)