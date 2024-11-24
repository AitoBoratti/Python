from turtle import Turtle

POS = (0,295)
SCORE_FONT = ("Arial", 16, "normal")
ALIGNMENT = "center"
class Score(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.penup()
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.print_score()


    def print_score(self):
        self.clear()
        self.goto(POS)
        text = f" SCORE:  {self.score}\t\tHIGHER SCORE: {self.high_score}  "
        self.write(arg=text,align=ALIGNMENT,font=SCORE_FONT)
    
    def update_score(self):
        self.score += 1
        self.print_score()

    def print_end(self):
        self.clear()
        self.home()
        text = f" ¡Game Over!\n\nFinal score: {self.score}.\n"
        text2 = "Press R to restart, or Esc to close."
        self.write(arg=text,align=ALIGNMENT,font=SCORE_FONT)
        self.write(arg=text2,align=ALIGNMENT,font=SCORE_FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score



        self.score = -1
        self.update_score()
