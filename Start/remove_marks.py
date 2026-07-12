import string
ga = input("Enter your string :\n")
la = ""
for i in ga :
    if i not in string.punctuation:
        la += i
print(la)        