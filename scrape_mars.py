#!/usr/bin/env python
# coding: utf-8

from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_data_dict = {}

# headline/story
      
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.find_all("div", {"class": "content_title"})[0].text
    news_note = soup.find_all("div", {"class": "article_teaser_body"})[0].text

    mars_data_dict.update({"news_title":news_title}) 
    mars_data_dict.update({"news_note":news_note})

# featured image

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    firsta = soup.find_all("a", {"class": "showimg fancybox-thumbs"})[0]
    href = firsta.get("href")
    featured_image_url = str(browser.url) + str(href)

    mars_data_dict.update({"feat_img_url":featured_image_url})

# facts

    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    tables = pd.read_html(url)[0]
    tables_df = pd.DataFrame(tables)
    tables_df.columns = tables_df.iloc[0]
    tables_df.drop(0, inplace=True)
    html = tables_df.to_html()
    print(html)
    mars_data_dict.update({"html":html})

# hemispheres

    img_url = ""
    img_title = ""
    img_dict = {}

    for x in range(1, 8, 2):
        url = 'https://marshemispheres.com/'
        browser.visit(url)
        html = browser.html
        soup = bs(html, 'html.parser')
        a = soup.find_all("a", {"class": "itemLink product-item"})[x]
    
        img_title_tagged = a.h3
        img_title = img_title_tagged.text

        href = a.get("href")
        img_search_url = str(url) + str(href)

        browser.visit(img_search_url)
        html = browser.html
        soup = bs(html, 'html.parser')

        a = soup.find_all("a")[3]
        href = a.get("href")
        img_url = str(url) + str(href)
        img_dict.update({"img_title" + str(x):img_title}) 
        img_dict.update({"img_url" + str(x):img_url})
    
    mars_data_dict.update(img_dict)
    browser.quit()
    
    return mars_data_dict


    





