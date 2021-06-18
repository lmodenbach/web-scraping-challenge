#!/usr/bin/env python
# coding: utf-8
 
#necessary imports

from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#define scraping code as a function

def scrape():

#create browser object and empty dictionary to be returned later

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_data_dict = {}

# collect headline/story, and add to return dictionary
      
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.find_all("div", {"class": "content_title"})[0].text
    news_note = soup.find_all("div", {"class": "article_teaser_body"})[0].text

    mars_data_dict.update({"news_title":news_title}) 
    mars_data_dict.update({"news_note":news_note})

# collect featured image url and add to return dictionary

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    firsta = soup.find_all("a", {"class": "showimg fancybox-thumbs"})[0]
    href = firsta.get("href")
    featured_image_url = str(browser.url) + str(href)

    mars_data_dict.update({"feat_img_url":featured_image_url})

# collect facts table html and add to return dictionary

    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    tables = pd.read_html(url)
    tables_df = pd.DataFrame(tables[0])
    tables_df.columns = tables_df.iloc[0]
    tables_df.drop(0, inplace=True)
    table_html = tables_df.to_html(index=False, border=4)
    mars_data_dict.update({"html":table_html})

# collect hemisphere titles and image urls and add to a dictionary just for them

    img_url = ""
    title = ""
    hemisphere_image_urls = []

    for x in range(1, 8, 2):
        hemisphere_entry = {}
        url = 'https://marshemispheres.com/'
        browser.visit(url)
        html = browser.html
        soup = bs(html, 'html.parser')
        a = soup.find_all("a", {"class": "itemLink product-item"})[x]
    
        img_title_tagged = a.h3
        title = img_title_tagged.text

        href = a.get("href")
        img_search_url = str(url) + str(href)

        browser.visit(img_search_url)
        html = browser.html
        soup = bs(html, 'html.parser')

        a = soup.find_all("a")[3]
        href = a.get("href")
        img_url = str(url) + str(href)
        hemisphere_entry.update({"title":title}) 
        hemisphere_entry.update({"img_url":img_url})
        hemisphere_image_urls.append(hemisphere_entry)

    #add hemispheres dictionary to return dictionary
    
    mars_data_dict.update({"hem_urls":hemisphere_image_urls})
    browser.quit()
    
    #return all of the data to function caller

    return mars_data_dict


    





