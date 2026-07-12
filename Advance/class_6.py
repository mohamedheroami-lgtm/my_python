import os 
import time
def clear():
  """داله تنظيف الشاشه"""
  os.system("cls") if os.name == "nt" else os.system("clear")
class Person:
  def __init__(self,frist_name,last_name,id,stats = "inactive"):
    self.frist_name = frist_name
    self.last_name = last_name
    self.id = id 
    self.stats = stats
  def show(self):
    """داله عرض العضو"""
    print(f"Frist name : {self.frist_name}")
    print(f"Last name : {self.last_name}")
    print(f"ID : {self.id}")
    print(f"Stats : {self.stats}")
def opj():
  """داله انشاء الكائن"""
  f_name = input("Enter first name :\n")
  l_name = input("Enter last name :\n")
  id = input("Enter membership  id :\n")
  st = input("Enter membership Stats or press enter:\n")
  if st == "":
    st = "inactive"
  return Person(f_name,l_name,id,st)


members = []
while True:
  ask = input("1.Add anew member\n2.Disply all members\n3.Search for a member\n4.Exit :\n")
  if ask == "1":
    members.append(opj())
    print("Members added")
    clear()
  elif ask == "2":
    if members:
      clear()
      for i in members:
        i.show()
      time.sleep(7)
      clear()
    else:
      print("Empty")
  elif ask == "3":
    ent = input("Search with\n1.membership id\n2.Frist name\n3.Stats :\n")
    if ent == "1":
      la = input("Enter membership id :\n")
      for i in members:
        if la == i.id:
          i.show()
      time.sleep(7)
      clear()
          
    elif ent == "2":
      ga =  input("Enter first name :\n")
      for i in members:
        if ga == i.frist_name:
          i.show()
      time.sleep(6)
      clear()
          
    elif ent == "3":
      sta = input("Enter active or in active :\n")
      for i in members:
        if sta == i.stats:
          i.show()
        elif sta == i.stats:
          i.show()
      time.sleep(7)
          
    else:
      print("invalid")
      clear()
  elif ask == "4":
    break