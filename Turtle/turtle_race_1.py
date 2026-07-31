from turtle import Turtle , Screen
import random


window = Screen()
window.screensize(700,700)
user_input = window.textinput(title="python turtle game",prompt="Enter red , green or black")


red = Turtle()
red.shape("turtle")
red.color("red")
red.penup()
red.goto(-300,300)
green = Turtle()
green.shape("turtle")
green.color("green")
green.penup()
green.goto(-300,0)
black = Turtle()
black.shape("turtle")
black.color("black")
black.penup()
black.goto(-300,-300)


list_of_speed = ["fast","fastest","slow","slowest"]
list_of_dist = [1,2,3,4]

for _ in range(1000):
    turtle = [red,green,black]
    random.choice(turtle).forward(random.choice(list_of_dist))
    if green.xcor() >= 300 and user_input == "green":
        green.hideturtle()
        green.goto(0,0)
        green.pendown()
        green.write("You win",font=("arial",14,"bold"),align="center")
        break
    elif red.xcor() >= 300 and user_input == "red":
        red.hideturtle()
        red.goto(0,0)
        red.pendown()
        red.write("You win",font=("arial",14,"bold"),align="center")
        break
    elif black.xcor() >= 300 and user_input == "black":
        black.hideturtle()
        black.goto(0,0)
        black.pendown()
        black.write("You win",font=("arial",14,"bold"),align="center")
        break
    elif (red.xcor() >= 300 and user_input != "red") or (black.xcor() >= 300 and user_input != "black") or (green.xcor() >= 300 and user_input != "green"):
        black.hideturtle()
        black.goto(0,0)
        black.pendown()
        black.write("You lose",font=("arial",12,"bold"),align= "center")
        break
    
    
         
    


window.exitonclick()