""""

#  exercise
#triangle = 0.5 *base * height
  # area =  base * height

  
class Triangle :
      def __init__(self,base,height) :
            self.base  = base
            self.height = height

            def Calculate_area(self):
                area = 0.5 * base * height
                print("Area  =  ",area)

                t1 = Triangle(20,30)
                t1.Calculate_area()
                t1 = Triangle(20,30)
                t1.Calculate_area()


"""
#  exercise  |  Triangle  * calculate (create) 
 
#triangle = 0.5 *base * height
  # area =  base * height
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Area =", area)


# Create instances and calculate the area
t1 = Triangle(10, 30)
t1.calculate_area()

t2 = Triangle(20, 30)
t2.calculate_area()
