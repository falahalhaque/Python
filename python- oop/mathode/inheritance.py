"""
## inheritance = onno jonar kaj thaika nijer kase niya asa

class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am the area method of Shape class")


class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print(f"Area of triangle: {area}")


class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print(f"Area of rectangle: {area}")


# Create objects and call their methods
t1 = Triangle(20, 30)
t1.area()

r1 = Rectangle(20, 30)
r1.area()

# overriding mathod = bar bar class niya kaj niya kaj kora jai


class Phone:
    def __init__(self):
        print("I am in phone class")

class Samsung(Phone):
    def __init__(self):
        # Calling the constructor of the parent class (Phone)
        super().__init__()
        print("I am in Samsung phone")

# Creating objects of both classes
p1 = Phone()       # This will call the constructor of Phone
s1 = Samsung() 

class phone:
    def call (self):
        print("You can call ")

    def message (self):
        print("You can message ")    

class samsung (phone):
      def photo(self):
            print("You can photo")


s =samsung()  
s.message()
s.call()
s.photo()
print(isinstance(samsung,phone))



# inheritence onno jonar jinis nijew nkase niya asa


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
p = Phone()
p.call()
p.message()

# Create an instance of Samsung and call its methods
s = Samsung()
s.message()
s.call()
s.photo()

"""


# inheritance 



class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")


class Samsung(Phone): 
    # kiso man kete dile asbe na niya aste gele inheritence use korte hbe 
    # phone calss all methode samsung kase aise porbe

    def photo(self):
        print("You can take a photo with Samsung")




s = Samsung()
s.message()
s.call()
s.photo()

print(issubclass(Samsung,Phone))