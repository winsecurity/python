

class Student:

    def __init__(self,name,id):
        self.student_name=name
        self.student_id=id

    def addHobby(self,hobby):
        self.student_hobby=hobby

student1= Student("nikhil",955)
student1.addHobby("Chess")
print(student1.student_name)
print(student1.student_id)
print(student1.student_hobby)