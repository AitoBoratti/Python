from turtle import Turtle

LINE_LONG = 15
Y = 300
class Screen_Decorator(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.speed("fastest")
        self.color("white")
        self.up()
        self.goto(x=0,y=-Y)
        self.setheading(90.0)
        self.draw_line()

    def draw_line(self):
        for i in range(int(640/LINE_LONG)):
            self.forward(LINE_LONG)
            if i%2 == 0:
                self.down()
            else:
                self.up()