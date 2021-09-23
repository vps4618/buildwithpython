class students:
    num_of_students=0
    def __init__(self,fname,lname,email):
        self.fname=fname
        self.lname=lname
        self.email=email

        students.num_of_students+=1

    def fullname(self):#this is a regular method(use self parameter)
        print(self.fname+" "+self.lname)
# pass a function to another function  and
# that function returns a function
# then it is called as a decorator
    @classmethod #(this a decorator) 
    def from_string(cls,data_string):#this is a class method
        firstname,lastname,email=data_string.split('-')#the items are spilted and goes to students class parameters
        return cls(firstname,lastname,email)
    @staticmethod#this is a static method
    def print_students():
        print(students.num_of_students)
#class method is a method which use parameter of its class name 

# stu1=students('vishwa','praveen','vishwapraveen4618@gmail.com')
# stu2=students('mandipa','perera','mandipa@gmail.com')

stu1_string='Vishwa-praveen-vishwapraveen4618@gmail.com'
stu2_string='mandipa-perera-mandipa@gmail.com'

stu1=students.from_string(stu1_string)
stu1.fullname() #THIS IS HOW WE CALL FOR CLASS METHODS

students.print_students()#this is how we call for static method