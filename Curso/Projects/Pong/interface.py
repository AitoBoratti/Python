from turtle import Turtle

class Menu(Turtle):
    TITLE_FONT  = ("Courier", 30, "bold")
    NORMAL_FONT = ("Courier", 18, "normal")
    TITLE_MARGIN = 40
    
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.up()
        self.color("white")
        self.make_menu()
        
        
    def make_title(self):
        self.goto(x=-150,y=165)
        self.fillcolor("white")
        self.begin_fill()
        for _ in range(2):
            self.forward(300)  # Ancho
            self.right(90)
            self.forward(120)  # Largo
            self.right(90)
        self.end_fill()
        self.color("black")
        self.goto(x=0,y=80)
        self.write(arg="PONG GAME",font=self.TITLE_FONT,align="center")
        
        
    def make_menu(self):
        self.make_title()
        
        self.goto(x=0,y=-(30 + self.TITLE_MARGIN))
        self.color("white")
        self.write(arg="1: To play vs IA!",font=self.NORMAL_FONT,align="center")
        self.goto(x=0,y=-(80 + self.TITLE_MARGIN))
        self.write(arg="2: To play vs other player!",font=self.NORMAL_FONT,align="center")
        self.goto(x=0,y=-(130 + self.TITLE_MARGIN))
        self.write(arg="3: To see a IA vs IA!",font=self.NORMAL_FONT,align="center")
        
    def hide(self):    
        self.clear()
    

# -----------------------------------------------------------------------------------------------------------------


class Score():
    SCORE_FONT = ("Courier", 18, "normal")
    ALIGNMENT = "center"
    POSITIONS = [(-150,260),(150,260)]
    TEXT = "Score:"
    
    def __init__(self) -> None:
        self.left_side = Turtle(visible=False)
        self.right_side = Turtle(visible=False)
        self.scores = [self.left_side,self.right_side]
        self.left_score = 0
        self.right_score = 0
        for i in range(len(self.scores)):  
            self.scores[i].up()
            self.scores[i].color("white")
            self.scores[i].goto(self.POSITIONS[i])
            self.scores[i].write(arg=f"{self.TEXT}0",font=self.SCORE_FONT,align=self.ALIGNMENT)
            
    def increment_left(self):
        self.left_side.clear()
        self.left_score += 1
        self.left_side.write(arg=f"{self.TEXT}{self.left_score}",font=self.SCORE_FONT,align=self.ALIGNMENT)
    
    def increment_right(self):
        self.right_side.clear()
        self.right_score += 1
        self.right_side.write(arg=f"{self.TEXT}{self.right_score}",font=self.SCORE_FONT,align=self.ALIGNMENT)


# -----------------------------------------------------------------------------------------------------------------


class Line(Turtle):
    SEGMENT_LENGTH = 15
    
    def __init__(self):
        super().__init__(visible=False)
        self.speed("fastest")
        self.color("white")
        self.up()
        self.goto(x=0,y=-300)
        self.setheading(90.0)
        self.draw_line()

    def draw_line(self):
        for i in range(int(640/self.SEGMENT_LENGTH)):
            self.forward(self.SEGMENT_LENGTH)
            if i%2 == 0:
                self.down()
            else:
                self.up()


