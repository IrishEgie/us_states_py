import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
screen.title("US States Game")
# screen.setup(width=600, height=600)

image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()

def get_mouse_click_coor(x,y):
    print(x,y)


turtle.shape(image)

screen.exitonclick()