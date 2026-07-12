print("welcome to place the rabbit ")
field = [["🥦", "🥦", "🥦"], ["🥦", "🥦", "🥦"], ["🥦", "🥦", "🥦"]]
print(f"{field[0]} \n{field[1]} \n{field[2]}")
print("\nWhere should the rabbit go? 🐇")
position = input("Enter the row and the column\n")
row = int(position[0])
column = int(position[1])
field[row-1][column-1] = "🐇"
print("\n success...")
print(f"{field[0]} \n{field[1]} \n{field[2]}")