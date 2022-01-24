import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the States!")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
words = Turtle()
words.hideturtle()

answer_state = screen.textinput(title="Guess a State", prompt="What a states name?").title()
user_score = 0
state_data = pandas.read_csv("50_states.csv")
state_in_us = state_data.state.to_list()


def display_text(answer_state):
    state = state_data[state_data.state == answer_state]
    state_name = state.state
    state_location = (int(state.x), int(state.y))
    words.penup()
    words.goto(state_location)
    words.write(f"{state_name.item()}", font=("Courier", 9, "normal"))
    pass


gameplay = True
guessed_states = []

while gameplay:

    if answer_state == "Exit":
        missing_states = []
        for state in state_in_us:
            if state not in guessed_states:
                missing_states.append(state)
        things_to_study = pandas.DataFrame(missing_states)
        things_to_study.to_csv("things-to-study")
        break

    if answer_state in state_in_us:
        guessed_states.append(answer_state)
        display_text(answer_state)
        user_score += 1
        answer_state = screen.textinput(title=f"{user_score}/50States Correct", prompt="What is another "
                                                                                       "states name?").title()
    else:
        words.penup()
        words.goto(-150, 0)
        words.write("Game Over. You Lose!", font=("Courier", 24, "normal"))
        gameplay = False

    if user_score == 50:
        words.write("Game Over! You Guessed all the states!", font=("Courier", 24, "normal"))

