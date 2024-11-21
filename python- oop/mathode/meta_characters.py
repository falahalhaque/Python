# mata character
# ^(star somoi  thik e thakte hbe)$(ses e thik thakte hbe)
#*(0 or mor(je kuno ki so  thakei cholbe))
# (1 or more)
#?(0 or 1)
#{and}

# . character 
"""


import re
pattern = r"colo.r"
if re.match(pattern,"colour"):
    print("Match")

else:
    print("NO match")



# ^    |   $



import re
pattern = r"^colo.r$ "
if re.match(pattern,"colour"):
    print("Match")

else:
    print("NO match")

  
  



    #?(0 or 1)


import re
pattern = r"(ab)*"
if re.match(pattern,"aaaabcolour"):
    print("Match")

else:
    print("NO match")



    #?(0 or 1)
    # (1 or more)

    
import re
pattern = r"a-"
if re.match(pattern,"aar"):
    print("Match")

else:
    print("NO match")

    ####?
import re
pattern = r"ice(-)cram"
if re.match(pattern,"ice-cram"):
    print("Match")

else:
    print("NO match")
  

    ##{and}

       ####?
import re
pattern = r"a{1,25}$"
if re.match(pattern,"aaaaaaaaaaa"):
    print("Match")

else:
    print("NO match")
    

   
   
    


###################################################################################

#**********************
#*|Character classes|**


     ####?
import re
pattern = r"[jjcdfjdjc]"
if re.match(pattern,"ilfkdjfrofojir"):
    print("Match")

else:
    print("NO match")


    """