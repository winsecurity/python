
class student:
    salary=0
    clg="rvr jc"
    def __init__(self,fname,lname,rollno):
        self.fname=fname
        self.lname=lname
        self.rollno=rollno
        
    def fullname(self):
        print(self.fname+" " +self.lname)
        
    def setSalary(self,pay):
        self.salary=pay

  
    
stu1=student("nikhil","sai",955)
stu1.setSalary(100)
stu2=student("gopi","ys",977)
stu2.setSalary(200)
print(stu1.clg)

