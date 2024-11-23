from turtle import Turtle
from random import randint
from time import sleep


class Paddle(Turtle):
    DIRECTIONS = {
        "left": (-285,0),
        "right" : (278,0)
    }

    def __init__(self,side) -> None:
        super().__init__("square")
        self.up()
        self.setheading(90)
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.goto(self.DIRECTIONS[side])


    def go_up (self, step):
        if not self.ycor() >= 240:
            self.forward(step)


    def go_down (self, step):
        if not self.ycor() <= -240:
            self.backward(step)


# -----------------------------------------------------------------------------------------------------------------


class Paddle_IA():
    # 35 - Normal
    DIFFICULTY = 35
    SPEED = 10
    
    def __init__(self,paddle,ball,side) -> None:
        self.paddle = paddle
        self.ball = ball
        self.side = side
        self.difference = self.SPEED - self.ball._speed
        if side.lower() == "right":
                self.side_logic = lambda : self.ball.xcor() > 0 
        elif side.lower() == "left":    
                self.side_logic = lambda : self.ball.xcor() < 0 
        self.loose = False


    def adjust_position(self):
            if self.side_logic() and randint(1,100) > self.DIFFICULTY:    
                if self.paddle.ycor() < self.ball.ycor()-self.difference:
                    self.paddle.go_up(self.SPEED)
                elif self.paddle.ycor() > self.ball.ycor()+self.difference:
                    self.paddle.go_down(self.SPEED)
            

    def serve(self):
            if self.ball.x_move == 0 and self.loose:
                sleep(1)
                self.ball.serve(self.side)
                self.loose = False