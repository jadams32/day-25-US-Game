# For day 25 I create a states guessing game. Play through the game guessing states until you can no longer remember
# anymore. Once you're finished type 'exit' to receive a new file with the list of states that you missed.

# Import files needed
import turtle
from turtle import Turtle
import pandas

# Initialize the screen and create the background of states
screen = turtle.Screen()
screen.title("Guess the States!")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
words = Turtle()
words.hideturtle()

# Store states in a list
state_data = pandas.read_csv("50_states.csv")
state_in_us = state_data.state.to_list()

# Prompt the user to guess a state name
answer_state = screen.textinput(title="Guess a State", prompt="What a states name?").title()


def display_text(answer_state):
    """Displays the states name over the state after user guesses correctly."""
    state = state_data[state_data.state == answer_state]
    state_name = state.state
    state_location = (int(state.x), int(state.y))
    words.penup()
    words.goto(state_location)
    words.write(f"{state_name.item()}", font=("Courier", 9, "normal"))
    pass


# Variables used
user_score = 0
gameplay = True
guessed_states = []

# Main Game Loop
while gameplay:

    if answer_state == "Exit":
        missing_states = [state for state in state_in_us if state not in guessed_states]
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
