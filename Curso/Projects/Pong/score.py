from turtle import Turtle

SCORE_FONT = ("Arial", 16, "normal")
ALIGNMENT = "center"
POSITIONS = [(-150,260),(150,260)]

class Score():
    def __init__(self) -> None:
        self.left_side = Turtle(visible=False)
        self.right_side = Turtle(visible=False)
        self.scores = [self.left_side,self.right_side]
        self.left_score = 0
        self.right_score = 0
        for i in range(len(self.scores)):  
            self.scores[i].up()
            self.scores[i].color("white")
            self.scores[i].goto(POSITIONS[i])
            self.scores[i].write(arg="SCORE: 0",font=SCORE_FONT,align=ALIGNMENT)
            
    def increment_left(self):
        self.left_side.clear()
        self.left_score += 1
        self.left_side.write(arg=f"SCORE: {self.left_score}",font=SCORE_FONT,align=ALIGNMENT)
    
    def increment_right(self):
        self.right_side.clear()
        self.right_score += 1
        self.right_side.write(arg=f"SCORE: {self.right_score}",font=SCORE_FONT,align=ALIGNMENT)