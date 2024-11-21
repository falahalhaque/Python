"""
class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")


class Samsung(Phone):  # Inheriting from the Phone class
    def call(self):
        print("You can call with Samsung")

    def message(self):
        print("You can message with Samsung")

    def photo(self):
        print("You can take a photo with Samsung")


# Create an instance of Samsung and call its methods
s = Samsung()
s.message()
s.call()
s.photo()




####





class Student:
    def __init__(self,roll,id):
        
        self.roll = roll
        self.id = id

    def display(self):
        print(f"Roll: {self.roll}  Id: {self.id}")



falah = Student(101, 212010101)
falah.display()

laboni = Student(102, 212010134)
laboni.display()


"""

class student :
    def __init__(self,roll,gpa):
              self.roll = roll
              self.gpa = gpa

              def display(self):
                  print(f"Roll  :  {self.roll} , Gpa  {self.gpa}")

    falah = student(101,3,4)
    falah.display()
    korim = student (101,3,4)
    korim.display()
        