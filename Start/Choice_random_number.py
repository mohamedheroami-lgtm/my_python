for i in range (10):
    import random
    fa = random.randint(-5,5)
    da = fa/5
    if da >0:
        print("Its posativ !!")
    elif da ==0:
        print("Its Zero") 
    else:
        print("its negative !!") 
           
    print(da)