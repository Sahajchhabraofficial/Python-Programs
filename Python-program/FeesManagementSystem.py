#Fees management system.
students={"Jhon": {"rollno": 101, "fees_paid": 3000, "total_fees": 6000},
          "Alice": {"rollno": 102, "fees_paid": 4000, "total_fees": 6000},
          "Bob": {"rollno": 103, "fees_paid": 2000, "total_fees": 6000}}
print("======WELCOME TO FEE MANAGEMENT======")
print("what did you want to do?")
print("1.Pay Fees")
print("2.View fee details")
print("3.Register a student")
print("4.Exit")
choice=input("->")
if choice=='Pay Fees' or choice=='pay fees':
    rollno=input("Enter your roll number:")
    for student, details in students.items():
        if str(details["rollno"]) == rollno:
            print("Hello", student)
            print("Your total fees are:", details["total_fees"])
            print("Fees paid so far:", details["fees_paid"])
            print("Remaining fees:", details["total_fees"] - details["fees_paid"])
    amount=input("Enter the amount to be paid:")
    if int(amount)<=details["total_fees"] - details["fees_paid"]:
        details["fees_paid"] += int(amount)
        print("Payment successful! Updated fees paid:", details["fees_paid"])   
    else:
        print("Error: Amount exceeds remaining fees.")
    
elif choice=='View fee details' or choice=='view fee details':
    rollno=input("Enter your roll number:")
    for student, details in students.items():
        if str(details["rollno"]) == rollno:
            print("Fee Details for", student)
            print("Total Fees:", details["total_fees"])
            print("Fees Paid:", details["fees_paid"])
            print("Remaining Fees:", details["total_fees"] - details["fees_paid"])
            break
    else:
        print("Student with roll number", rollno, "not found.")
elif choice=='Register a student' or choice=='register a student':
    name=input("Enter student's name:")
    rollno=input("Enter student's roll number:")
    course=input("Enter course enrolled:")
    print("Student registered successfully!")
    print("Name:",name)
    print("Roll Number:",rollno)
    print("Course:",course)
    students[name] = {"rollno": rollno, "fees_paid": 0, "total_fees": 6000}
elif choice=='Exit' or choice=='exit':
    print("Exiting the system. Goodbye!")
else:
    print("Invalid choice!!")
    