
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


census_data = pd.read_csv("data/census.csv")
census_data = census_data.drop(['Unnamed: 0'], axis = 1)

mortality_data = pd.read_csv("data/mortality_grouped.csv")
mortality_data = mortality_data.drop(['Unnamed: 0'], axis = 1)

df = mortality_data.merge(census_data, on='ResidencePlace')
df['death_rate'] = (df['Deaths']/df['respop72017']) * 1000
df.head()


# In[ ]:


if 'total' not in os.listdir('data/'):
    os.mkdir('data/total/')

quantiles = df['death_rate'].quantile([0.20, 0.40, 0.60, 0.80, 1.0]).get_values()

## 0% -20%
df_20 = df[df['death_rate'] <= quantiles[0]].sort_values(by=['death_rate'], ascending = False)
df_20.to_csv('data/total/percentile_20.csv')

## 21% - 40%
df_40 = df[(df['death_rate'] <= quantiles[1]) & 
                 (df['death_rate'] > quantiles[0])].sort_values(by=['death_rate'], ascending = False)
df_40.to_csv('data/total/percentile_40.csv')

## 41% - 60%
df_60 = df[(df['death_rate'] <= quantiles[2]) & 
                 (df['death_rate'] > quantiles[1])].sort_values(by=['death_rate'], ascending = False)
df_60.to_csv('data/total/percentile_60.csv')

## 61% - 80%
df_80 = df[(df['death_rate'] <= quantiles[3]) & 
                 (df['death_rate'] > quantiles[2])].sort_values(by=['death_rate'], ascending = False)
df_80.to_csv('data/total/percentile_80.csv')

## 81% - 100%
df_100 = df[(df['death_rate'] <= quantiles[4]) & 
                  (df['death_rate'] > quantiles[3])].sort_values(by=['death_rate'], ascending = False)
df_100.to_csv('data/total/percentile_100.csv')


# In[ ]:


if 'urban' not in os.listdir('data/'):
    os.mkdir('data/urban/')

df_urban = df[df['ResidenceZone'] == 'URBANO']
quantiles = df_urban['death_rate'].quantile([0.20, 0.40, 0.60, 0.80, 1.0]).get_values()

## 0% -20%
df_20 = df_urban[df_urban['death_rate'] <= quantiles[0]].sort_values(by=['death_rate'], ascending = False)
df_20.to_csv('data/urban/percentile_20.csv')

## 21% - 40%
df_40 = df_urban[(df_urban['death_rate'] <= quantiles[1]) & 
                 (df_urban['death_rate'] > quantiles[0])].sort_values(by=['death_rate'], ascending = False)
df_40.to_csv('data/urban/percentile_40.csv')

## 41% - 60%
df_60 = df_urban[(df_urban['death_rate'] <= quantiles[2]) & 
                 (df_urban['death_rate'] > quantiles[1])].sort_values(by=['death_rate'], ascending = False)
df_60.to_csv('data/urban/percentile_60.csv')

## 61% - 80%
df_80 = df_urban[(df_urban['death_rate'] <= quantiles[3]) & 
                 (df_urban['death_rate'] > quantiles[2])].sort_values(by=['death_rate'], ascending = False)
df_80.to_csv('data/urban/percentile_80.csv')

## 81% - 100%
df_100 = df_urban[(df_urban['death_rate'] <= quantiles[4]) & 
                  (df_urban['death_rate'] > quantiles[3])].sort_values(by=['death_rate'], ascending = False)
df_100.to_csv('data/urban/percentile_100.csv')


# In[ ]:


if 'rural' not in os.listdir('data/'):
    os.mkdir('data/rural/')

df_rural = df[df['ResidenceZone'] == 'RURAL']
quantiles = df_rural['death_rate'].quantile([0.20, 0.40, 0.60, 0.80, 1.0]).get_values()

## 0% -20%
df_20 = df_rural[df_rural['death_rate'] <= quantiles[0]].sort_values(by=['death_rate'], ascending = False)
df_20.to_csv('data/rural/percentile_20.csv')

## 21% - 40%
df_40 = df_rural[(df_rural['death_rate'] <= quantiles[1]) & 
                 (df_rural['death_rate'] > quantiles[0])].sort_values(by=['death_rate'], ascending = False)
df_40.to_csv('data/rural/percentile_40.csv')

## 41% - 60%
df_60 = df_rural[(df_rural['death_rate'] <= quantiles[2]) & 
                 (df_rural['death_rate'] > quantiles[1])].sort_values(by=['death_rate'], ascending = False)
df_60.to_csv('data/rural/percentile_60.csv')

## 61% - 80%
df_80 = df_rural[(df_rural['death_rate'] <= quantiles[3]) & 
                 (df_rural['death_rate'] > quantiles[2])].sort_values(by=['death_rate'], ascending = False)
df_80.to_csv('data/rural/percentile_80.csv')

## 81% - 100%
df_100 = df_rural[(df_rural['death_rate'] <= quantiles[4]) & 
                  (df_rural['death_rate'] > quantiles[3])].sort_values(by=['death_rate'], ascending = False)
df_100.to_csv('data/rural/percentile_100.csv')

