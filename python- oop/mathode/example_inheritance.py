""""# shape .  (Triangle | Rectangle)
# Triangle  = 0.5 * base * hieght
#Rectangle = base * height

class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am the area of the shape class.")

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print(f"Area of Triangle: {area}")

class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print(f"Area of Rectangle: {area}")

# Triangle এর জন্য একটি অবজেক্ট তৈরি
t1 = Triangle(10, 20)
t1.area()  # Triangle এর এরিয়া দেখাবে

# Rectangle এর জন্য একটি অবজেক্ট তৈরি
r1 = Rectangle(10, 20)
r1.area()  # Rectangle এর এরিয়া দেখাবে



#########################################################################################


# shape .  (Triangle | Rectangle)
# Triangle  = 0.5 * base * hieght
#Rectangle = base * height

class  Shape:
   def __init__(self,base,height) :
         self.base = base 
         self.height = height


def area(self):
   print("You can area st:")


class Triangle(Shape):
 def area (self):
  area = 0.5 * self.base*self.height
print("Triangle is Right value")

class Rectangle(Shape):

  def area  (self):

   area =  self.base*self.height
print("Rectangle is Right value")

T1 = Triangle(20,30)
T1.area()
R1 = Rectangle(30,40)
R1.area()

"""

# shape .  (Triangle | Rectangle)
# Triangle  = 0.5 * base * hieght
#Rectangle = base * height

class  Shape:
   def __init__(self,base,height) :
         self.base = base 
         self.height = height


def area(self):
   print("You can area st:")


class Triangle(Shape):
 def area (self):
  area = 0.5 * self.base*self.height
print("Triangle is Right value")

class Rectangle(Shape):

  def area  (self):

   area =  self.base*self.height
print("Rectangle is Right value")

T1 = Triangle(20,30)
T1.area()
R1 = Rectangle(30,40)
R1.area()

