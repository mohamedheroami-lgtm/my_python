import random 
randnum = random.randint(0,10)
gusses = ""
while gusses != randnum :
    gusses = int(input("Enter random number form 0 to 10 :\n"))
    if gusses < randnum :
        
        print("To low !")
        
    elif gusses > randnum :
        print("To high !")
        
      
if gusses == randnum:
    print("Correct")        