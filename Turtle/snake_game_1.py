from turtle import Turtle, Screen



window = Screen()
window.screensize(1600,1600)
window.bgcolor("black")
window.tracer(0)
index = [(-60,0),(-40,0),(-20,0),(0,0)]
turtle = [] 

for i in range(4):
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.penup() 
    new_turtle.goto(index[i])
    new_turtle.speed("slow") 
    turtle.append(new_turtle) 
     
window.update()


game_on = True
while game_on:
    for i in turtle:
        i.forward(1)
        window.update()



window.exitonclick() 