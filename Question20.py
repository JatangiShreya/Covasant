# ######################DAY-10####################
# pandas

# Question-20
# # A. Daily attendance of bike tracks
# every row contains the number of bicycles on every track of the city(montreal), 
# for every day of the year.
# Can you infer anything from the attendence record?

# url = "https://raw.githubusercontent.com/ndas1971/Misc/master/bikes.csv"

# 1. Read 
# 2. Check head 
# 3. Check summary statistics 
# 4. plot the daily attendance of two tracks, 'Berri1', 'PierDup'
# 5. Check index , explore weekday_name attributes 
# 6. Get sum of all attendance as a function of the weekday
# 7. Display this in figure , what is the inference?


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path=r"bikes.csv"
df=pd.read_csv(path)
# 1. Read 
df
# 2. Check head
df.head() 
# 3. Check summary statistics 
df.describe()
# 4. plot the daily attendance of two tracks, 'Berri1', 'PierDup'

# 5. Check index , explore weekday_name attributes
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['weekday']=df['Date'].dt.dayofweek

# 6. Get sum of all attendance as a function of the weekday
weekday_sum = df.groupby('weekday')['Total_Attendance'].sum()



# 7. Display this in figure , what is the inference?
df['Weekday'] = df['Date'].dt.day_name()
attendance_by_weekday = df.drop(columns='Date').groupby('Weekday').sum()
attendance_by_weekday.plot(kind='bar', figsize=(10,6))
plt.title('Sum of Attendance by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Total Attendance')
plt.tight_layout()
plt.show()