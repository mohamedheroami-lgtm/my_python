ga = [['🥦', '🥦', '🥦',], ['🥦', '🥦', '🥦'], ['🥦', '🥦', '🥦']]
print(f"{ga[0]}\n{ga[1]}\n{ga[2]}")
for i in range(1,10):
    print ("Enter where do you think that the rabbit will be in :")
    import random
    la = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
    ra = random.randint(0,8)
    va = la[ra]
    ya = int(va[0])
    ha = int(va[1])
    
    ja = input("Enter two number :\n")
    fa = int(ja[0])-1
    ba = int(ja[1])-1
    vv = (str(fa)+str(ba))
    
    if  vv == va :
        ga[ya][ha] = "🐇"
        
        print ("You win")
        print(f"{ga[0]}\n{ga[1]}\n{ga[2]}")
    else:
        print  ("You lose")
        print("The rabbit is in :")
        ga[ya][ha] = "🐇"
        print(f"{ga[0]}\n{ga[1]}\n{ga[2]}")  