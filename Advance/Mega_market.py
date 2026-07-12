#مشروع مصغر لاداره دكان الفكره انه يتكون من اربعه ابعاد مبيعات وواردات  وتقرير وموارد بشريه
import time 
import json
import os 
shelves = { }
sells = {}
hr = {}
def clear():
  os.system("cls") if os.name == "nt" else os.system("clear")
def data_save_sells():
  with open("Sells_data.json","w") as op:
    json.dump(sells,op,indent=4)
def data_read_sells():
  global sells 
  try:
    with open("Sells_data.json","r") as op:
      sells = json.load(op)
  except FileNotFoundError:
    print("لا يوجد ملف سوف يتم انشاء ملف جديد")
def data_read():
  """داله تقرا نلف جيسون وتقوم بتخزين ناتج القراءه في الرام"""
  global shelves
  try:
    with open("market_data.json","r") as file:
      shelves = json.load(file)
      
  except FileNotFoundError:
    print("لا يوجد ملف سيتم انشاء ملف جديد")
def data_save():
  """داله تحفظ البيانات في ملف جيسون"""
  global shelves
  with open("market_data.json","w") as file:
    json.dump(shelves,file,indent=4)
def hr_save():
  global hr
  with open("hr_data.json","w") as od:
    json.dump(hr,od,indent=4)
def hr_read():
  global hr
  try:
    with open("hr_data.json","r") as od:
      hr = json.load(od)
  except FileNotFoundError:
    print("سوف يتم انشاء ملف")
def add(product,price,quantity,type):
  """داله بتضيف المنتجات الجديده او بتعدل على سعرها"""
  global shelves
  if product in shelves:
    ga = shelves[product]["quantity"]
    shelves[product] = {
    "price" : price,
    "quantity" : ga + quantity,
    "type" : type,
    }
  else:
    shelves[product] = {
    "price" : price,
    "quantity" : quantity,
    "type" : type,
  }

def remove(product):
  """داله تحذف البينات من القاموس"""
  if product in shelves :
    del shelves[product]
    print(f"{product} removed")
  else:
    print(f"{product} isnt finded")

def show_product():
  global shelves
  data_read
  print("Product     :   quantity     :   Price   :")
  te = "_"
  print(te*37)
  for product , info in shelves.items():
    type = info["type"]
    if type == "lb":
      print(f"{product}     :   {info["quantity"]} Lb   :   {info["price"]} $")
    elif type == "pic" :
      print(f"{product}     :   {info["quantity"]} pic   :   {info["price"]} $")
    else:
      print(f"{product}     :   {info["quantity"]} kg   :   {info["price"]} $")
  
    
    

def products():
  data_read()
  while True:
    
    ask =  int(input("1.Add product 🍇\n2.Remove product ⛔\n3.Modifying price 🔄\n4.Show product 🛂\n"))
    if ask == 1 or ask == 3:
      name_pro = input("Enter the name of the product :\n")
      price_pro = float(input("Enter the price of the product :\n"))
      quantity_pro = float(input("Enter the quantity of the product :\n"))
      type_pro = input("Enter the type of the product :\n")
      add(name_pro,price_pro,quantity_pro,type_pro)
      data_save()
    elif ask == 2 :
      name_pro = input("Enter the name of the product you want to remove :\n")
      remove(name_pro)
      data_save()
    elif ask == 4:
      show_product()
      if input("Continue ?") == "y":
        continue
      break
    else:
      print("Invalid")



def take(ba,ga,price,name,type):
  global shelves
  quantity_after = ba - ga
  shelves[name] = {
    "price" : price,
    "quantity" : quantity_after,
    "type" : type
  }


def calculat(quantity,price):
  total = price * quantity
  return total


def sell_today(product_selled,quantity_selled,paid):
  data_read_sells()
  if product_selled in sells:
    ga = sells[product_selled]["quantity"]
    ba = sells[product_selled]["total_cost"]
    sells[product_selled] = {
    "quantity" : ga + quantity_selled,
    "total_cost" : ba + paid
  }
  else:
    sells[product_selled] = {
      "quantity" : quantity_selled,
      "total_cost" : paid
    }
  data_save_sells()
