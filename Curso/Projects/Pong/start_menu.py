from turtle import Turtle

TITLE_FONT  = ("Courier", 24, "bold")
NORMAL_FONT = ("Courier", 16, "bold")

class Menu(Turtle):
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
        self.write(arg="PONG GAME",font=TITLE_FONT,align="center")
        
        
    def make_menu(self):
        self.make_title()
        
        title_margin = 50
        self.goto(x=0,y=-(30 + title_margin))
        self.color("white")
        self.write(arg="1: To play vs IA!",font=NORMAL_FONT,align="center")
        self.goto(x=0,y=-(70 + title_margin))
        self.write(arg="2: Play vs other player!",font=NORMAL_FONT,align="center")
        self.goto(x=0,y=-(110 + title_margin))
        self.write(arg="3: To see a IA vs IA!",font=NORMAL_FONT,align="center")
        
    def hide(self):    
        self.clear()
    
