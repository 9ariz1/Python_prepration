# Use **kwargs to display student info.
def student_info(**kwargs):
    print("Student Information:")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# function call
student_info(
    name="Ariz",
    roll_no=101,
    course="B.Tech",
    branch="CSE"
)
