import random
import string
fq = input("Enter the number of the charcters in the password :\n")
sq = input("Enter the numbers of the letters in the password :\n")
thq = input("Enter the numbers of numbers in the password :\n")
foq = input("Enter the numbers of symbols in the password :\n")
ma =int(sq)+int(thq)+int(foq)
if ma != int(fq):
    print("Out of range")
ga = random.choices(string.digits, k=int(thq))
ha = random.choices(string.ascii_letters,k=int(sq))
va = random.choices(string.punctuation,k=int(foq))
ba = ("".join(ga))
ka = ("".join(ha))
ca = ("".join(va))
ra = ba+ka+ca
fa =[]
for i in ra:
    fa.append(i)
my = random.choices(fa, k =ma) 
my = ("".join(my))
print(f"Your new password is{my} ")
