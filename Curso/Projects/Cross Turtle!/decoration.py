from turtle import Turtle

class Decoration(Turtle):
    SIDEWALK_LEN = 10

    def __init__(self) -> None:
        super().__init__(visible=False)
        self.color("lightgrey")
        self.up()
        self.make_sidewalk()
        self.make_middle_line()


    def make_sidewalk(self):
        
        new_x = -300
        new_y = -250
        for _ in range(2):
            self.goto(x=new_x,y=new_y)
            for i in range(int(600/self.SIDEWALK_LEN)):
                if i % 2 == 0:
                    self.down()
                else: 
                    self.up()
                self.forward(self.SIDEWALK_LEN)
            new_y *= -1

    def make_middle_line(self):
        
        self.pensize(5)
        self.goto(x=-293,y=0)
        for i in range(int(600/20)):
            if i % 2 == 0:
                self.down()
            else: 
                self.up()
            self.forward(20)