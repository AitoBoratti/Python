###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
# rgb_colors = []
# colors = colorgram.extract("image.jpg",84)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# rgb_colors.remove((245, 243, 238))
# print(rgb_colors)


X_START = -200
Y_START = 200
DISTANCE = 100
color_list = [(173, 216, 230),
            (149, 75, 50),
            (222, 201, 136),
            (53, 93, 123),
            (170, 154, 41),
            (138, 31, 20),
            (134, 163, 184),
            (197, 92, 73),
            (47, 121, 86),
            (73, 43, 35),
            (145, 178, 149),
            (14, 98, 70),
            (232, 176, 165),
            (160, 142, 158),
            (54, 45, 50),
            (101, 75, 77),
            (183, 205, 171),
            (36, 60, 74),
            (19, 86, 89),
            (82, 148, 129),
            (147, 17, 19),
            (27, 68, 102),
            (12, 70, 64),
            (107, 127, 153),
            (176, 192, 208),
            (168, 99, 102),
            (66, 64, 60),
            (219, 178, 183),
            (178, 198, 202),
            (112, 139, 141),
            (254, 194, 0)]

t.setup(600,500)
screen = t.Screen()
screen.screensize(600,500)

pen = t.Turtle()
pen.hideturtle()
pen.up()
pen.goto(X_START,Y_START)
t.colormode(255)
screen.bgcolor((245, 243, 238))

for i in range(len(color_list)-1):
    
    if ((i)%5 == 0) and (i != 0):
        pen.goto(X_START,pen.ycor() - DISTANCE)

    pen.dot(50,color_list[i])
    pen.goto(pen.xcor() + DISTANCE ,pen.ycor())



input()