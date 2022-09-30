#!/usr/bin/env python
# coding: utf-8

# ## Cars in Ebay 
# The aim of this project is to clean the data and analyze them. 

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


autos=pd.read_csv("autos.csv",encoding="Latin-1")


# In[3]:


autos


# In[4]:


autos.info()


# In[5]:


autos.head()


# The types of columns are, for the most part, "object". The price is in dollar and the name of the car is very specific. 

# In[6]:


autos.columns


# In[7]:


autos.columns=['dateCrawled', 'name', 'seller', 'offerType', 'price', 'abtest',
       'vehicleType', 'registration_year', 'gearbox', 'powerPS', 'model',
       'odometer', 'registration_month', 'fuelType', 'brand',
       'unrepaired_damage', 'ad_created', 'nrOfPictures', 'postalCode',
       'lastSeen']


# In[8]:


autos.head()


# It was necessary to change the name of some columns to understand the dataset better. 

# In[9]:


autos.describe(include="all")


# The registration_year has several values that it's necessary to drop:  for example the max and min year. As well as the number of pictures column, where the value is 0. Month column needs more investigation in order to understand better the values. We have to transform the price and odometer as a different type instead of a text one

# In[10]:


autos["price"].value_counts()


# In[11]:


autos["odometer"].value_counts()


# In[12]:


autos["price"]=autos["price"].str.replace("$","").str.replace(",","").astype(int)
autos["odometer"]=autos["odometer"].str.replace("km","").str.replace(",","").astype(int)
autos.rename({"odometer":"odometer_km"},axis=1, inplace=True)


# In[13]:


autos.head()


# In[14]:


autos["odometer_km"].unique().shape


# In[15]:


autos["odometer_km"].describe()


# In[24]:


autos["odometer_km"].value_counts().sort_index(ascending=True).head()


# In[18]:


autos["price"].unique().shape


# In[19]:


autos["price"].describe()


# In[21]:


autos["price"].value_counts().head()


# In[25]:


autos["price"].value_counts().sort_index(ascending=True).head()


# In[26]:


autos["price"].value_counts().sort_index(ascending=False).head()


# In[30]:


autos=(autos[autos["price"].between(1, 500000)])


# In[32]:


autos["price"].describe()


# The price column was changed due to some problems with prices. The minimum price was 0, so it wasn't realistic and the maximum was 10000000. So, it was cut in a range between 0 and 500000

# In[39]:


autos["dateCrawled"].str[:10].value_counts(normalize=True, dropna=False).sort_index(ascending=True)


# In[40]:


autos["dateCrawled"].str[:10].value_counts(normalize=True, dropna=False).sort_values(ascending=True)


# It seems that the site was visited more on March and April.

# In[41]:


autos["ad_created"].str[:10].value_counts(normalize=True, dropna=False).sort_index(ascending=True)


# For the distribution the ads were created more on April and March

# In[44]:


autos["lastSeen"].str[:10].value_counts(normalize=True, dropna=False).sort_index(ascending=True)


# The first days of April shows an higher value, so it shows an higher presence of possible buyers during those days. Even though, this is not probably related to a higher amount of sales. 

# In[45]:


autos["registration_year"].describe()


# The registration year means when the car was produced. Some values are a bit strange, for example the minimum at 1000 and the maximum at 9999. 

# The realistic range, for me, for the autos sold in ebay during that periodo is between: 1900 and 2016

# In[47]:


autos["registration_year"].between(1900,2016).value_counts()


# In[48]:


1884/46681


# In[49]:


autos=autos[autos["registration_year"].between(1900,2016)]
autos["registration_year"].value_counts(normalize=True)


# So the percentage of error was nearly 4% so I dropped the rows with the unrealistic values. As we can see, the cars were produceded, for the most part, during 2000's.

# In[50]:


un=autos["brand"].unique()


# In[56]:


n_values=autos["brand"].value_counts(normalize=True)
top_brand=n_values[n_values>.05].index
print(top_brand)


# I took the top car producers that represents the 50% of the sold cars.

# In[68]:


brand={}
for i in top_brand:
    name=autos[autos["brand"]==i]
    price=name["price"].mean()
    brand[i]=int(price)


# In[69]:


print(brand)


# Mercedes, bwm and audi have the highest price

# In[70]:


bmp_series=pd.Series(brand)
df=pd.DataFrame(bmp_series, columns=["mean_price"])
df


# In[72]:


mileage={}
for i in top_brand:
    name=autos[autos["brand"]==i]
    media=name["odometer_km"].mean()
    mileage[i]=int(media)
mileage


# In[73]:


bmp_series1=pd.Series(mileage)


# In[74]:


df["bmp_series1"]=bmp_series1


# In[77]:


df.rename({"bmp_series1":"mean_mileage"},axis=1, inplace=True)


# In[78]:


df


# The mean mileage is similar for all the brands, while the price is different considering all the brands. 

# In[ ]:




