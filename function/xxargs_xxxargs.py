
    # xxargs 
'''


def student(id,name):
   print(id,"name")

student(103,"laboni")



def student(*details):
   print(details)

student(103,"laboni")
student(104,"shaboni")
student(105,"kolamoni",3.90)

def add(num1,num2):
    sum = num1+ num2
    print(sum)

add(10,40)
add(12,111140)
add(10,40.999)




def add(*number):
    sum = 0

    for num in number:
        sum =sum +num
        print(sum)

add(10,40)
add(12,111140)
add(10,40.999)


# xxxargs

def student(**detaile):
    print(detaile)
    student(Id=101,name='Falah')

    

    
    # xxargs 



def student(id,name):
   print(id,"name")

student(103,"laboni")



def student(*details):
   print(details)

student(103,"laboni")
student(104,"shaboni")
student(105,"kolamoni")

'''


def student(**deteailes):
   print(deteailes)

student(id = 103, name ="laboni")