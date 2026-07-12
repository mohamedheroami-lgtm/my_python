import random
words = ["orange","blue","ahmed","oil"]
num = random.randint(0,len(words)-1)
choice = words[num]
do = ["_"] * len(choice)
c = []
for i in choice :
    c.append(i)   
print(" ".join(do))
tries = 4
while "_" in do and tries > 0 :
      u = input("Enter one letter :").lower()
      if u in do :
          print("You have had already enterd that")
          print(f"You have {tries} try")
          continue 
      if u not in c :
       tries -=1  
       print(f"You have {tries} try")
      for  n in range(len(choice)) :
                   if choice[n] == u:
                       do[n] = u
                       print(f"You have {tries} try")
      print(" ".join(do))
    
if tries == 0:
    print("You loss")
else :
    print("You win")              