
# coding: utf-8

# In[1]:


import pandas as pd
import os
import unidecode


# In[2]:


# Link to get the census data
# https://factfinder.census.gov/bkmk/table/1.0/en/PEP/2017/PEPANNRES/0400000US72.05000 


# In[3]:


os.system("unzip data/PEP_2017_PEPANNRES.zip -d data/")


# In[4]:


data = pd.read_csv("data/PEP_2017_PEPANNRES.csv", encoding='latin-1')
data.head()


# In[5]:


municipalities = []

for i in range(0, 78):
    muni_raw = data['GEO.display-label'][i].split(" Municipio, Puerto Rico")[0]
    muni_clean = unidecode.unidecode(muni_raw)
    muni_upper = muni_clean.upper()
    municipalities.append(muni_upper)
    
data['ResidencePlace'] = municipalities 


# In[6]:


data_processed = data[['ResidencePlace', 'respop72017']]
data_processed.head()


# In[7]:


data_processed.to_csv("data/census.csv")


# In[8]:


os.system("rm data/PEP_2017_PEPANNRES.csv data/PEP_2017_PEPANNRES_metadata.csv data/PEP_2017_PEPANNRES.txt data/aff_download_readme.txt")

