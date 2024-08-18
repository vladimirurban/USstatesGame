import turtle
import pandas

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

guessed_answer = []
missing_states = []


while len(guessed_answer) < 50:
    answer_state = screen.textinput(title=f"Guess the state {len(guessed_answer)}/50 States Correct",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_answer]
        pandas.DataFrame(missing_states).to_csv("missing states.csv")
        break

    if answer_state in states_list:
        guessed_answer.append(answer_state)
        state_index = states_list.index(answer_state)
#        state_data = data[data.state == answer_state]
#        print(state_data)
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(data["x"][state_index], data["y"][state_index])
        state_name.write(f"{data.state[state_index]}")
