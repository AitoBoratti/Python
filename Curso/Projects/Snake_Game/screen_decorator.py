from turtle import Turtle
LIMIT = 285
COMPENSATION = 8

class Screen_Decorator(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.goto(LIMIT, -LIMIT)
        self.pendown()
        self.draw()

    def draw(self):  
        self.goto(LIMIT, LIMIT+COMPENSATION)  
        self.goto(-LIMIT -COMPENSATION, LIMIT+COMPENSATION)  
        self.goto(-LIMIT -COMPENSATION, -LIMIT)  
        self.goto(LIMIT, -LIMIT)  
