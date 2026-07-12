import time
name = input("Enter your name")
def tax (income):
   return income * 0.15
def total_salary(salary,bouns):
  total = salary + bouns 
  salary_after_tax = tax(total)
  return total - salary_after_tax
salary = int(input("Enter your salary :\n"))
bouns = int(input("Enter your bouns :\n"))
the_income = total_salary(salary,bouns)
print("It will take some time ...")
time.sleep(3)
print("Finding rate if tax in sudan ...")
time.sleep(2)
print("System is working ...")
time.sleep(2)
print(f"Your income is {the_income}")
def append():
  with open("salary.txt","a",encoding="utf-8") as org :
    org.write(f"Your name is :\n{name}\nyour salary is :\n{the_income}\n")
  print("Doing that...")
  time.sleep(2)
  print("Whit...")
  time.sleep(3)
append()
with open("salary.txt","r",encoding="utf-8") as f :
  txt = f.read()
print(txt)


  


  
  