from turtle import Turtle, Screen



window = Screen()
window.screensize(1600,1600)
window.bgcolor("black")
index = [(-40,0),(-20,0),(0,0)]
turtle = [] 

for i in range(3):
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.penup() 
    new_turtle.goto(index[i])
    new_turtle.speed("slow") 
    turtle.append(new_turtle) 
     


for _ in range(100):
    turtle[2].forward(56)
    turtle[2].left(90)
    turtle[1].goto(turtle[2].pos())       
    turtle[0].goto(turtle[1].pos())      
        
        
    
    
window.exitonclick() 