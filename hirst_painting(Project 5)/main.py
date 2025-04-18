# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r #bcs we want only rgb value from colorslist
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,b,g)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
tim= Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 110, 164),(236, 243, 239), (149, 50, 75), (222, 136, 201), (53, 123, 93), (170, 41, 154), (138, 20, 31), (134, 184, 163), (197, 73, 92), (47, 86, 121), (73, 35, 43), (145, 149, 178), (14, 70, 98), (232, 165, 176), (160, 158, 142), (54, 50, 45), (101, 77, 75), (183, 171, 205), (36, 74, 60), (19, 89, 86), (82, 129, 148), (147, 19, 17), (27, 102, 68), (12, 64, 70), (107, 153, 127), (176, 208, 192), (168, 102, 99)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots +1 ):
    tim.dot(20,random.choice(color_list))
    tim.forward((50))

    if dot_count%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen=Screen()
screen.exitonclick()