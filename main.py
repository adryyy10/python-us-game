import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
MAX_STATES = 50

states = pandas.read_csv("50_states.csv")
end_game = False
answered = 0
while not end_game:
    answer_state = screen.textinput(title=f"Guess the state {answered}/{MAX_STATES}", prompt="What's another state's name")
    answer_state = answer_state.title()
    for state in states.state:
        if answer_state == state:
            answered += 1
            if answered >= MAX_STATES:
                end_game = True
            # Write something coordinates
            x_coord = states[states.state == answer_state].x
            y_coord = states[states.state == answer_state].y
            # Write state in coordinates
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(x_coord), int(y_coord))
            t.write(answer_state)

screen.exitonclick()