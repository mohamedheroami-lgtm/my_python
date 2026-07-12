order = input("Press enter to change the content .....")
main_list = ["Apple", "Orange"]
main_list_2 = [1, 2, 3]
main_list_3 = ["Kiwis", "Green"]
if order :
    print("Please just press enter")
else :
    main_list.insert(1,main_list_3)
    main_list.append(main_list_2)
    main_list.insert(3,"Orange")
    main_list.insert(4,"Kiwis")
    main_list.remove("Apple") 
    print(main_list)  