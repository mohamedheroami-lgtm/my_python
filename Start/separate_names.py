names = input("Enter your first and last names :\n").split(",")
ca = []

for i in range (len(names)):
    ka = names[i].split(" ")
    print(ka)
    ca.append(ka)
print("Abbreviated name :") 
for o in range( len(ca)):
    fa = ca[o][0]
    na = ca [o][1]
    la=(fa[0])
    oa = (na[0])
    print(f"{la}.{oa}.")
