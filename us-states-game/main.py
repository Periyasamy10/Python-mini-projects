import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S Start Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
found_state = []

while len(found_state) < 50:
    answer_state = screen.textinput(title=f"{len(found_state)}/50 correct state", prompt="what's another state name?").title()

    if answer_state == "Exit":
        missing_states =[state for state in states_list if state not in found_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in states_list:
        found_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
