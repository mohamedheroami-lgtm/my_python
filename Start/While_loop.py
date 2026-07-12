op = "0p1o2i3u4"
ep = input("Enter your password : \n")
try_p = 3
if ep == op :
    print("Correct password")
while try_p> 0:
    try_p -=1
    if op != ep :
 
        print("Uncorrect password")
        ep = input("Enter your password :\n")
    