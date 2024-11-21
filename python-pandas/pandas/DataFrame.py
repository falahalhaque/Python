

# data frem 
import pandas as pd
Data = {'Marks': [350, 450, 500], 'Id': [101, 102, 103]}
Falah = pd.DataFrame(Data)
print(Falah)

# subseting 
import pandas as pd

Data = {'roll  ' : [101,102,103] , 'name' :['falah','labny','srabony']}
Falah = pd.DataFrame(Data)
print(Falah.loc[[0,2]])

#name index

import pandas as pd
Data = {'roll ': [101,102,103], 'name ' :['falah','labony','srabony']}
Falah = pd.DataFrame(Data ,index = ['day1','day2','day3'])
print(Falah)


import pandas as pd
fileload  = pd.read_csv('Data.csv'("C:\\Users\\DCL\\Documents\\Excle"))
print(fileload)


import pandas as pd
data = ['bangla','english','math'];
falah = pd.DataFrame(data);
print(falah[0].dtype);


import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Dhaka', 'Chittagong', 'Khulna']
}

df = pd.DataFrame(data)
print(df.shape)
