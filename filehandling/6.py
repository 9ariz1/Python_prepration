print("Yahi hai")
with open("third.txt","a+") as h:
    name=input(" Enter name : ")
    enroll=int(input("Enter Enrolment : "))
    uni=input("Enter University : ")
    c=input("Enter Your Course : ")
    h.write(f"""
Name : {name} ,
Enrollment : {enroll},
University : {uni}, 
Course : {c}
""")
    print("Data append Succesfully")

    # Move the file pointer back to the beginning (offset 0)
    h.seek(0)
    data=h.read()
    print(data)