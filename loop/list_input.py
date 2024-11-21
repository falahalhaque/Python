""""# input list 
# 10 , 20, 30 ,40 
'''
n = input("Enter a text num:")

list = n.split()
sum = 0

for num in list():
    sum= sum + int(num)
    print(sum)
    
    # num ber chasck 

numofwords = 0
numofletter = 0
numofdigits = 0

text = input("Enter  text number:")


for x in text :
    
    if x >='a' and x <='z':
        numofletter = numofletter+1

    elif x >='1' and x <='9':
        numofdigits = numofdigits+1

    elif x ==" " :
        numofwords = numofwords+1
        print(numofletter)
    print(numofdigits)
    print(numofwords+1)




numofword = 0
numofdigite = 0
numofletter = 0
 
text = input("enter the text: ")

for x in text:
    x = x.lower()
    if x >='a' and x >='z':
             
             numofletter = numofletter+1
             
             
    elif x >='1' and x >='9':
             
             numofdigite = numofdigite+1

    elif x == ' ':
             
             numofletter = numofletter+1

             print(numofdigite)
             print(numofletter)
             print(numofletter)

 



n = input("Enter a text num:")

list = n.split()
sum = 0

for num in list():
    sum= sum + int(num)
    print(sum)

    '''

   # number chack

n = input("Enter the usger name:")
list = n.split()
sum = 0
for x in  list:
    sum =sum+int(x)
    print(sum)

"""

numofwords = 0
numofletter = 0
numofdigits = 0

text = input("Enter  text number:")


for x in text :
    
    if x >='a' and x <='z':
        numofletter = numofletter+1

    elif x >='1' and x <='9':
        numofdigits = numofdigits+1

    elif x ==" " :
        numofwords = numofwords+1
        print(numofletter)
    print(numofdigits)
    print(numofwords+1)
