class Recipe:
  def __init__(self,name,ingredients,time_cooking,instruction):
    self.name = name
    self.ingredients = ingredients
    self.time_cooking = time_cooking
    self.instruction = instruction
  def information(self):
    print(f"Name : {self.name}\nIngredients : {self.ingredients}\nTime for cooking : {self.time_cooking}\nInstruction :{self.instruction}")
def enter_information():
  name_recipe = input("Enter recipe name :\n")
  ingredients_recipe = input("Enter recipe ingredients :\n")
  time_for_cooking = input("Enter the currnt time for cooking :\n")
  recipe_ins = input("Enter recipe instruction :\n")
  return Recipe(name_recipe,ingredients_recipe,time_for_cooking,recipe_ins)
recipe1 = enter_information()
recipe1.information()
recipe2 = enter_information()
recipe2.information()