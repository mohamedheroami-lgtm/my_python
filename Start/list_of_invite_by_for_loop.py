attendees = []
ga = input("Enter names after comma\n").split(",")
attendees.extend(ga)
for person in attendees:
    print(person)
    answer = input ("Did the person come ?\n").capitalize()
    if answer == "Yes":
        print("Attendance confirmed")
    elif answer == "No":
       print("Attendance not confirmed")  
    else:
        print("In valid ")
      
          