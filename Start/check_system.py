ha = input("Do you have رخصه ?\n")
ga = int(input("How old are you ?\n"))
if ha.lower() == "yes" and ga >= 18:
    print("You can drive")
else:
    print ("You can not drive")