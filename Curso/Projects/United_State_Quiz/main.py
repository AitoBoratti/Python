from turtle import Screen, Turtle
import pandas

FONT = ("Arial",8,"normal")
screen = Screen()
screen.setup(725,491)
screen.bgpic("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
pointer = Turtle(visible=False)
pointer.penup()
pointer.color("black")
guessed_states = []

while len(guessed_states) < 50:

    answer = screen.textinput(f"{len(guessed_states)}/50 States correct","Try to guess an state! ").title()
    
    state = data[data["state"] == answer]

    if not state.empty and  not state.state.iloc[0] in guessed_states:
        
        pointer.goto(int(state.x.item()),int(state.y.item()))
        pointer.write(arg=answer,font=FONT,align="center")
        guessed_states.append(state.state.iloc[0])
    
    else:
        reset = screen.textinput("Wrong!","You are a looser, looser! Write \"Bye\" to exit, or \"R\" to try again").lower()
        if reset == "bye":
            break
        elif(reset != "r"):
            screen.textinput("Yours father´s are cousins?","Stupid bitch. Try again and shut up. Just write anything.")

screen.bye()  
if len(guessed_states) < 50:
    all_states = data["state"].to_list()
    to_learn = [state for state in all_states if state not in guessed_states]
    pandas.DataFrame(to_learn).to_csv("state_to_learn.csv")
    