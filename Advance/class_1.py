#الدرس الاول في الكلاس هو الصفات او الاتربيوت 
class Person :
  hight = ""
  age = 0
  gender = ""
age_ahmed = input("Enter Ahmed age :\n")
age_nada = input("Enter nada age :\n")
hight_ahmed = input("Enter Ahmed hight :\n")
hight_nada = input("Enter nada hight :\n")
ahmed = Person()
ahmed.hight = float(hight_ahmed)
ahmed.age = float(age_ahmed)
ahmed.gender = "Male"
nada = Person()
nada.hight = float(hight_nada)
nada.age = float(age_nada)
nada.gender = "Female"
print(f"Nada is a {nada.gender} and Ahmed is a {ahmed.gender}\nNada is {nada.age} years old and Ahmed is {ahmed.age} years old\nNada is {nada.hight} cm and Ahmed is {ahmed.hight} cm")