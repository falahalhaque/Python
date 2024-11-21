"""
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









class Phone:
    def __init__(self) :
        print("You can call me")


class Samsung (Phone):
    def __init__(self) :
       super().__init__()
       print("You can message ")
  
p1 = Phone()
S1 = Samsung



"""
class Phone:
    def __init__(self):
        print("I am in phone class")

class Samsung(Phone):
    def __init__(self):

        super().__init__()
        print("I am in Samsung phone")

p1 = Phone()       
s1 = Samsung() 