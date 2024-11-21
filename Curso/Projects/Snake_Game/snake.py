from turtle import Turtle
DIRECTIONS = {"right": 0, "up": 90, "left": 180, "down": 270}
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
STARTING_SPEED = 80
ACCELERATION = 1

class Snake:
    def __init__(self):
        self.speed = STARTING_SPEED
        self.body = []
        self._create_snake()
        self.head = self.body[0]
        self.body_len = lambda : len(self.body) -1
        self.can_turn = True


    def add_segment(self,pos):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.shapesize(0.9,0.9)
        new_part.goto(pos)
        self.body.append(new_part)


    def _create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        

    def move(self):
        for i in range(self.body_len(),0,-1):
            new_x = self.body[i-1].xcor() 
            new_y = self.body[i-1].ycor()
            self.body[i].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
        self.can_turn = True


    def up(self):
        if (DIRECTIONS["down"] != self.head.heading()) and self.can_turn:
            self.head.setheading(DIRECTIONS["up"])
            self.can_turn = False


    def down(self):
        if (DIRECTIONS["up"]!= self.head.heading()) and self.can_turn:
            self.head.setheading(DIRECTIONS["down"])
            self.can_turn = False


    def right(self):
        if (DIRECTIONS["left"]!= self.head.heading()) and self.can_turn:
            self.head.setheading(DIRECTIONS["right"])
            self.can_turn = False


    def left(self):
        if (DIRECTIONS["right"]!= self.head.heading()) and self.can_turn:
            self.head.setheading(DIRECTIONS["left"])
            self.can_turn = False


    def grow(self):
        new_pos = self.body[-1].position()
        self.add_segment(new_pos)
        self.speed -= ACCELERATION


    def check_distance(self,object):
        if self.head.distance(object) < 1:
            return True
        return False
    

    def check_distance_from_body(self,object):
        for segment in self.body:
            if segment.distance(object) < 1:
                return True
        return False
    
    
    def check_self_collision(self):
        for i in range(1,self.body_len(),1):
            if self.check_distance(self.body[i]):
                return True
        return False
    

    def check_wall_colission(self):
        if ((self.head.xcor() > 290  or self.head.xcor() < -298) or 
            (self.head.ycor() > 298  or self.head.ycor() < -290)):
            return True
        return False
    

    def disappear(self):
        for segment in self.body:
            segment.hideturtle()
            
            
    def reset(self):
        for segment in self.body:
            segment.reset()
            segment.goto(800,800)
        self.body.clear()
        self._create_snake()
        self.head=self.body[0]
        self.speed = 100