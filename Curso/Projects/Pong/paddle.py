from turtle import Turtle
DIRECTIONS = {
    "left": (-285,0),
    "right" : (278,0)
}
SPEED = 30
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


    def go_up (self): 
        if not self.ycor() >= 240:
            self.forward(self._speed)

    def go_down (self):
        if not self.ycor() <= -240:
            self.backward(self._speed)