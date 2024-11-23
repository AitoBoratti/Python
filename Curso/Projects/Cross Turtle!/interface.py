from turtle import Turtle


class Interface(Turtle):
    END_FONT = ("Courier", 26, "normal")
    LEVEL_FONT = ("Courier", 18, "normal")
    def __init__(self):
        super().__init__(visible=False)
        self.color("lightgrey")
        self.up()
        self.goto(-295,265)
        self.level = 1
        self.score_update()


    def score_update(self):
        self.clear()
        self.write(arg=f"Level: {self.level}",font=self.LEVEL_FONT)

    def end_game(self):
        self.clear()
        self.color("white")
        self.goto(0,20)
        self.write(arg="GAME OVER",font=self.END_FONT,align="center")


    def level_up(self):
        self.level += 1
        self.score_update()