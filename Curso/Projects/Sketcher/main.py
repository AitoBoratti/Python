from turtle import Turtle, Screen

pen = Turtle()
pen.color("white")
screen = Screen()
screen.bgcolor("black")

def move_forwards():
    pen.forward(10)
def move_backwards():
    pen.backward(10)
def turn_right():
    pen.right(10)
def turn_left():
    pen.left(10)
def clear():
    pen.reset()
    pen.color("white")


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="c", fun=clear)


screen.mainloop()