
# attendance management using set 
all_stdeunt={1001,1002,1003,1004,1005,1006,1007,1008}
print("Press ! for marks attendance\nPress 2 for View Attendance\nAfter veiw attendance and Exit to code...Press 3")
present_set=set()

while True :
    ch =int(input("Enter Choice : "))
    if ch==1:
        rollno=int(input("Enter Roll NO : "))
        if rollno in all_stdeunt:
            present_set.add(rollno)
            print(f"Attendence Mark {rollno} Successfully")
        else:
            print("This Roll No is Not Registered on Portal")
    elif ch==2:   
        print("Today's Present = ",present_set)
        print("Today's Absent Student = ",all_stdeunt-present_set )
    elif ch==3:
        break
    else :
         print("Invalid Choise...")


