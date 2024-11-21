"""class Student:
    def __init__(self, roll, student_id):
        self.roll = roll
        self.id = student_id

    def display(self):
        print(f"Roll: {self.roll}, Id: {self.id}")


# Creating an instance of Student
falah = Student(101, 212010101)
falah.display()

laboni = Student(103, 212010134)
laboni.display()

# Check if `falah` is an instance of the `Student` class
print(isinstance(falah, Student))  # This should print True if `falah` is an instance of `Student`



class Student :
    def __init__(self,id,gpa) :
        
     self.Id = id
     self.gpa = gpa
def display(self):

    print(f" id :  {self.Id} gpa : {self.gpa}")

falah = Student(101, 212010101)
falah.display()

laboni = Student(103, 212010134)
laboni.display()
print(isinstance(falah,Student))





class Student:
    def __init__(self, id, gpa):
        self.Id = id
        self.gpa = gpa

    def display(self):
        print(f"Id: {self.Id}, GPA: {self.gpa}")

# Creating instances of Student
falah = Student(101, 3.8)  # Assuming GPA is 3.8
falah.display()

laboni = Student(103, 3.9)  # Assuming GPA is 3.9
laboni.display()

# Check if `falah` is an instance of the `Student` class
print(isinstance(falah, Student)


######



class Student :
    gpa = ""
    id = ""


def display(self):
 print(f"gpa : {self.gpa}  Id : {self.id}")


falah = Student ()
falah.gpa  = 101
falah.id  = 212010101
falah.display()

laboni = Student ()
laboni.gpa = 103
laboni.id = 212010134
laboni.display()

###

class Student:
    def __init__(self, gpa, id):
        self.gpa = gpa
        self.id = id

    def display(self):
        print(f"gpa: {self.gpa}  Id: {self.id}")


# ফালাহ এর জন্য তথ্য সেট করা হচ্ছে
falah = Student(101, 212010101)
falah.display()

# লাবনী এর জন্য তথ্য সেট করা হচ্ছে
laboni = Student(103, 212010134)
laboni.display()





class Student:
    def set_value(self, gpa, id):
        self.gpa = gpa
        self.id = id

    def display(self):
        print(f"gpa: {self.gpa}  Id: {self.id}")


# ফালাহ এর জন্য তথ্য সেট করা হচ্ছে
falah = Student()  # উদাহরণ তৈরি করা হচ্ছে
falah.set_value(3.5, 101)
falah.display()

# লাবনী এর জন্য তথ্য সেট করা হচ্ছে
laboni = Student()  # উদাহরণ তৈরি করা হচ্ছে
laboni.set_value(3.6, 103)
laboni.display()

"""
class Student:
    def set_value(self, roll, id):
        self.roll = roll
        self.id = id

    def display(self):
        print(f"Roll: {self.roll}  Id: {self.id}")


# ফালাহ এর জন্য তথ্য সেট করা হচ্ছে
falah = Student()
falah.set_value(101, 212010101)
falah.display()

# লাবনী এর জন্য তথ্য সেট করা হচ্ছে
laboni = Student()
laboni.set_value(102, 212010134)
laboni.display()
