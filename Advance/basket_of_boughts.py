import os 
def calculate(number,price) :
    return number*price
def clear() :
        os.system("clear")              
while True :
    clear()
    budget = float(input("Enter your spending budget :\n"))
    item = input("Enter the item you want to buy :\n") 
    numberit = int(input(f"Enter how many {item}s do you want to buy :\n")) 
    priceit = float(input(f"Enter the price pre {item} :\n"))
    total = calculate(number = numberit,price = priceit )
    if total > budget :
        print("Warning : your purchase exceeds your daily budget")
        choice = input("Do you want to continue y or n :\n")
        if choice == "y" :
            clear()
            continue
        else :
            break
            
    else :
        print("Purchase successful")  
    if input("Do you want to continue :\n") != "y" :
        break
    else :
        continue    
        