from turtle import Turtle , Screen

import random

window = Screen()

sam = Turtle()
tom = Turtle()


window.setup(width=100,height=100)
window.bgcolor("black")

sam.color("orange")
sam.speed("fastest")
sam.pensize(4)
tom.color("red")
tom.speed("fast")
tom.pensize(6)






my_angle = [20,50,70,90,180,270]
my_distance = [50,10,40,90,60,25,40]
loop = [14,17,19,40,30,20]
name = sam
while True:
    for _ in range(random.choice(loop)):
        name.forward(random.choice(my_distance))
        name.left(random.choice(my_angle))
    if name == tom :
        break
    name = tom
        
















window.exitonclick()