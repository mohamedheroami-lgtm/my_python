from turtle import Turtle  , Screen



window = Screen()
window.screensize(500, 500)
window.bgcolor("black")



sam = Turtle()
sam.shape("turtle")
sam.color("red")
sam.speed("fastest")


def circle(name):
    name.penup()
    name.goto(-200,-500)
    name.pendown()
    for _ in range(20):
        name.circle(70)
        name.left(360/20)
        
def triangle(name):
        def tri(name):          
            for _ in range(3):
                name.left(60)
                name.forward(150)
                name.left(60)
        name.penup()
        name.goto(0,0)
        name.pendown()
        for i in range(20):
            tri(name)
            name.left(360/20)
def square(name):
        def squ(name):                  
                        for _ in range(4):
                            name.forward(100)
                            name.left(90)
        name.penup() 
        name.goto(200,500)
        name.pendown()                    
        for _ in range(20):
                        squ(name) 
                        name.left(360/20)       
                        
        
                  
circle(sam)
triangle(sam)
square(sam)






window.exitonclick()