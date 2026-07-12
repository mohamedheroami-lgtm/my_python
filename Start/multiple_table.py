print("Welcome to multiplication table")
num =int(input("Enter a number :\n"))
oa = 0
print("Your multiplication table is :")
for number in range (12):
    
    oa = oa+1
    ha =(num*oa)
    print(f"{num} × {oa} = {ha}")