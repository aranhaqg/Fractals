from turtle import *
import turtle
import random


# Fractal simples do floco de neve

def fractal(length, depth):
    if depth == 0:
        myPen.forward(length)
    else:
        fractal(length / 3, depth - 1)
        myPen.right(60)
        fractal(length / 3, depth - 1)
        myPen.left(120)
        fractal(length / 3, depth - 1)
        myPen.right(60)
        fractal(length / 3, depth - 1)


def draw_snowflake(length, depth):
    fractal(length, depth - 1)
    myPen.left(120)
    fractal(length, depth - 1)
    myPen.left(120)
    fractal(length, depth - 1)


if __name__ == "__main__":
    myPen = turtle.Turtle()
    myPen.penup()
    myPen.goto(-100, -50)
    myPen.pendown()
    myPen.speed(0)
    # myPen.pencolor('blue')
    myPen.color("blue")

    draw_snowflake(240, 4)
    draw_snowflake(240, 4)
    draw_snowflake(240, 4)
    myPen.penup()
    myPen.goto(140, -50)
    myPen.pendown()
    draw_snowflake(240, 4)
    draw_snowflake(240, 4)
    draw_snowflake(240, 4)
    myPen.penup()
    myPen.goto(20, 158)
    myPen.pendown()
    draw_snowflake(240, 4)
    draw_snowflake(240, 4)
    draw_snowflake(240, 4)

    exitonclick()