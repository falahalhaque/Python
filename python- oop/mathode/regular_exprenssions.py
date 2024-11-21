####(Object return kore)
# match (fist count korle "yes" )
# search (je kuno jaigai maj holei "yes")
# findall(joto golo pabe sob gulo list akare kore dibe)

"""

# match

import re 
pattern = r"our"

if re.match(pattern,"   our county Bangladesh, in best plach"):
    print("Yes == Match")

else:
    print("No == Match")




# search
import re 
pattern = r"Bangladesh"

if re.search(pattern,"   My county Bangladesh, in best plach"):
    print("Yes == Match")

else:
    print("No == Match")




  # findall
import re 
pattern = r"in"

print (re.findall(pattern, "our county in Bangladesh, in best  in plach"))
















#####$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


#  ( obj + function)
#search ()
# start(index num jei khanei pabe man bosai dibe)
#end(man pabar por tar seser value bole dibe)
#span(suro abong ses dui tar value dekha be)



import re 

pattern = r'colour'

text = "My favourit   e colour is blue"

match = re.search(pattern,text)

if match :
    print(match.start())
    print(match.end())
    print(match.span())

    
"""
