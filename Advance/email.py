import os
import time
import random
import string

with open("email.txt","r",encoding="utf_8") as g:
  check_u = g.read().splitlines() 
def clear():
  os.system("clear")
def check_email(email):
  if "." in email and "@" in email:
    return True
  else:
    return False 
def add_email(name,email):
  if check_email(email) == True:
    print(f"Email added sussfuly")
    print(f"Under name {name}")
  else:
    print("Invalid email")
    print("Check in your input")
    print(f"Added failed under name {name}")
name = input("Enter your name :\n")
ask = input("Enter y to suggest you an email or n to write your own :\n")
while True:
  random_email = random.choices(string.ascii_letters,k=6)
  random_string = ""
  for i in random_email:
    random_string += i
  if ask == "y":
    email = f"{random_string}@gmail.com"
    if email in check_u:
      continue 
    else:
      break
  else:
    email = input("Enter your email :\n")
    if email in check_u:
      print("Taken one")
      continue 
    else:
      break
print("Please wait a second")
time.sleep(3)
print(f"Working in your order {name}")
time.sleep(2)
print("Trying to read the data")
time.sleep(2)
add_email(name,email)
with open("email.txt","a",encoding="utf_8") as f:
  f.write(f"{email}\n")
time.sleep(6)
clear()

  