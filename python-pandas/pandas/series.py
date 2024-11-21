
# 
import pandas as pd
data = [1,2,3]
Falah = pd.Series(data)
print(Falah)

# index ber kore
import pandas as pd
data = [1,2,3,]
Falah = pd.Series(data)
print(Falah[0])

# value srial poribortton

import pandas as pd
data =[ 1,2,3]
Falah = pd.Series(data , index = ['x','y','z'])
print(Falah)
# value index
import pandas as pd
data =[ 1,2,3]
Falah = pd.Series(data , index = ['x','y','z'])
print(Falah [0])

#dictionary
import pandas as pd
Dictionary = {'day1 ': 100, 'day2':200 , 'day3': 300}
Falah = pd.Series(Dictionary)
print(Falah)


# dictinory index 
import pandas as pd
Dictionary = {'day1 ': 100, 'day2':200 , 'day3': 300}
Falah = pd.Series (Dictionary , index=['day1','day3'])
print(Falah)


import pandas as pd
Data = [1,2,3]
Falah = pd.Series(Data)
print(Falah[1])