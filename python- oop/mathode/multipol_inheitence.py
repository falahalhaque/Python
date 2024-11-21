#multepol inheritence 
# A  , B  , c

"""class A:
    def deisplay1(self):
        print("I am inside A class")


class B:
    def deisplay2(self):
        print("I am inside B class")


class C (A,B):
    def deisplay3(self):
        print("I am inside C class") 
        
        
        obj = C()
        obj.display1()
        obj.display2()
        obj.display3()
        

 
class A:
    def display1(self):
        print("I am inside A class")

class B():
    def display2(self):
        print("I am inside B class")


class C(B,A):
    pass
   # def display3(self):
      
      #  print("I am inside C class")


obj = C()
obj.display1()  
obj.display2()
     


class A:
    def deisplay1(self):
        print("I am inside A class")


class B:
    def deisplay2(self):
        print("I am inside B class")


class C (A,B):
    def deisplay3(self):
        print("I am inside C class") 
        
        
        obj = C()
        obj.display1()
        obj.display2()
        obj.display3()




class A :
         def display1(self) :
           print("The reuslt is A ") 




class B(A):
         def display2(self) :
           print("The reuslt is B ") 


           
class C(B) :
         def display3(self) :
                     super().deisplay1
        super().deisplay2
           print("The reuslt is C ") 


ob1 = C() 

ob1.displary1()   
ob1.displary2()         
ob1.displary3()   


"""
class A:
    def display(self):
        print("I am inside A class")


class B:
    def display(self):
        print("I am inside B class")


class C(B, A):
    def display(self):
        print("I am inside C class")


# Object creation and method call
ob1 = C()
ob1.display()