def sell():
  data_read()
  show_product()
  quantity_buy = float(input("Enter the quantity of the product do you want to buy :\n"))
  name_pro_bought = input("Enter the name of the product that you want to buy :\n")
  cash = float(input("How much cash do you have : \n"))
  type_pro = input("Enter the type of product")
  if name_pro_bought in shelves:
    price_bought_pro = shelves[name_pro_bought]["price"]
    quantity = shelves[name_pro_bought]["quantity"]
  else:
    print("There is no such a product")
    return
    
  if quantity_buy > quantity:
    print("Out of product")
    return
  elif quantity_buy <= quantity:
    
    take(quantity,quantity_buy,price_bought_pro,name_pro_bought,type_pro)
    cost_price = calculat(quantity_buy,price_bought_pro)
    asked = input(f"The cost price is {cost_price} , do you want to buy ?\n")
    if asked == "y" and cash >= cost_price:
      sell_today(name_pro_bought,quantity_buy,cost_price)
      data_save()
    else:
      print("You have no enogh cash")



def show_report():
  global sells
  global shelves
  data_read_sells()
  total_item_sold = 0
  total_renevue = 0
  if not sells :
    print("No sells for this month")
  else:
    for produc , info in sells.items():
      type = "True"
      print(f"\nItem sold {produc} :\nThe sold quantity = {info["quantity"]} {type} \nThe Total reneveu = {info["total_cost"]} $")
      total_item_sold += info["quantity"]
      total_renevue += info["total_cost"]
  print(f"\nThe total quantity sold = {total_item_sold} {type} \nThe total renevue = {total_renevue} $")


def show_employs():
  global hr
  hr_read()
  total_cost_of_employs = 0
  print("Name     :   Salary     :   total   :")
  ta = "_"
  print(f"{ta*35}")
  for name_em , inf in hr.items():
    print(f"{name_em}     :   {inf["salary"]}  $   :   {inf["total"]} $")
    total_cost_of_employs += inf["total"]
  print(f"The total cost of employs = {total_cost_of_employs} $") 
def tax(income,benfit):
  salary = income + benfit
  if salary <= 5000 :
    salary_after_tax = salary*0.15
  elif salary > 5000:
    salary_after_tax = salary*0.20
  return salary - salary_after_tax
def salary_system():
  global hr
  hr_read()
  ask = int(input("1.add employ 🚹\n2.show employs 🚸:\n"))
  if ask == 1:
    show_employs()
    name = input("Enter the worker name :\n")
    salary = float(input("Enter the worker salary :\n"))
    bouns = float(input("Enter The worker bouns :\n"))
    total = tax(salary,bouns)
    hr[name] = {
    "salary" : salary,
    "bouns" : bouns,
    "total" : total,
  }
    hr_save()
  else:
    show_employs()




def budget():
  global hr 
  global sells
  hr_read()
  data_read_sells()
  la = 0
  for ga , ha in hr.items():
    la += ha["total"]
  fa = 0
  for va , ba in sells.items():
    fa += ba["total_cost"]
  print(f"The market monthly cost = {la}")
  print(f"The monthly income = {fa}")
  if la > fa :
    print("You have inability in your budget 😱")
  else:
    print(f"Your net income is {fa - la}")
    


while True :
  clear()
  print("************Welcome to PYTHON compony***********")
  run_prog = input("1.Store house 🛂\n2.Hr 🏳️‍🌈\n3.Order 🏧\n4.Show report 😇\n5.Budget 😶‍🌫️\nprees enter to logout ↩️\n")
  if run_prog == "1":
    products()
  elif run_prog == "2":
    salary_system()
    if input("Continue ?") == "y":
      continue
  elif run_prog == "3":
    while True:
      sell()
      if input("Continue") == "y":
        continue
      else:
        break
  elif run_prog == "4":
    show_report()
    if input("Continue ?") == "y":
      continue
  elif run_prog == "5":
    budget()
    if input("Continue ?") == "y":
      continue
  else:
    break
  


    
  