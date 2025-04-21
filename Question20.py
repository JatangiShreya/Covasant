# ######################DAY-10####################
# pandas

#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pwd', '')


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 1. Read 

# In[21]:


path=r"bikes.csv"
df=pd.read_csv(path)
df


# 2. Check head

# In[22]:


df.head()


# 3. Check summary statistics 

# In[23]:


df.describe()


#  4. plot the daily attendance of two tracks, 'Berri1', 'PierDup'

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
path=r"bikes.csv"
fig, ((ax1)) = plt.subplots(1,1, figsize=(5,2.7),layout='tight')
bikes=pd.read_csv(path)
ax1.plot(bikes['Berri1'])
ax1.plot(bikes['PierDup'])


# In[ ]:


5. Check index , explore weekday_name attributes


# In[32]:


df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['weekday']=df['Date'].dt.dayofweek


# 6. Get sum of all attendance as a function of the weekday

# In[37]:


attendance_columns = ["Berri1", "CSC", "Mais1", "Mais2", "Parc", "PierDup", "Rachel1", "Totem_Laurier"]
df['Total_Attendance'] = df[attendance_columns].sum(axis=1)


# In[41]:


weekday_sum = df.groupby('weekday')['Total_Attendance'].sum()


# In[43]:


weekday_sum


# 7. Display this in figure , what is the inference?

# In[49]:


df['Weekday'] = df['Date'].dt.day_name()


attendance_by_weekday = df.drop(columns='Date').groupby('Weekday').sum()

attendance_by_weekday.plot(kind='bar', figsize=(10,6))
plt.title('Sum of Attendance by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Total Attendance')
plt.tight_layout()
plt.show()


#  2. Which gender survived more 

# In[5]:


path=r"titanic_train.csv"
df2=pd.read_csv(path)
df2


# 2. Which gender survived more 
# 

# In[ ]:


gr=df2.groupby('sex').agg({'survived':'sum'}).reset_index()
gr.sort_values('survived',ascending=False)
gr.head(1)


# 3. Does it depend on pclass?:Yes

#  4. can we see % of survival of each gender and pclass 

# In[43]:


gr=df2.groupby('pclass').agg({'pclass': 'sum','survived':'sum',})
gr['percentage']=gr['survived']/gr['pclass']
gr
gr=df2.groupby('sex').agg({'sex': 'count','survived':'sum'})
gr['percentage']=gr['survived']/gr['sex']
gr


#  1. Read and check data
path=r"federer.csv"
df2=pd.read_csv(path)
df2

#  2. How many % of matched won by our player? ('winner')

# In[45]:


matches_won = len(df2[df2['winner'] =='Roger Federer'])
total_match=len(df2)
win_per=(matches_won/total_match)*100
win_per


# In[ ]:


3. Proportion of double faults wrt total points in each match 
This number is an indicator of the player's state of mind, his level of self-confidence,  his willingness to take risks while serving, and other parameters.
columns:
'player1 double faults' and 'player1 total points total'
Display simple stats of above 


# In[63]:


df2['player1 double faults']/df2['player1 total points total']


#  4. Average Win per surface 

# In[75]:


dt=df2[df2['winner'] =='Roger Federer']
dt.groupby('surface').agg({'winner':['count']})/df2.groupby('surface').agg({'winner':['count']})


#  5. Display the proportion of double faults as a function of the tournament date, 'start date'
#  Trend: display average double faults in each year 

# In[ ]:




gr=df2.groupby('start date')
gr[['player1 double faults','player2 double faults']].mean()


#  D. 
#  Create two frequencies 5Hz and 50Hz sin signals 
#  Draw FFT components 

# In[132]:


import numpy as np
import matplotlib.pyplot as plt


sampling_rate = 1000  
duration = 1    


t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)


frequency_1 = 5  
amplitude_1 = 1
sine_wave_1 = amplitude_1 * np.sin(2 * np.pi * frequency_1 * t)


frequency_2 = 50  # Hz
amplitude_2 = 0.8
sine_wave_2 = amplitude_2 * np.sin(2 * np.pi * frequency_2 * t)


combined_signal = sine_wave_1 + sine_wave_2


fft_result = np.fft.fft(combined_signal)


frequencies = np.fft.fftfreq(combined_signal.size, d=1/sampling_rate)

positive_frequencies = frequencies[:combined_signal.size//2]
positive_fft_magnitude = np.abs(fft_result)[:combined_signal.size//2] * 2 / combined_signal.size 


plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, combined_signal)
plt.title('Combined Sine Waves (5 Hz + 50 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(positive_frequencies, positive_fft_magnitude, basefmt=" ")
plt.title('FFT Components')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.tight_layout()
plt.show()


# E. Plotting normal random numbers
# and show that addition of two Gaussian is Gaussian 
# and addition of all is Gaussian

# In[133]:


import numpy as np
import matplotlib.pyplot as plt

num_samples = 10000
num_additions = 10


gaussian_vars = np.random.normal(0, 1, size=(num_additions, num_samples))


sum_of_two = gaussian_vars[0] + gaussian_vars[1]


sum_of_all = np.sum(gaussian_vars, axis=0)




plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.hist(gaussian_vars[0], bins=50, density=True, alpha=0.6, color='blue', label='Gaussian 1')
plt.hist(gaussian_vars[1], bins=50, density=True, alpha=0.6, color='green', label='Gaussian 2')
plt.title('Individual Gaussian Samples')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()


plt.subplot(1, 3, 2)
plt.hist(sum_of_two, bins=50, density=True, alpha=0.6, color='red', label='Sum of Two')
mean_sum_two = np.mean(sum_of_two)
std_sum_two = np.std(sum_of_two)
x_plot = np.linspace(min(sum_of_two), max(sum_of_two), 100)
plt.plot(x_plot, (1 / (std_sum_two * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_plot - mean_sum_two) / std_sum_two) ** 2), color='black', label='Gaussian Fit')
plt.title('Sum of Two Gaussians')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

plt.subplot(1, 3, 3)
plt.hist(sum_of_all, bins=50, density=True, alpha=0.6, color='purple', label='Sum of All')
mean_sum_all = np.mean(sum_of_all)
std_sum_all = np.std(sum_of_all)
x_plot = np.linspace(min(sum_of_all), max(sum_of_all), 100)
plt.plot(x_plot, (1 / (std_sum_all * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_plot - mean_sum_all) / std_sum_all) ** 2), color='black', label='Gaussian Fit')
plt.title(f'Sum of {num_additions} Gaussians')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

plt.tight_layout()
plt.show()


# In[ ]:




