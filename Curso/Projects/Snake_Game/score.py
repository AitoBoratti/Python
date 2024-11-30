from turtle import Turtle

class Score(Turtle):
    POS = (0,295)
    SCORE_FONT = ("Arial", 16, "normal")
    ALIGNMENT = "center"
    SCORE_FILE = "data\high_score.txt"
    
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.penup()
        self.color("white")
        self.score = 0
        with open (self.SCORE_FILE,mode="r") as max_score:
            self.high_score = int(max_score.read())
        self.print_score()


    def print_score(self):
        self.clear()
        self.goto(self.POS)
        text = f" SCORE:  {self.score}\t\tHIGHER SCORE: {self.high_score}  "
        self.write(arg=text,align=self.ALIGNMENT,font=self.SCORE_FONT)
    
    def update_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.SCORE_FILE,mode="w") as max_score:
                max_score.write(f"{self.score}")
        
        self.print_score()

    def print_end(self):
        self.clear()
        self.home()
        text = f" ¡Game Over!\n\nFinal score: {self.score}.\n"
        text2 = "Press R to restart, or Esc to close."
        self.write(arg=text,align=self.ALIGNMENT,font=self.SCORE_FONT)
        self.write(arg=text2,align=self.ALIGNMENT,font=self.SCORE_FONT)
    
    def reset(self):
        self.score = -1
        self.update_score()
