from turtle import Turtle, Screen
import random

window = Screen()
window.screensize(700, 700)
user_input = window.textinput(title="python turtle game", prompt="Enter red, green or black")

# بدلاً من تكرار الأوامر لكل سلحفاة، نستخدم القوائم للحركات السريعة
colors = ["red", "green", "black"]
y_positions = [300, 0, -300]
all_turtles = []

for i in range(3):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-300, y_positions[i])
    all_turtles.append(new_turtle)

is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(1, 4))
        
        # التقاط الفائز ديناميكياً بدلاً من الشروط المتعددة
        if turtle.xcor() >= 300:
            is_race_on = False
            winning_color = turtle.pencolor()
            
            # إخفاء السلحفاة وكتابة النتيجة
            turtle.hideturtle()
            turtle.goto(0, 0)
            
            if user_input == winning_color:
                turtle.write(f"You win! The {winning_color} turtle won!", font=("arial", 14, "bold"), align="center")
            else:
                turtle.write(f"You lose! The {winning_color} turtle won!", font=("arial", 14, "bold"), align="center")
            break

window.exitonclick()
