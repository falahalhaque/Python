

#
'''

< ------ __it___
<= ------ __ie___
> ------ __gt ___
>= ------ __ge ___
== ------ __eq ___
!= ------ __ne ___



class Bike :
    def __init__(self,name,color) :
        self.name = name
        self.color = color
    def display (self):
        print(f"Name = {self.name}, color{self.color}")

bike1 = Bike ("Yamaha R15","Blue")
bike2 = Bike("Yamaha FZ","Red")




# magic 
class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color


        
    def __str__(self) -> str:
        
        return (f"name = {self.name}, color = {self.color}")

    
    def display(self):
        print(f"name = {self.name}, color = {self.color}")

bike1 = Bike("Yamaha R15", "red")
bike2 = Bike("Yamaha R15", "green")

print(str(bike1))





class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __eq__(self, other) :
        return self.name == other.name and self.color == other.color
        
    def __str__(self) -> str:
        
        return (f"name = {self.name}, color = {self.color}")

    
    def display(self):
        print(f"name = {self.name}, color = {self.color}")

bike1 = Bike("Yamaha R15", "green")
bike2 = Bike("Yamaha R15", "green")

print(bike1  == bike2)

''' 
class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color
  
    def __eq__(self,  other) :
        return self.name == other.name and self.color == other.color
    
    def __str__(self) -> str:
        
        return (f"name = {self.name}, color = {self.color}")

def display(self):
        print(f"name = {self.name}, color = {self.color}")

bike1 = Bike("Yamaha R15", "green")
bike2 = Bike("Yamaha R15", "green")

print( bike1 == bike2)
 