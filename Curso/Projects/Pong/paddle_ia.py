class Paddle_IA():
    def __init__(self,paddle,ball) -> None:
        self.paddle = paddle
        self.ball = ball
        self.difference = self.paddle._speed - self.ball._speed

    def adjust_position(self):
        if self.paddle.ycor() < self.ball.ycor()-self.difference:
            self.paddle.go_up()
        elif self.paddle.ycor() > self.ball.ycor()+self.difference:
            self.paddle.go_down()