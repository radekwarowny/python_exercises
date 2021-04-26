# Reqirement: 
# pip3 install gkeepapi


import csv
import gkeepapi

keep = gkeepapi.Keep()
success = keep.login('example@gmail.com', 'password')

gnotes = keep.all()

exercises = []

n = 1
for i in gnotes:

    single_ex = i.text.split('\n')
    exercises.append(single_ex)
    n += 1

for i in range(len(exercises)):
    while ('' in exercises[i]):
        exercises[i].remove('')

result = sum(exercises, [])
for i in result:
    print(i)
    
    
# testing pandas 

#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd


# In[81]:


import re


# In[82]:


df = pd.read_csv('gym_notes.txt', delimiter = '\n')


# In[83]:


df['Exercises'] = df['Exercises'].str.lower()


# In[84]:


df['Ex_name'] = df['Exercises'].str.extract('([A-Za-z]+)')


# In[85]:


df['Ex_num'] = df['Exercises'].str.replace('([A-Za-z]+)', '')


# In[86]:


df.head()


# In[87]:


df.Ex_name.unique()


# In[88]:


df['Ex_name'] = df['Ex_name'].replace('trap', 'traps')


# In[89]:


df['Ex_name'] = df['Ex_name'].replace('tof', 'top')


# In[90]:


df['Ex_name'] = df['Ex_name'].replace('ches', 'chest')


# In[91]:


df['Ex_name'] = df['Ex_name'].replace('lar', 'lat')


# In[92]:


df['Ex_name'] = df['Ex_name'].replace('dead', 'deadlift')


# In[93]:


df['Ex_name'] = df['Ex_name'].replace('overhead', 'overhead press')


# In[94]:


df['Ex_name'] = df['Ex_name'].replace('pull', 'pull up')


# In[95]:


df['Ex_name'] = df['Ex_name'].replace('chest', 'chest press')


# In[96]:


df['Ex_name'] = df['Ex_name'].replace('face', 'face pull')


# In[97]:


df['Ex_name'] = df['Ex_name'].replace('dumbbell', 'dumbbell rows')


# In[98]:


df['Ex_name'] = df['Ex_name'].replace('overhead', 'overhead press')


# In[99]:


df['Ex_name'] = df['Ex_name'].replace('front', 'front squat')


# In[100]:


df['Ex_name'] = df['Ex_name'].replace('shoulder', 'back shoulder press')


# In[101]:


df['Ex_name'] = df['Ex_name'].replace('top', 'top fly')


# In[102]:


df['Ex_name'] = df['Ex_name'].replace('down', 'down fly')


# In[103]:


df['Ex_name'] = df['Ex_name'].replace('low', 'low fly')


# In[104]:


df['Ex_name'] = df['Ex_name'].replace('overhead', 'overhead press')


# In[105]:


df['Ex_name'] = df['Ex_name'].replace('incline', 'incline bench')


# In[106]:


df['Ex_name'] = df['Ex_name'].replace('barbell', 'chest press')


# In[107]:


df['Ex_name'] = df['Ex_name'].replace('overhead', 'overhead press')


# In[108]:


df['Ex_name'] = df['Ex_name'].replace('squad', 'squat')


# In[109]:


df['Ex_name'] = df['Ex_name'].replace('barbel', 'chest press')


# In[110]:


df['Ex_name'] = df['Ex_name'].replace('right', 'right chest press')


# In[111]:


df['Ex_name'] = df['Ex_name'].replace('crunch', 'crunches')


# In[112]:


df['Ex_name'] = df['Ex_name'].replace('single', 'single leg split')


# In[113]:


df['Ex_name'] = df['Ex_name'].replace('windshield', 'windshield wiper')


# In[114]:


df['Ex_name'] = df['Ex_name'].replace('wide', 'wide angle press')


# In[115]:


df['Ex_name'] = df['Ex_name'].replace('reverse', 'crunch')


# In[116]:


df['Ex_name'] = df['Ex_name'].replace('step', 'step lounges')


# In[117]:


df['Ex_name'] = df['Ex_name'].replace('behind', 'behind dumbell fly')


# In[118]:


df['Ex_name'] = df['Ex_name'].replace('stretch', 'low stretch fly')


# In[119]:


df['Ex_name'] = df['Ex_name'].replace('from', 'front squat')


# In[120]:


df['Ex_name'] = df['Ex_name'].replace('swimmers', 'swimmers press')


# In[121]:


df['Ex_name'] = df['Ex_name'].replace('back', 'back shoulder press')


# In[122]:


df['Ex_name'] = df['Ex_name'].replace('prone', 'prone ext.')


# In[123]:


df['Ex_name'] = df['Ex_name'].replace('alt', 'alt leg/arm rises')


# In[124]:


df['Ex_name'] = df['Ex_name'].replace('rear', 'rear delt')


# In[125]:


df['Ex_name'] = df['Ex_name'].replace('quat', 'squat')


# In[126]:


df['Ex_name'] = df['Ex_name'].replace('should', 'shoulder press')


# In[127]:


df['Ex_name'] = df['Ex_name'].replace('exp', 'explosive squat')


# In[128]:


df.Ex_name.unique()


# In[ ]:




