from turtle import Screen
from car import Car
from decoration import Decoration
from player import Player
from interface import Interface

class CrossTurtleGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.colormode(255)  # Enable RGB colors
        asphalt_color = (30, 30, 30)
        self.screen.bgcolor(asphalt_color)
        self.screen.tracer(0)

        self.deco = Decoration()
        self.player = Player()
        self.interface = Interface()
        self.cars = []
        self.game_is_on = True

        self.screen.listen()
        self.screen.onkey(self.player.move_up, "w")
        self.screen.onkey(self.player.move_down, "s")

    def create_cars(self):
        align = 1
        for i in range(40):
            self.cars.append(Car(align))
            align *= -1

    def cars_update(self):
        for car in self.cars:
            car.move_forward()
            # I must account for slight differences in heights
            if (abs(car.xcor() - self.player.xcor()) <= 40 and 
                abs(car.ycor() - self.player.ycor()) <= 15):
                return True
        return False

    def accelerate(self):
        for car in self.cars:
            car.accelerate()

    def end_game(self):
        for car in self.cars:
            car.hideturtle()
        self.player.hideturtle()
        self.interface.end_game()
        self.screen.update()

    def game_loop(self):
        if self.game_is_on:
            collision = self.cars_update()
            self.screen.update()
            
            if collision:
                self.game_is_on = False  

            elif self.player.ycor() > 255:
                self.interface.level_up()
                self.accelerate()
                self.player.reset()

            self.screen.ontimer(self.game_loop, 10)
        else:
            self.end_game()

    def run(self):
        self.create_cars()
        self.game_loop()
        self.screen.exitonclick()

if __name__ == "__main__":
    game = CrossTurtleGame()
    game.run()


# from turtle import Screen, Turtle
# from car import Car
# from decoration import Decoration
# from player import Player
# from interface import Interface

# screen = Screen()
# screen.setup(600,600)
# screen.colormode(255)  # Habilitar colores RGB
# asphalt_color = (30, 30, 30)
# screen.bgcolor(asphalt_color)
# screen.tracer(0)
# deco = Decoration()
# player = Player()
# interface = Interface()
# game_is_on = True

# screen.listen()
# screen.onkey(player.move_up,"w")
# screen.onkey(player.move_down,"s")


# cars = []
# def create_cars():
#     aling = 1
#     for i in range(40):
#         cars.append(Car(aling))
#         aling *= -1


# def cars_update():
#     for car in cars:
#         car.move_forward()
#         # Tengo que tener en cuenta las ligeras diferencias entre alturas
#         if (abs(car.xcor() - player.xcor()) <= 40 and 
#             abs(car.ycor() - player.ycor()) <= 15):
#             return True
#     return False


# def accelerate():
#     for car in cars:
#         car.accelerate()


# def end_game():
#     for car in cars:
#         car.hideturtle()
#     player.hideturtle()
#     interface.end_game()
#     screen.update()


# def game_loop():
#     global game_is_on
    
#     if game_is_on:
#         collision = cars_update()
#         screen.update()
        
#         if collision:
#             game_is_on = False  

#         elif player.ycor() > 255:
#             interface.level_up()
#             accelerate()
#             player.reset()

#         screen.ontimer(game_loop,10)
#     else:
#         end_game()


# create_cars()
# game_loop()
# screen.exitonclick()