import random
print ("Welcome to 'whose wallet'?")
print ("You will give me a list of your friends names ")
names = input ("Enter the names separated by a comma :\n ").split(",")
choose = random.randint(0,len(names)-1)
print (f"please ask {names[choose]} to take out his wallet. dinner is on you ")