import random
ga = random.randint(0,9)
fa = random.randint(0,9)
sa = random.randint(0,9)
ha = random.randint(0,9)
la = str(ga)
va = str(fa)
ma =str(sa)
ba = str(ha)
na =la+va+ma+ba
print(na)
ta = input("Enter the pin number :\n")
if len(ta) == 4:
    if ta == na:
        print("wilcome master")
    elif ta != na:
        print("You are not my master!!")
else:
    print("pleas enter 4 only")