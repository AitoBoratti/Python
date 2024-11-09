import turtle as t
import random as r
from viborin import fragmento, serpiente

t.bgcolor("black")
t.title("Viborita")
screenW, screenH = t.screensize()


#--------------------------------
viborin = serpiente()




food = t.Turtle("square")
food.color("red")
food.penup()
food.shapesize(0.8)

def redondear_multiplo_20(valor):
    return round(valor / 20) * 20

def mover_comida():
    food.hideturtle()
    x = redondear_multiplo_20(r.randint(0-screenW,screenW))
    y = redondear_multiplo_20(r.randint(0-screenW,screenW))
    food.goto(x, y)
    food.showturtle()

mover_comida()              
screen = t.Screen()
t.tracer(0)


# Loop de juego.

while True:     
    screen.listen()   
    screen.onkeypress(viborin.arriba, "w")
    screen.onkeypress(viborin.abajo, "s")
    screen.onkeypress(viborin.izquierda, "a")
    screen.onkeypress(viborin.derecha, "d")
    if (food.distance(viborin.getPosicion()) <= 1 ):
        mover_comida()
        viborin.añadirFragmento()
    if (viborin.colision()):
        screen.clear()    
    
    
    
    
    
    
    
    
    
    
    
    screen.update()
    