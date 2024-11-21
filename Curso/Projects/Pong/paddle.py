from turtle import Turtle
DIRECTIONS = {
    "left": (-285,0),
    "right" : (278,0)
}

class Paddle(Turtle):
    def __init__(self,side) -> None:
        super().__init__("square")
        self.up()
        self.setheading(90)
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.goto(DIRECTIONS[side])

    def go_up (self):
        if not self.ycor() >= 240:
            self.forward(20)

    def go_down (self):
        if not self.ycor() <= -240:
            self.backward(20)



    #         self.paddle.append(new_part)