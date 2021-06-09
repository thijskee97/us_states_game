import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
game_is_on = True
score = 0
while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State {score}/50", prompt="Guess a State name: ").title()
    print(answer_state)

    data = pandas.read_csv("50_states.csv")
    all_states = data.state


    for state in all_states:
        if state == answer_state:
            print("correct")
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x),int(state_data.y))
            t.write(answer_state)
            score += 1

screen.mainloop()


