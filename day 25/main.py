import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")

IMAGE = "blank_states_img.gif"


def corr_tuple(my_input, data):
    if my_input in data.state.tolist():
        x = int(data[data.state == my_input]['x'])
        y = int(data[data.state == my_input]['y'])
        return (x, y)
    else:
        return False


screen = turtle.Screen()
screen.title("U.S. State Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

all_states = data.state.tolist()
counter = 10
correct_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 State Correct",
                                    prompt="What's a another state's name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in correct_states]
        new_df = pd.DataFrame(missing_states, columns=['states'])
        new_df.to_csv('states_with_you_dont_know.csv')
        break
    if answer_state in all_states and answer_state not in correct_states:
        corr = corr_tuple(answer_state, data)
        turtle_loc = turtle.Turtle()
        turtle_loc.hideturtle()
        turtle_loc.penup()
        turtle_loc.goto(corr_tuple(answer_state, data))
        turtle_loc.write(answer_state, align='center', font=("Arial", 8, "normal"))
        correct_states.append(answer_state)
