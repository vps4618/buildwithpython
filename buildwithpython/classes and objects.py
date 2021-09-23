#classes and objects
class students:
    number_of_students=0
    def __init__(self,fname,lname,email):
        self.fname=fname
        self.lname=lname
        self.email=email
        students.number_of_students+=1
    def fullname(self):
         print(self.fname+" "+self.lname)
stu1=students("vishwa","praveen","vishwapraveen4618@gmail.com")
print(stu1.lname)
print(stu1.email)
print(stu1.fname)

print("")
stu2=students("Mandipa","Mevanjith","mandipa@gmail.com")
print(stu2.email)
print(stu2.fname)
print(stu2.lname)

stu3=students("Supun","Sanajana","supensanajana@gmail.com")

print(students.number_of_students)

print(stu1.fname+" "+stu1.lname)
print(stu2.fname+" "+stu2.lname)

print(" ")
stu1.fullname()
stu2.fullname()

print(" ")
students.fullname(stu1)
students.fullname(stu2)

print(" ")
#inheritance
class teachers(students):
    pass #pass use when we do nothing with this class

teacher1=teachers("Champika","Samarasinghe","champika@gmail.com")
teacher1.fullname()
print(teacher1.email)

teacher2=teachers("Nelum","Dilhani","nelumdilhani@gmail.com")
teacher2.fullname()
print(teacher2.fname)
print(teachers.number_of_students)