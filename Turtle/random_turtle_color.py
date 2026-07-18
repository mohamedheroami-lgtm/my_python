from turtle import Turtle , Screen
import random
sam = Turtle()
window = Screen()
list_of_color = ["green","red"]
list_of_size = [6,3]
list_of_shape = ["turtle","arrow"]
def one():
    for _ in range(40):
        sam.color(random.choice(list_of_color))
        sam.pensize(random.choice(list_of_size))
        sam.shape(random.choice(list_of_shape))
        sam.forward(200)
        sam.left(90)
one() 

    
        
            
                
window.exitonclick()        