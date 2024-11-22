from random import randint
from time import sleep

"""75 seems like a fair difficulty"""
DIFFICULTY = 75
class Paddle_IA():
    def __init__(self,paddle,ball,side) -> None:


        self.paddle = paddle
        self.ball = ball
        self.side = side
        self.difference = self.paddle._speed - self.ball._speed
        if side.lower() == "right":
                self.side_logic = lambda : self.ball.xcor() > 0 
        elif side.lower() == "left":    
                self.side_logic = lambda : self.ball.xcor() < 0 
        self.loose = False

    def adjust_position(self):
            
            if self.side_logic() and randint(1,100) > DIFFICULTY:    
                if self.paddle.ycor() < self.ball.ycor()-self.difference:
                    self.paddle.go_up()
                elif self.paddle.ycor() > self.ball.ycor()+self.difference:
                    self.paddle.go_down()
            

            if self.ball.x_move == 0 and self.loose:
                sleep(1)
                self.ball.serve(self.side)
                self.loose = False