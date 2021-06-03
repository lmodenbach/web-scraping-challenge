#!/usr/bin/env python
# coding: utf-8
def scrape():
    scrape_dict = []

    from splinter import Browser
    from bs4 import BeautifulSoup as bs
    from webdriver_manager.chrome import ChromeDriverManager
    import os
    import pandas as pd
    import requests 

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

# headline/story

    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.find_all("div", {"class": "content_title"})[0].text
    news_note = soup.find_all("div", {"class": "article_teaser_body"})[0].text

    scrape_dict.append({"news_title":news_title, "news_note":news_note})

# featured image

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    firsta = soup.find_all("a", {"class": "showimg fancybox-thumbs"})[0]
    href = firsta.get("href")
    featured_image_url = str(browser.url) + str(href)

    scrape_dict.append({"feat_img_url":featured_image_url})

# facts

    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    tables = pd.read_html(url)
    df = pd.DataFrame(tables[0])
    df.columns = df.iloc[0]
    df.drop(0, inplace=True)

    html = df.to_html()
    scrape_dict.append({"html":html})

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
        scrape_dict.append(hemisphere_image_urls)

    browser.quit()

    return scrape_dict
    print(scrape_dict)





