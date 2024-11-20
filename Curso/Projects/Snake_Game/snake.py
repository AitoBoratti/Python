from turtle import Turtle
DIRECTIONS = {"right": 0, "up": 90, "left": 180, "down": 270}
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        self.speed = 100
        self.body = []
        self._create_snake()
        self.head = self.body[0]
        self.body_len = lambda : len(self.body) -1
        

    def _create_snake(self):
        for position in STARTING_POSITIONS:
            new_part = Turtle("square")
            new_part.color("white")
            new_part.penup()
            new_part.shapesize(0.9,0.9)
            new_part.goto(position)
            self.body.append(new_part)
        

    def move(self):
        for i in range(self.body_len(),0,-1):
            new_x = self.body[i-1].xcor() 
            new_y = self.body[i-1].ycor()
            self.body[i].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if DIRECTIONS["down"] != self.head.heading():
            self.head.setheading(DIRECTIONS["up"])
    def down(self):
        if DIRECTIONS["up"]!= self.head.heading():
            self.head.setheading(DIRECTIONS["down"])
    def right(self):
        if DIRECTIONS["left"]!= self.head.heading():
            self.head.setheading(DIRECTIONS["right"])
    def left(self):
        if DIRECTIONS["right"]!= self.head.heading():
            self.head.setheading(DIRECTIONS["left"])



    def grow(self):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.shapesize(0.9,0.9)


        last_part = self.body[-1] 
        new_x = last_part.xcor() 
        new_y = last_part.ycor() - MOVE_DISTANCE
        new_part.goto(x=new_x,y=new_y)


        self.body.append(new_part)
        self.speed -=2



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
    
    def reappear(self):
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