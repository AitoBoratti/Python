from turtle import Turtle

POS = (0,295)
SCORE_FONT = ("Arial", 16, "normal")
class Score:
    def __init__(self) -> None:
        self.item = Turtle(visible=False)
        self.item.penup()
        self.item.color("white")
        self.score = 0
        self.print_score()
    
    def print_score(self):
        self.item.clear()
        self.item.goto(POS)
        text = f"SCORE: {self.score}"
        self.item.write(arg=text,align="center",font=SCORE_FONT)
    
    def update_score(self):
        self.score += 1
        self.print_score()

    def print_end(self):
        self.item.clear()
        self.item.home()
        text = f" ¡Game Over!\n\nFinal score: {self.score}.\n"
        text2 = "Press R to restart, or Esc to close."
        self.item.write(arg=text,align="center",font=SCORE_FONT)
        self.item.write(arg=text2,align="center",font=SCORE_FONT)
    
    def reset(self):
        self.score = -1
        self.update_score()
