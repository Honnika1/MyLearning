import pandas as pd
cars = pd.read_csv("E:/Pywd/Python_Practice/Car_Data.csv", sep = ",")
cars.head()
cars.count()
cars.dtypes
cars.sum()
cars.prod()
len(cars)
cars["Buy_Prob"].value_counts()
cars["Maintainence"].value_counts()
cars["No_of_Doors"].value_counts()
cars["Seating_Capcity"].value_counts()
cars["Boot_Space"].value_counts()
cars["Safety"].value_counts()
cars["Car_Acceptability"].value_counts()
cars.describe()

data = {'Buy_Prob':cars["Buy_Prob"], 'Maintainence':cars["Maintainence"], 'No_of_Doors':cars["No_of_Doors"], 'Seating_Capcity':cars["Seating_Capcity"], 'Boot_Space':cars["Boot_Space"], 'Safety':cars["Safety"], 'Car_Acceptability':cars["Car_Acceptability"]}
df = pd.DataFrame(data)
print(df)