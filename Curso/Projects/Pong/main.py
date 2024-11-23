from turtle import Screen
from interface import Line, Menu, Score
from paddle import Paddle, Paddle_IA
from ball import Ball

class Game:
    X_LIMIT = 300
    Y_LIMIT = 280
    SCREEN_SIZE = 600
    PADDLE_SPEED = 7
    KEYS = {"w": False, "s": False, "Up": False, "Down": False}

    def __init__(self):
        # Configuración inicial de la pantalla
        self.screen = Screen()
        self.screen.setup(self.SCREEN_SIZE, self.SCREEN_SIZE)
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.listen()
        
        # Variables de control
        self.game_is_on = True
        
        # Elementos del juego
        self.score = None
        self.line = None
        self.paddle1 = None
        self.paddle2 = None
        self.ball = None
        self.ia1 = None
        self.ia2 = None
        self.menu = None

    def adjust_inputs(self):
        """Configuración de teclas de movimiento, elimina las opciones del menu."""
        self.screen.onkeypress(lambda x="w": self.key_down(x), "w")
        self.screen.onkeypress(lambda x="s": self.key_down(x), "s")
        self.screen.onkeypress(lambda x="Up": self.key_down(x), "Up")
        self.screen.onkeypress(lambda x="Down": self.key_down(x), "Down")

        self.screen.onkeyrelease(lambda x="w": self.key_up(x), "w")
        self.screen.onkeyrelease(lambda x="s": self.key_up(x), "s")
        self.screen.onkeyrelease(lambda x="Up": self.key_up(x), "Up")
        self.screen.onkeyrelease(lambda x="Down": self.key_up(x), "Down")

        self.screen.onkeypress(None, "1")
        self.screen.onkeypress(None, "2")
        self.screen.onkeypress(None, "3")

    def key_down(self, key):
        self.KEYS[key] = True

    def key_up(self, key):
        self.KEYS[key] = False


    def start_game(self, option):
        """Incializa el juego con los parametros de IA indicados"""

        # Preparamos los inputs del juego
        self.adjust_inputs()

        # Inicializar elementos del juego
        self.score = Score()
        self.line = Line()
        self.paddle1 = Paddle("left")
        self.paddle2 = Paddle("right")
        self.ball = Ball()

        if option == 1:
            self.ia2 = Paddle_IA(ball=self.ball, paddle=self.paddle2, side="right")
        elif option == 3:
            self.ia1 = Paddle_IA(ball=self.ball, paddle=self.paddle1, side="left")
            self.ia2 = Paddle_IA(ball=self.ball, paddle=self.paddle2, side="right")

        self.menu.hide()
        self.game_loop()

    def check_paddle_collision(self):
        paddle_width = 20
        paddle_height = 110
        ball_radius = 10

        # Límites de paddle1
        paddle1_top = self.paddle1.ycor() + paddle_height / 2
        paddle1_bottom = self.paddle1.ycor() - paddle_height / 2
        paddle1_right = self.paddle1.xcor() + paddle_width / 2
        paddle1_left = self.paddle1.xcor() - paddle_width / 2

        # Límites de paddle2
        paddle2_top = self.paddle2.ycor() + paddle_height / 2
        paddle2_bottom = self.paddle2.ycor() - paddle_height / 2
        paddle2_right = self.paddle2.xcor() + paddle_width / 2
        paddle2_left = self.paddle2.xcor() - paddle_width / 2

        # Verificar colisiones
        if (paddle1_bottom <= self.ball.ycor() <= paddle1_top and
                paddle1_right >= (self.ball.xcor() - ball_radius) >= paddle1_left):
            return True

        if (paddle2_bottom <= self.ball.ycor() <= paddle2_top and
                paddle2_left <= (self.ball.xcor() + ball_radius) <= paddle2_right):
            return True

        return False

    def serve(self, side):
        self.ball.serve(side)
        self.screen.onkey(None, "space")

    def game_loop(self):
        if self.game_is_on:
            self.screen.update()
            self.ball.move()

            # Movimiento de las IA
            if self.ia1:
                self.ia1.adjust_position()
                if self.ia1.loose:
                    self.ia1.serve()

            if self.ia2:
                self.ia2.adjust_position()
                if self.ia2.loose:
                    self.ia2.serve()

            # Movimiento de los jugadores
            if self.KEYS["w"]:
                self.paddle1.go_up(self.PADDLE_SPEED)
            if self.KEYS["s"]:
                self.paddle1.go_down(self.PADDLE_SPEED)
            if self.KEYS["Up"]:
                self.paddle2.go_up(self.PADDLE_SPEED)
            if self.KEYS["Down"]:
                self.paddle2.go_down(self.PADDLE_SPEED)

            # Colisiones
            if self.ball.ycor() > self.Y_LIMIT or self.ball.ycor() < -self.Y_LIMIT:
                self.ball.bounce()

            if self.check_paddle_collision():
                self.ball.bounce_on_paddle()

            # Puntos anotados
            if self.ball.xcor() > self.X_LIMIT:
                self.score.increment_left()
                self.ball.reset()
                if self.ia2:
                    self.ia2.loose = True
                else:
                    self.screen.onkey(lambda x="right": self.serve(x), "space")

            elif self.ball.xcor() < -self.X_LIMIT:
                self.score.increment_right()
                self.ball.reset()
                if self.ia1:
                    self.ia1.loose = True
                else:
                    self.screen.onkey(lambda x="left": self.serve(x), "space")

            self.screen.ontimer(self.game_loop, 10)

    def run(self):
        self.menu = Menu()
        # Configurar inputs iniciales
        self.screen.onkeypress(lambda x=1: self.start_game(x), "1")
        self.screen.onkeypress(lambda x=2: self.start_game(x), "2")
        self.screen.onkeypress(lambda x=3: self.start_game(x), "3")
        self.screen.onkeypress(self.screen.bye, "Escape")
        self.screen.exitonclick()


# Iniciar el juego
if __name__ == "__main__":
    game = Game()
    game.run()