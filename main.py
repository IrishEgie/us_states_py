import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game")
# screen.setup(width=600, height=600)

image = "blank_states_img.gif"
screen.addshape(image)

def get_mouse_click_coor(x,y):
    print(x,y)

turtle.shape(image)

answer_state = turtle.textinput(title="Guess a state!",prompt="What's another State?")