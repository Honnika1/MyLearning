import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('E:/Pywd/Python_Practice/vehicles.csv') as vehidata:
   vehiptd = np.loadtxt(vehidata, delimiter= ',', dtype="object", skiprows=0, usecols=59)
plt.hist(vehiptd, bins=35, color='purple')
plt.xlabel("Number")
plt.ylabel('Vehicles type')
plt.title("Distribution of Vehicles")

fig, ax=plt.subplots()
rects1=plt.hist(vehiptd, bins=35, color='red')
ax.set_xlabel("Number")
ax.set_ylabel('Vehicles type')
ax.set_title("Distribution of Vehicles")


vehi = pd.read_csv("E:/Pywd/Python_Practice/vehicles.csv", sep = ",")
vehi.count()
vehi.dtypes
vehi.head()