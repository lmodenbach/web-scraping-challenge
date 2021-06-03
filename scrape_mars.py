#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import os
import pandas as pd
import requests 


# In[32]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# headline/story

url = 'https://redplanetscience.com/'
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')

news_title = soup.find_all("div", {"class": "content_title"})[0].text
news_note = soup.find_all("div", {"class": "article_teaser_body"})[0].text



# In[ ]:


# featured image

url = 'https://spaceimages-mars.com/'
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')

firsta = soup.find_all("a", {"class": "showimg fancybox-thumbs"})[0]
href = firsta.get("href")
featured_image_url = str(browser.url) + str(href)


# In[ ]:


# facts

url = 'https://galaxyfacts-mars.com/'
browser.visit(url)

tables = pd.read_html(url)
df = pd.DataFrame(tables[0])
df.columns = df.iloc[0]
df.drop(0, inplace=True)

text_file = open("index.html", "w", encoding="utf-8")
text_file.write(df.to_html())
text_file.close()


# In[55]:


# hemispheres

hemisphere_image_urls = []
img_url = ""
title = ""

for x in range(1, 8, 2):
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    a = soup.find_all("a", {"class": "itemLink product-item"})[x]
    
    title_tagged = a.h3
    title = title_tagged.text

    href = a.get("href")
    image_search_url = str(url) + str(href)

    browser.visit(image_search_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    a = soup.find_all("a")[3]
    href = a.get("href")
    img_url = str(url) + str(href)
    hemisphere_image_urls.append({"title":title, "img_url":img_url})


# In[56]:


return hemisphere_image_urls


# In[57]:


browser.quit()


# In[ ]:




