import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def read_data_csv():
    data = pd.read_csv("50_states.csv")
    return data

def write_state_name(state_name, x, y):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(x, y)
    pen.write(state_name, align="center", font=("Arial", 8, "normal"))

def state_matching(answer):
    data = read_data_csv()
    state_names = data["state"].to_list()

    if answer in state_names:
        state_row = data[data["state"] == answer]
        x = int(state_row["x"])
        y = int(state_row["y"])
        write_state_name(answer, x, y)
        return True
    else:
        return False
# Main loop
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50", "Guess a state!")

    if state_matching(answer_state) and answer_state not in guessed_states:
        guessed_states.append(answer_state)
    else:
        print("Oops, that is incorrect!")
        break
screen.exitonclick()