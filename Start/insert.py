# اضافه قوائم لبعضها وطباعه محدده
fruit = [["banana","apple"],["orange","kewy"]]
print (fruit[0])
print(fruit[0][0])
print(fruit[0][1],fruit[1][1])
cake = [["Cake","Candy"]]
fruit.append(cake[0])
print(fruit)
# امر insert
books = ["book 2", "book 4", "book 6"]
books.insert(0,"book 1")
books.insert(2,"book 3")
books.insert(4,"book 5")
print(books)