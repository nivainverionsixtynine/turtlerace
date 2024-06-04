from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="MAKE YOUR BET", prompt="Which turtle will win the race? Enter color: ")

tim = Turtle()
tim.speed(0)  # Set the speed to the fastest
tim.penup()

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-78, -48, -10, 20, 50, 80]

# Create turtles and set their color and position
turtles = []
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False

            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
