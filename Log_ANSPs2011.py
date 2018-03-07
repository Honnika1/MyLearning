import pandas as pd
logs = pd.read_csv("E:/Pywd/Python_Practice/Log_ANSPs2011.csv", sep = ",")
logs.head()
logs.count()
logs.dtypes
logs.sum()
logs.prod()
len(logs)
logs["Ops_Staff_Cost"].value_counts()
logs["Non_Ops_Staff_Cost"].value_counts()
logs["Other_Costs"].value_counts()
logs["Composite_Flight_Hours"].value_counts()
logs["Traffic_Variability_Index"].value_counts()
logs["Delays_Cost"].value_counts()
logs["No_of_Trainees"].value_counts()
logs["No_of_Assists_n_Support_Staff"].value_counts()
logs["No_of_Admin_Staff"].value_counts()
logs.describe()

data = {'Ops_Staff_Cost':logs["Ops_Staff_Cost"], 'Non_Ops_Staff_Cost':logs["Non_Ops_Staff_Cost"], 'Other_Costs':logs["Other_Costs"], 'Composite_Flight_Hours':logs["Composite_Flight_Hours"], 'Traffic_Variability_Index':logs["Traffic_Variability_Index"], 'Delays_Cost':logs["Delays_Cost"], 'No_of_Trainees':logs["No_of_Trainees"], 'No_of_Assists_n_Support_Staff':logs["No_of_Assists_n_Support_Staff"], 'No_of_Admin_Staff':logs["No_of_Admin_Staff"]}
df = pd.DataFrame(data)
print(df)