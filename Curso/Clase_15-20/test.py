import turtle as t
from random import choice,randint


screen = t.Screen()
screen.bgcolor("black")
pen = t.Turtle()
t.colormode(255)
pen.speed("fastest")
pen.pencolor("white")



"Draw a Spirograph"
# def draw_circle():
#     pen.circle(100)

# pen.hideturtle()
# distance = 
# number_of_circles = int(360 / distance) 
# for i in range(number_of_circles):
#     pen.forward(distance)
#     draw_circle()
#     pen.right(distance)
# input()


"Random Walk"
# def get_random_direction():
#     number = 90 * randint(0,3)
#     return number


# def get_random_color():
#     return (randint(1,255),randint(1,255),randint(1,255))


# def random_walk():
#     pen.pencolor(get_random_color())
#     pen.right(get_random_direction())
#     pen.forward(30)
    
    
# t.colormode(255)
# pen.hideturtle()
# pen.speed(0)
# for _ in range(500):
#     random_walk()

# input()


"Draw a line"
# for i in range(30):
#     pen.forward(10)
#     if i % 2 == 0:
#         pen.up() 
#     else:
#         pen.down()


"""Draw a Triangle, square, pentagon, hexagon, petagon, 
   octagon, nonagon, and decagon"""
# input()
# def draw_shape(sides, size):
#     angle = (360 / sides)
#     for j in range(sides):
#         pen.forward(size)
#         pen.right(angle)
        
# size = 100
# pen.hideturtle()
# for sides in range(3,11,1):
#     draw_shape(sides,size)
# input()



