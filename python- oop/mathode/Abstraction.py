


 #absraction  

"""
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
s1 = Shape(20,30)
s1.area()

t1 = Triangle(20, 30)
t1.area()

r1 = Rectangle(20, 30)
r1.area()

# overriding mathod = bar bar class niya kaj niya kaj kora jai


"
from abc import ABC, abstractmethod

# Shape নামে একটি Abstract Base Class (ABC) তৈরি করা হচ্ছে
class Shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass

# Triangle ক্লাসটি Shape ক্লাস থেকে ইনহেরিট করছে
class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print(f"Area of triangle: {area}")

# Rectangle ক্লাসটি Shape ক্লাস থেকে ইনহেরিট করছে
class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print(f"Area of rectangle: {area}")

# Triangle এর জন্য একটি অবজেক্ট তৈরি এবং area() মেথড কল করা
t1 = Triangle(20, 30)
t1.area()

# Rectangle এর জন্য একটি অবজেক্ট তৈরি এবং area() মেথড কল করা
r1 = Rectangle(20, 30)
r1.area()
"""




 #absraction  




 #absraction  
from abc import ABC,abstractmethod

class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    @abstractmethod
    def area(self):
       
      pass

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