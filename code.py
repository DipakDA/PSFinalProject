import pandas as pd
import datetime
import calendar
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('EmployeeAttendance.xls')
#df = df.drop(labels = 'Employee', axis = 1)
Count_row = df.shape[0]
df['Day'] = np.nan
df['Minutes Worked'] = np.nan


for x in range(0,Count_row):
    df.at[x, 'In Time'] = str(df.at[x, 'In Time']).split(" ")[-1]
    df.at[x, 'Out Time'] = str(df.at[x, 'Out Time']).split(" ")[-1]
    temp = df.at[x, 'Punch Date'].split("/")
    date1 = datetime.date(int(temp[-1]), int(temp[1]), int(temp[0]))
    df.at[x, 'Day'] = date1.weekday()
    hours_worked = df.at[x, 'Worked Hours'].split(":")
    df.at[x, 'Minutes Worked'] = int(hours_worked[0]) * 60 + int(hours_worked[-1])


df = df.drop(labels = 'Worked Hours', axis = 1)

print(df.to_string())
plt.hist(df["Day"], bins = 7, rwidth = 1)
plt.show()
