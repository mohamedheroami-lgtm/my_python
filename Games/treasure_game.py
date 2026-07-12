print("""
꧁⎝ 𓆩༺✧༻𓆪 ⎠꧂
""")
print("Welcome to my lsland!")
print("There are two doors in front of you blue door and red door" )
ga = input ("select one door :\n")
if ga.lower() == ("blue"):
    print("oops you select the crocodile door.")
    print("Game over ! 🐊🐊🐊")
elif ga.lower() == ("red"):
    print("Great ! now you entered a room.")
    print("You found three boxes: white, 🎁 black, 🎁 green, 🎁")
    ha = input("Which box do you open ?\n")
    if ha.lower() == "white":
        print("oops! you opened a box filled with snakes 🐛🐛🐛")
    elif ha.lower() == "black":
           print("Oops! you opened a box filled with spiders 🕷️🕷️🕷️")
    elif ha.lower() == "green":
           print("congratultions! you found the treasure! 🎉🎉🎉")
           print ("The treasure is you 🙈")
    else:
           print("invalid choice! 🤦🤦🤦")
else:
    print("invalid choice! 🤦🤦🤦")          