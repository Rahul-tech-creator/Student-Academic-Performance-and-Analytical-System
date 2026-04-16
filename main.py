from student.student import Student
s = Student()

while True:
    print("\n1.Add 2.Display 3.Search 4.Delete 5.Update 6.Visualize 7.Exit")
    ch = input("Choice: ")

    if ch == '1':
        s.add_student()
    elif ch == '2':
        s.display_students()
    elif ch == '3':
        s.search_student()
    elif ch == '4':
        s.delete_student()
    elif ch == '5':
        s.update_student()
    elif ch == '6':
        s.visualize_data()
    elif ch == '7':
        print("Program Closed")
        break
    else:
        print("Invalid")
