import time
import os
def clear():
  os.system("cls") if os.name == "nt" else os.system("clear")
info = {}
class Person:
  def __init__(self,first_name,last_name,email,stats = "inactive"):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.stats = stats
  def disply(self):
    print(f"Frist name : {self.first_name}\nLast name : {self.last_name}\nEmail : {self.email}\nStats : {self.stats}")
  
      
def ask():
  fr_name = input("Enter your first name :\n")
  sc_name = input("Enter your last name :\n")
  email = input("Enter you email :\n")
  return Person(fr_name,sc_name,email)


new_user = []
while True:
  start = input("Welcome to users mangmant\n\nChoice an action\n1.add user\n2.disply users\npress enter to exit\n")
  if start == "1":
    clear()
    new_user.append(ask())
    continue
    print("Person add \n")
  elif start == "2":
    clear()
    if new_user:
      for i in new_user:
        i.disply()
      time.sleep(5)
    else:
      print("Empty")
      time.sleep(3)
    print("_"*20)
    print("\n")
    time.sleep(3)
  else:
    break