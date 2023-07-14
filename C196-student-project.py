#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name: ")
print("Clean the data and show which top 10 countries has the highest Undernourished rate as compared with their Population")
print("Show a comparison between Meat and Vegetables consumption across the countries")


# In[2]:


#predefine code for image
from IPython.display import Image
Image(filename='healthy.jpg') 
#predefine code end


# # Activity - 1 Clean the data and show which top 10 countries has the highest Undernourished rate as compared with their Population

# In[3]:


#import the required packages 
import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file.
df = pd.read_csv("COVID-19 Healthy Diet Dataset.csv")
df


# In[4]:


#Cleaning data
df.replace("<2.5", int(3), inplace=True)
df


# In[5]:


#Converting object datatype column to float datatype
df['Undernourished'] = df["Undernourished"].astype(float)
df


# In[6]:


#Groupby country and apply sum on Undernourished and Population column and create a new dataframe out of it
group_country = df.groupby('Country')[['Undernourished','Population']].sum().reset_index()
group_country


# In[7]:


#Sort the new dataframe as per Undernourished column
sorted_by_undernourished = group_country.sort_values(by=['Undernourished'], ascending=False)
sorted_by_undernourished


# In[8]:


#Get the top 10 countries from the sorted data
top_10 = sorted_by_undernourished.head(10)

#Convert Undernourished percentage to number and add a new column to the top 10 countries dataframe
top_10['percentage_number'] = top_10['Undernourished']/100 * top_10['Population']
top_10


# In[9]:


#Plot a stacked bar graph for showing the Population vs Undernourished rate
total_population = top_10['Population']
percent_number = top_10['percentage_number']

index = top_10['Country']
plt.subplots(figsize=(10,8))
plt.title('Top 10 countries with highest Undernourished rate ', fontsize=20)
plt.bar(index, total_population, bottom=percent_number , color='blue', label='Country Population') 
plt.bar(index, percent_number ,  color='purple', label = 'Undernourished') 
plt.xticks(rotation=80)
plt.legend()
plt.xlabel("Country")
plt.ylabel("Population and  Undernourished")
plt.show()


# Conclusion - 

# # Activity - 2 Show a comparison between Meat and Vegetables consumption across the countries

# In[10]:


#Sort the big dataframe as per Meat consumption
sorted_meat = df.sort_values(by=['Meat'], ascending=False)
sorted_meat


# In[11]:


#Sort the big dataframe as per Vegetables consumption
sorted_vegetables = df.sort_values(by=['Vegetables'], ascending=False)
sorted_vegetables


# In[12]:


#Plot a histogram showing the Meat consumption vs Vegetables consumption across countries 
plt.figure(figsize=(10,10))
plt.hist(sorted_meat['Meat'].head(50), bins=10, label="Meat")
plt.hist(sorted_vegetables['Vegetables'].head(50), bins=10, label = "Vegetables")
plt.title("Meat consumption vs Vegetables")
plt.ylabel("Consumption Percentage")
plt.xlabel("Meat vs Vegetables")
plt.legend()
plt.show()


# Conclusion - 

# In[ ]:




