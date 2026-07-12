you have :\n"))
x =[]
y = []
for i in range(1,oa+1):
    name = input("Enter the employ name :\n")
    y.append(name)
    
    salary = int(input("How much is his salary :\n"))
    bonus = input("how much bouns did he get ?\n")
    x.append(salary)
    x.append(int(bonus))
print(x)    
print(y)    
for n in range(0,oa):
         print(f"{n+1}\{y[n]}")
         ga = x[0:10:2]
         ha = x[1:10:2]
         print(ga[n]+ha[n])
         
