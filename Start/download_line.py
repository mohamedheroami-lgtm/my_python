import os
import time
print("Downloading GTA6")
def clear():
    os.system("clear")
list = ["░"]*20
for i in range(len(list)) :
        list[i]="█"
        print(f"{''.join(list)} {int((i+1)/len(list)*100)}%")
        time.sleep(0.3)
        clear()
print("GTA6 downloded")