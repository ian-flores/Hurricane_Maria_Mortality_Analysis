
# coding: utf-8

# In[3]:


import pandas as pd
import os


# In[4]:


os.system("wget --output-document='data/mortality.xlsx' 'https://www.dropbox.com/s/k4wrb1ztwu0fwxh/Base%20de%20Datos%20Mortalidad%20en%20PR%20de%20septiembre%2018%20de%202017%20a%2011%20de%20junio%20de%202018%20entregada%20por%20Gobierno%20de%20PR%20al%20CPI.xls?dl=0'")


# In[5]:


data = pd.read_excel("data/mortality.xlsx")
data.head()


# In[6]:


data = data[data.ResidencePlace.str.contains('PUERTO RICO')]
data = data[data.ResidencePlace != 'PUERTO RICO, DESCONOCIDO']
data = data[data.ResidenceZone != 'DESCONOCIDO']


# In[7]:


df_grp = data.groupby(['ResidencePlace', 'ResidenceZone']).size().reset_index(name='Deaths')
df_grp.head()


# In[8]:


municipalities = df_grp.ResidencePlace.tolist()

for i in range(0,len(municipalities)):
    municipalities[i] = municipalities[i].split("PUERTO RICO, ")[1]


# In[9]:


df_grp.ResidencePlace = pd.Series(municipalities)
df_grp.head()


# In[10]:


df_grp.to_csv("data/mortality_grouped.csv")

