
for i in range (1,100000000):
    fn = float(input(" "))
    sn = float(input(" "))
    op = input(" ")
    if  sn  == 0 and op == "/":
        print("You can not (/) on 0")
        print("done")   
    elif op == "+":
        print(fn+sn)
        print("done")
    elif op == "÷":
        print(fn/sn)   
        print("done")
    elif op == "×" :
        print(fn*sn)  
        print("done")   
    elif op == "-":
        print(fn-sn)
        print("done")
    
           

