print ("Welocme to i shop calculator")
num = int(input ("How many items do you have : \n"))
total_price = []
basket = []
num = num+1
fa = 0
print("Let's calculat them")
for i in range (1,num):
    fa= fa+1
    item = input(f"Please tell me the name of the item number {fa} :\n")
    basket.append(item)
    price = float(input(f"What the price of {item} :\n"))
    total_price.append(price)
answer = input ("Do you wnat to see your entier basket :\n").lower()
if answer == "yes":
        print(basket) 
answer_2 = input("Do you wnat to see how much it will cost :\n").lower()
if answer_2 ==  "yes":
    la =(sum(total_price)) 
    print(f"{la}$")
    
