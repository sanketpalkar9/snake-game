from turtle import Turtle

class Border():
    def __init__(self):
        border = Turtle()
        border.penup()
        border.hideturtle()
        border.color("white")
        border.goto(-290, 290)
        border.pendown()
        border.goto(290, 290)
        border.goto(290, -290)
        border.goto(-290, -290)
        border.goto(-290, 290)



