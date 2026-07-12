class Student:
  def __init__(self,name,age,sch_class,grades = 0):
    """تعريف قيمه الدرجات كديفولت معى امكانيه تغييرها مقدما عند كل طالب بواسطه ادخال قيمه الدرجات عند داله الطباعه"""
    self.name = name
    self.age = age 
    self.sch_class = sch_class
    self.grades = grades
  def information(self,new_grades):
    self.grades = new_grades
    print(f"Student name : {self.name}\nStudent age = {self.age} years old\nStudent school class {self.sch_class}\nStudent grades = {self.grades} point from 180")

def creat_student():
  name_st = input("Enter Student name :\n")
  age_st = input("Enter Student age :\n")
  class_st = input("Enter Student currnt class :\n")
  return Student(name_st,age_st,class_st)

st1 = creat_student()
st1.information(160)