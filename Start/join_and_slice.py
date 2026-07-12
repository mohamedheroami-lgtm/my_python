# its something that print the string insde the list whis no [ ] and you can control what is print betwen them
names = ["Ahmed","Omer","Khalid"]
print((",").join(names))
print("\n")
print(("\n").join(names))
print(("😔").join(names))
#by a variable
ga = "\n"
print((ga).join(names))
#silising
#print (names[x:y:z])
#x is the number that the  range will begin with 
#y is the number that the range will never reach by one number so that the ranger will stop in 2 
#z is how much do you want it to skip so he will go from 1 to 3 with no 2 if the z value was 2 and you can make it any number that you want
print(names[0:3:2])