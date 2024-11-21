'''
# smane thaika - hoiya jai
stack


books = []

books.append('learn C')
books.append('learnC+') 

books.append('learn java')

books.append('learn python')
print(books)
books.pop()
print('now the top book is:',books[-1])

books.pop()
print('now the top book is:',books[-1])

books.pop()
if not books:

  print('now the book left:',books[-1])
  

from collections import deque

bank = deque(['falah','saloah','malah'])


print(bank)

bank.popleft()
bank.popleft()
bank.popleft()

print(bank)
if not bank:
    print('no person left:')
  
# smane thaika - hoiya jai
stack


#stark 

books = []
books.append('c')
books.append('c+')
books.append('java')
books.append('python')

books.pop()
print(books[-1])
books.pop()
print(books[-1])
books.pop()
print(books[-1])
books.pop()
if not books :
    print("now the books left:",[-1])


# queue line menten kore
# # queue er somoi // from collections import deque //
from collections import deque

bank = deque(['rany',"santa",'labony','rina'])
print(bank)

bank.popleft()
bank.popleft()

bank.popleft()   
bank.popleft()   

print(bank)
if not bank :
    print('the no personleft:')*121*52#

 '''

# qeue

from collections import  deque


bank = deque(['rany',"santa",'labony','rina'])

print(bank)

bank.popleft()


bank.popleft()


bank.popleft()


bank.popleft()

if not  bank:

 print("You Faltu man :",bank)