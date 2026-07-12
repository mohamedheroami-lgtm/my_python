import random
fa = random.randint(0,10)
ga = int(input("Enter one number :\n"))
if ga == fa:
    print(f"Right")
else:
    print(f"you gussed {ga}, and the Right number is {fa}")