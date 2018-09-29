
# coding: utf-8

# In[6]:


import geopandas as gpd
import unidecode
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


# In[7]:


os.system("wget 'https://raw.githubusercontent.com/miguelrios/atlaspr/master/geotiles/pueblos.json'")
os.system("mv 'pueblos.json' 'data/'")


# In[3]:


geo_muni = gpd.read_file('data/pueblos.json')
geo_muni.head()


# In[4]:


geo_muni.plot()


# In[5]:


municipalities = []

for i in range(0, 78):
    muni_raw = geo_muni['NAME'][i].split(" Municipio, Puerto Rico")[0]
    muni_clean = unidecode.unidecode(muni_raw)
    muni_upper = muni_clean.upper()
    municipalities.append(muni_upper)
    
geo_muni['NAME'] = municipalities


# In[7]:


census_data = pd.read_csv("data/census.csv")
census_data = census_data.drop(['Unnamed: 0'], axis = 1)
census_data.head()


# In[8]:


mortality_data = pd.read_csv("data/mortality_grouped.csv")
mortality_data = mortality_data.drop(['Unnamed: 0'], axis = 1)
mortality_data.head()


# In[8]:


df = mortality_data.merge(census_data, on='ResidencePlace')
df['death_rate'] = (df['Deaths']/df['respop72017']) * 1000
df.head()


# In[9]:


df[df['ResidencePlace'] == 'LAS PIEDRAS']


# In[10]:


geo_muni['death_rate'] = list(df.groupby(['ResidencePlace'])['death_rate'].sum())


# In[29]:


figure, ax = plt.subplots(1)

geo_muni.plot(column = 'death_rate', 
              scheme = 'quantiles', 
              legend = True, 
              ax = ax,
              edgecolor='1', 
              linewidth = 0.3)

fig = plt.gcf()
fig.set_size_inches(7, 6)
fig.set_dpi(150)
plt.title("Mortality rate per 1,000 individuals\n Timeframe from September 20, 2017 to June 2018\n (Top 10 municipalities with highest rate annotated)")
ax.set_axis_off()

## Plot Top 10 Municipalities with overall death 

## Maunabo
plt.text(-66.00, 17.84, 
         'Maunabo: ' + str(round(geo_muni[geo_muni['NAME'] == 'MAUNABO'].at[74, 'death_rate'], 2)), 
         fontsize = 9)
plt.arrow(-65.90, 17.90, 0.01, 0.08, head_width = 0.02)

## Vieques
plt.text(-65.70, 17.95,
        'Vieques: ' + 
         str(round(geo_muni[geo_muni['NAME'] == 'VIEQUES'].at[63, 'death_rate'], 2)),
        fontsize = 8)
plt.arrow(-65.55, 18.00, 0.07, 0.06, head_width = 0.02)

## Hormigueros
plt.text(-67.73, 18.21,
        'Hormigueros: ' + 
         str(round(geo_muni[geo_muni['NAME'] == 'HORMIGUEROS'].at[64, 'death_rate'], 2)),
         fontsize = 8)
plt.arrow(-67.27, 18.2, 0.12, -0.05, head_width = 0.02)

## Dorado
plt.text(-66.20, 18.50, 'Dorado: ' + 
         str(round(geo_muni[geo_muni['NAME'] == 'DORADO'].at[10, 'death_rate'], 2)), 
         fontsize = 8)
plt.arrow(-66.20, 18.49, -0.06, -0.04, head_width = 0.02)

## Guanica
plt.text(-67.35, 17.80, 'Guanica: ' + 
         str(round(geo_muni[geo_muni['NAME'] == 'GUANICA'].at[77, 'death_rate'], 2)), 
         fontsize = 8)
plt.arrow(-66.97, 17.85, 0.03, 0.05, head_width = 0.02)

## Morovis
plt.text(-66.37, 18.60, 'Morovis: ' + 
         str(round(geo_muni[geo_muni['NAME'] == 'MOROVIS'].at[28, 'death_rate'], 2)),
         fontsize = 8)
plt.arrow(-66.37, 18.58, -0.05, -0.22, head_width = 0.02)

## Utuado
plt.text(-67.10, 18.58, 'Utuado: ' +
         str(round(geo_muni[geo_muni['NAME'] == 'UTUADO'].at[34, 'death_rate'], 2)),
         fontsize=8)
plt.arrow(-66.85, 18.56, 0.15 , -0.30, head_width = 0.02)

## Luquillo
plt.text(-65.67, 18.45, 'Luquillo: ' +
        str(round(geo_muni[geo_muni['NAME'] == 'LUQUILLO'].at[26, 'death_rate'], 2)),
         fontsize = 8) 
plt.arrow(-65.66, 18.44, -0.05, -0.08, head_width = 0.02)

## Arecibo
plt.text(-66.65, 18.74, 'Arecibo: ' +
        str(round(geo_muni[geo_muni['NAME'] == 'ARECIBO'].at[2, 'death_rate'], 2)), fontsize = 8)
plt.arrow(-66.50, 18.71, -0.17, -0.30, head_width = 0.02)

## Sabana Grande
plt.text(-66.75, 17.8, 'Sabana Grande: ' +
         str(round(geo_muni[geo_muni['NAME'] == 'SABANA GRANDE'].at[66, 'death_rate'], 2)), fontsize = 8)
plt.arrow(-66.75, 17.86, -0.18,0.21, head_width = 0.02)

plt.axis('equal')
#plt.show()
plt.savefig('figs/puerto_rico_death_choropleth.png')

