for i in range(1,10**4):
    name = input("Enter the employ name :\n")
    x = []
    y = []
    salary = input("How much is his salary :\n")
    bonus = input("Did he get bouns ?\n")
    y.append(name)
    
    x.append(salary)
    if bonus == "yes":
        x.append(int(bonus))
    else:
     bonus = 0
     x.append(int(bonus))     
    
