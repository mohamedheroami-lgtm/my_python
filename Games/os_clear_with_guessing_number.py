import os 
import random
def clear ():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")    
number = random.randint(1,10)
while True :
    gusse = int(input("Enter number betwen 1 and 10 :\n"))
    if gusse != number :
        print("wrong choice")
        input("Press enter to continue")
        clear()
        continue
    else:
        print("Right")
        break
    