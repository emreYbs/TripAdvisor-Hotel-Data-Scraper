#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as soup


# In[2]:

html = requests.get("https://www.tripadvisor.com/Hotel_Review-g274887-d7306673-Reviews-Aria_Hotel_Budapest_by_Library_Hotel_Collection-Budapest_Central_Hungary.html")
# html = requests.get('https://www.tripadvisor.in/Hotels-g187147-Paris_Ile_de_France-Hotels.html')
html.status_code


# In[3]:


bsobj = soup(html.content,'lxml')


# In[4]:


hotel = []
for name in bsobj.findAll('div',{'class':'listing_title'}):
    hotel.append(name.text.strip())
   
    
hotel


# In[5]:


ratings = []
for rating in bsobj.findAll('a',{'class':'ui_bubble_rating'}):
    ratings.append(rating['alt'])
    
ratings
    


# In[6]:


reviews = []

for review in bsobj.findAll('a',{'class':'review_count'}):
    reviews.append(review.text.strip())

reviews


# In[7]:


price = []

for p in bsobj.findAll('div',{'class':'price-wrap'}):
    price.append(p.text.replace('₹','').strip())
    
price[:5]


# In[8]:


len(price)


# In[9]:


d1 = {'Hotel':hotel,'Ratings':ratings,'No_of_Reviews':reviews,'Price':price}


# In[10]:

import pandas as pd


# In[11]:

df = pd.DataFrame.from_dict(d1)
df

