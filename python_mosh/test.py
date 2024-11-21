'''print(9)
print("Falah al haque")
print("0---------")
print("@"*10)
print("0"*10)


price = 10

price = 20
print(price)

Red = input("Whats Your name ?")

color = input("Whats is your color?")

print( Red,'Fabourite color', color)



### birth year test


birth_yare = float (input("Birth Year :"))
print(type(birth_yare))
age = 2024.09 - birth_yare
print(type(age))
print(age)



### weight test 

weight_lbs = input('weight_lbs')

weight_kg = int(weight_lbs)*0.45
print(weight_kg)



#********** String  
name.upper()
name.lower()
name.title()
name.find()
name.replse()




## coloum test

course =  



The name is
falah  al haque
my id 212010101


 ##
print(course)


###   index test:

course = 'python for beginners'
print(course[-18])
print(course[0:2])
print(course[1:-1])

## replase (poribothon)

course = 'python for beginners'
print(course.replace('p','j '))


## title 


course = 'python for beginners'
print(course.title('R'))



#******* Arithmetic opretions


print(10//3)
print(10**3)
print(10 +3 * 2 ** 2)


#********* if statemant

##******** for loop

for item in range (5,10,2):
  print(item)

  

  #**Nested loops
for x in range(9):
    for y in range(8):

     print(f'({x},{y})')


##** Challenge


num =[4,5,3,2,2,1]
for x in num:
    print('x'* x)
    
#** list



## ** unpacking ( nirddito kore man ber kora)
coordinates = ('1p',2,3)

x,y,z = coordinates

print(x,y)

#################







##*** Dictionaries

phone = input("pohon : ")
digits_mapping = {
  '1':'one',
   '2': 'two',
   '3':'Three',
   '4':'four'
  
}
output =''
for ch in phone:
 output =+ digits_mapping.get(ch,'!') + "  "
 print(output)

 
 ##*** emoji converter

message = input(">")
words = message.split(' ')
emojis = {
" :)":"8"
":(" :"6

}
output = " "
for word in words :
 output =+ emojis.get(word,word) + " "

print(words) 


## Square ()

def square (number):
  return number*number
  result = square(3)

  print(result)

try:
  age =int(input('age :'))
 
  incame = 20000
  risk = incame / age
except ZeroDivisionError:
    print('Age cannot be o.')
except ValueError:
  print('invalid value')

### comments

### classes

class point :
  def _init_(self,x,y):
    self.x= x
    self.y = y


    def draw(self):
      print("draw")

      print1 = point()
      point1.x=10
      point1.y=20
   
      print(point.x)
      

      

class person :
  def talk (self):
    print("talk")


john = person()
john.talk()




command  = ""
while  True:
  command = input("> ").lower()
  if command == "Start":
         print("Car Started.........")
  elif command == "Stop":
    print("Car stoped.....")
  elif command == "Help":
  
  
    
  
   print 
   ("""
    srate - to asaratb
    stop - to satoip tghe ccar
   
     )"""







## modulas
import converters

print(converters.kg_to_lbs(70))  # This should print 154.3234



import random 

class Falah:
  def roll(self):
    first = random.random(1,6)
    second = random.random(1,6)
    return (first,second)


falah = falah()
print(Falah.roll())    

'''

from pathlib import Path
path =dict("ecmmerce")
print(dict.exists())