ca = []
ga = input("Add the first color you like :\n")
ca.append (ga)
ha = input("Do you want to add more color ? (yes) or (No) :\n")
if ha.lower() == "yes":
    la = input("What is it :\n")
    ca.append(la)
    print (ca)
else:
    print(ca)