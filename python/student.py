student = []
while True:
    print("\n STUDENT MENU")
    print("1. add student")
    print("2. view all student")
    print("3. search student by roll no.")
    print("4. delete student by roll no.")
    print("5. update student by roll no.")
    print("6. exit")

    choice = input("enter your choice(1-6):")

    if choice == "1":
        name = input("enter student name:")
        roll_no = input("enter  roll no.:")
        age = int(input("enter student age:"))
        course = input("enter student course:")
        student.append({"roll_no":roll_no,"name":name,"age":age,"course":course})
        print(f"\nsuccess:record for'{name}'added successfully!")
    elif choice == "2":
        if not student:
            print("\nno records found!please add a student first")
        else:
            print("\nSTUDENT LIST")
            print(f"{'roll no'} | {'name'} | {'age'} | {'course'}")
            print("_"*55)
            for s in student:
                print(f"{s['roll_no']}| {s['name']} | {s['age']} | {s['course']}")
    elif choice == "3":
        roll_no = input("enter roll no. to search:")
        found = False
        for s in student:
            if s['roll_no'] == roll_no:
                print(f"\nstudent found:\nroll no:{s['roll_no']}\nname:{s['name']}\nage:{s['age']}\ncourse:{s['course']}")
                found = True
                break
        if not found:
            print(f"\nno student found with roll no.{roll_no}")
    elif choice == "4":
        roll_no = input("enter roll no. to search:")
        found = False
        for s in student:
            if s['roll_no'] == roll_no:
                student.remove(s)
                print(f"\nsuccess:record for roll no.{roll_no} deleted successfully!")
                found = True
                break 
    elif choice =="5":
        roll_no = input("enter roll no. to search:")
        found = False
        for s in student:
            if s['roll_no'] == roll_no:
                name = input("enter new student name:")
                age = int(input("enter new student age:"))
                course = input("enter new student course:")
                s['name'] = name
                s['age'] = age
                s['course'] = course
                print(f"\nsuccess:record for roll no.{roll_no} updated successfully!")
                found = True
                break
        if not found:
            print(f"\nno student found with roll no.{roll_no}")    

    elif choice == "6":
        print("exiting program...goodbye!") 
        break
    else:
        print("invalid choice!please try again.")           

