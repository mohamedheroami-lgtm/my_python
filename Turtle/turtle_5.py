from turtle import Turtle , Screen
import random

window = Screen()

sam = Turtle()

list_of_color = ["green","red"]
list_of_size = [6,3]
list_of_shape = ["turtle","arrow"]



def  triangle():   
    sam.color(random.choice(list_of_color))
    sam.pensize(random.choice(list_of_size))
    sam.shape(random.choice(list_of_shape))
    for _ in range(3):
        sam.left(60)
        sam.forward(150)
        sam.left(60)
 
        
                      
def  squre():
     sam.color(random.choice(list_of_color))
     sam.pensize(random.choice(list_of_size))
     sam.shape(random.choice(list_of_shape))
     for _ in range(4):
        sam.forward(300)
        sam.left(90)



def circle():
    sam.color(random.choice(list_of_color))
    sam.pensize(random.choice(list_of_size))
    sam.shape(random.choice(list_of_shape))
    sam.circle(70)
  

def write():            
            sam.write("press eny key to exit",font=("arial",12,"bold"),align="center")
      
            
                        

while True:
      
      user_input = window.textinput(title="Input box",prompt="Enter tirangle , circle , squre or exit ")
      if user_input == "triangle" or user_input == "مثلث":
          triangle()
      elif user_input == "squre" or user_input == "مربع":
         squre()
      elif user_input == "circle" or user_input == "دائره":
          circle()
      elif user_input == "exit" or user_input == "خروج":
          window.bgcolor("blue")
          break
          
      
      
sam.clear()
write()



window.exitonclick()