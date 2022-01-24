import turtle

screen = turtle.Screen()
screen.title("Guess the States!")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess a State", prompt="What is another states name?")
# TODO: Display states name after user guesses it.
# TODO: Implement game over
# TODO: Pull data from the csv

user_guess_score = 0
state_in_us = csv[0]
answer_state = screen.textinput(title="Guess a State", prompt="What is another states name?")


def display_text():
    pass


while user_guess_score < 50:
    for state in state_in_us:
        if answer_state.title() == state:
            answer_state = screen.textinput(title=f"{user_guess_score}/50States Correct", prompt="What is another "
                                                                                                 "states name?")
            display_text()
            user_guess_score += 1

    if user_guess_score == 50:
        turtle.write("Game Over! You Guessed all the states!")

screen.exitonclick()
