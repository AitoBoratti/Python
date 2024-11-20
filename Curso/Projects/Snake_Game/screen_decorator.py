from turtle import Turtle
LIMIT = 285
COMPENSATION = 8

class Screen_Decorator:
    def __init__(self):
        self.item = Turtle(visible=False)
        self.item.color("white")
        self.item.penup()
        self.item.goto(LIMIT, -LIMIT)
        self.item.pendown()
        self.draw()
    def draw(self):  
            # Esquina inferior derecha
            # print(f"Esquina inferior derecha: ({LIMIT}, {-LIMIT})")
        self.item.goto(LIMIT, LIMIT+COMPENSATION)  # Esquina superior derecha
            # print(f"Esquina superior derecha: ({LIMIT}, {LIMIT+COMPENSATION})")

        self.item.goto(-LIMIT -COMPENSATION, LIMIT+COMPENSATION)  # Esquina superior izquierda
            # print(f"Esquina superior izquierda: ({-LIMIT -COMPENSATION}, {LIMIT+COMPENSATION})")

        self.item.goto(-LIMIT -COMPENSATION, -LIMIT)  # Esquina inferior izquierda
            # print(f"Esquina inferior izquierda: ({-LIMIT -COMPENSATION}, {-LIMIT})")
        
        self.item.goto(LIMIT, -LIMIT)  # Cerrar el rectángulo
