import turtle as t
import random


screen = t.Screen()
screen.colormode(255)


colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim = t.Turtle()
tim.penup()

print(tim.pos())
def coloumn_dots ():
    for dot in range(10):
        tim.color(random.choice(colors))
        tim.dot(20)
        tim.forward(40)


for ydot in range(10):
    coloumn_dots()
    tim.setx(0)
    current_y = tim.ycor()
    tim.sety(cu)



screen.exitonclick()

