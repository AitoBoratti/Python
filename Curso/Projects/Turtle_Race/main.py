import turtle as t
from Turtle_Competitor import Turtle_Competitor
from random import randint

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=1000,height=400)
screen.title("Turtle race!")

def call_bet():
    return screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter a color: ").lower()
def make_final_line():
    pen = t.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.hideturtle()
    pen.up()
    pen.goto(y=-207,x=450)
    pen.down()
    pen.left(90)


    for i in range(int(400/20)):
        if i%2 == 0:
            pen.up()
        else:
            pen.down()
        pen.forward(20)
def create_competitors():
    color_list = ["red", "blue", "green", "yellow", "purple", 
                  "orange", "pink", "grey", "white", "brown"]
    turtles = []


    for i in range(10):
        height =  140 - (i * 30)
        color = color_list[i]
        turtles.append(Turtle_Competitor(height,color))


    return turtles
def reset():
    for turtle  in turtles:
        turtle.reset()
def race():
    winner = None
    while not winner:
        for actual_turtle in turtles:
            actual_turtle.run(randint(10,30))
            if actual_turtle.turtle.xcor() >= 440:
                winner = actual_turtle
                break
    return winner
def check_winner():
    win_bet = None
    if player1_bet == winner.id:
        win_bet = "Player 1"
    elif player2_bet == winner.id:
        win_bet = "Player 2" 
    return win_bet
def final_promt():
    winner_player = check_winner()
    final_promt = f"The winner was the {(winner.id).title()} competitor! "
    final_promt += f"Contratulations! {winner_player} wins! ☺\n" if winner_player else "Better luck next time loosers!\n"
    final_promt += "\t\tYou want another try? Y/N: "
    return final_promt

make_final_line()
turtles=[]
turtles = create_competitors()
one_more = 'y'
while (one_more == 'y'):
    player1_bet = screen.textinput(title="Player 1, Make your bet!",prompt="Which turtle will win the race? Enter a color: ").lower()
    player2_bet = screen.textinput(title="Player 2,Make your bet!",prompt="Which turtle will win the race? Enter a color: ").lower()
    winner = race()

    one_more = screen.textinput(title="The race is over!",prompt=final_promt()).lower()
    if one_more == 'y':
        reset()
