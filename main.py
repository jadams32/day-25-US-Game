import turtle

screen = turtle.Screen()
screen.title("Guess the States!")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess a State", prompt="What is another states name?")

screen.exitonclick()
# TODO: Display states name after user guesses it.
# TODO: Implement counter
# TODO: Implement game over
# TODO: Pull data from the csv

