#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#1. Which country consumes the most alcohol in total?

df = pd.read_csv('/Users/hannasharifi/Downloads/drinks.csv')

sorted_df = df.sort_values('total_litres_of_pure_alcohol', ascending=False).head(50)

plt.figure(figsize=(10, 10))  
plt.barh(sorted_df['country'], sorted_df['total_litres_of_pure_alcohol'], color='salmon')
plt.xlabel('Total Litres of Pure Alcohol')
plt.ylabel('Country')
plt.title('Top 50 Countries by Total Alcohol Consumption')
plt.margins(y=0.01)
plt.gca().invert_yaxis()  
plt.tight_layout()  
plt.show()


# In[6]:


#2. Which country consumes the most beer in total?

average_beer = df['beer_servings'].mean()

top_10_beer_countries = df.nlargest(10, 'beer_servings')

plt.figure(figsize=(30, 15))
plt.bar(top_10_beer_countries['country'], top_10_beer_countries['beer_servings'], color='green')
plt.axhline(y=average_beer, color='r', linestyle='-')

plt.text(x=0, y=average_beer+5, s=f"Global Average: {average_beer:.2f}", color='r', fontsize=20)
plt.margins(y=0.05)
plt.margins(x=0.01)

plt.title('Top 10 Countries by Beer Consumption', fontsize=30)
plt.xlabel('Country', fontsize=20)
plt.ylabel('Beer Servings', fontsize=20)

plt.xticks(rotation=45, fontsize=20)

plt.yticks(fontsize=15)

plt.show()


# In[4]:


#3. Is there a correlation between beer and spirit servings?

plt.scatter(df['beer_servings'], df['spirit_servings'])
plt.title('Correlation between Beer and Spirit Servings')
plt.xlabel('Beer Servings')
plt.ylabel('Spirit Servings')
plt.show()


# In[5]:


#4. What is the relationship between wine servings and total alcohol consumption?

plt.scatter(df['wine_servings'], df['total_litres_of_pure_alcohol'])
plt.title('Relationship between Wine Servings and Total Alcohol Consumption')
plt.xlabel('Wine Servings')
plt.ylabel('Total Litres of Pure Alcohol')
plt.show()

