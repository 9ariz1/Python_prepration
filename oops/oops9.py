# variable in class 

class Student():
    college="Integral University"
    def set_value(self,id,name,course):
        self.stu_id=id
        self.stu_name=name
        self.stu_course=course
    def det_value(self):
        print(f"College : {self.college}") # use self to current obj value 
        print(f"Student Id : {self.stu_id}")
        print(f"Student Name : {self.stu_name}")
        print(f"Student Course : {self.stu_course}")

ariz=Student()
#print(ariz.college)
ariz.set_value("2300100832","Mo Ariz","B.tech")
ariz.det_value()


saif=Student()
#print(ariz.college)
saif.set_value("1003","Saif Ahmad","B.tech")
saif.det_value()