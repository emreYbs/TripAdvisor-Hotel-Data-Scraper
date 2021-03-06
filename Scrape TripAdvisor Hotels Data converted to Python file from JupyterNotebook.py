#EmreYbs
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
from bs4 import BeautifulSoup as soup


# %%
# You may encounter an issue here. I can get successful StatusCode 200 in my country
# but with some foreigh destinations, I need to rerun this step for a couple of times. I'll try to fix it.
html = requests.get('https://www.tripadvisor.com.tr/Hotels-g14984534-Marmaris_District_Mugla_Province_Turkish_Aegean_Coast-Hotels.html')
html.status_code


# %%
bsobj = soup(html.content,'lxml')


# %%
hotel = []
for name in bsobj.findAll('div',{'class':'listing_title'}):
    hotel.append(name.text.strip())
     
hotel


# %%
ratings = []
for rating in bsobj.findAll('a',{'class':'ui_bubble_rating'}):
    ratings.append(rating['alt'])
    
ratings


# %%
reviews = []

for review in bsobj.findAll('a',{'class':'review_count'}):
    reviews.append(review.text.strip())

reviews


# %%
price = []

for p in bsobj.findAll('div',{'class':'price-wrap'}):
    price.append(p.text.replace('TL','').strip())
    
price[:5]


# %%
len(price)


# %%
d1 = {'Hotel':hotel,'Ratings':ratings,'No_of_Reviews':reviews,'Price':price}


# %%
import pandas as pd


# %%
df = pd.DataFrame.from_dict(d1)
df


