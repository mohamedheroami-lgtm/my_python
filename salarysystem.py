number = int(input("How many employees do you have\n"))
x = []
y = []
g = number
while number > 0:
    number -= 1
    name = input("Enter the employee name\n")
    x.append(name)
    salary = int(input("Enter his salary\n"))
    bouns = int(input("Enter his bouns\n"))
    total = salary+bouns
    y.append(total)
number = number    
for i in range(g):
    print(f"The employee name is {x[i]}")
    print(f"His salary is {y[i]}")
print(sum(y))    
  
  