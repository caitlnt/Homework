#CTa-HW11-Mission to Mars
#Part 02 - MongoDB and Flask Application

import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import requests


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:\Chrome\chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    # create mars_data dict that we can insert into mongo
    mars_data = {}

    # visit mars.nasa.gov
    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(masa_url)

    # search for news
    mars_data["news_title"] = soup.find_all('div', class_='content_title')[0].text
    mars_data["news_p"] = soup.find_all('div', class_='rollover_description_inner')[0].text


    # visit jpl url
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    browser.click_link_by_partial_text('FULL IMAGE')

    image = soup.find('a',class_="button fancybox")['data-fancybox-href']

    jpl_url = 'https://www.jpl.nasa.gov'

    image_url = jpl_url + image

    mars_data["image_url"] = image_url



    # visit mars weather
    marsweath_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(marsweath_url)

    # search for news
    mars_data["mars_weather"] = soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text



    # visit mars hemispheres
    marsweath_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(marsweath_url)

    # search for news
    mars_data["mars_weather"] = soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text




 url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # find all div classes 'item'
    mhemi_img_url_text = soup.find_all('div', class_="item")

    # get list of URLs for each hemisphere
    mhemi_img_url_text = []

    for item in mhemi_image:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        
        link = item.find('a')
        href = link['href']
       
        url = ('https://astrogeology.usgs.gov' + href)
   
        mhemi_img_url_text.append(mh_url)
        
        
    # run for loop going through each url and getting the title and sample url
    # put values in as dictionary
    hemisphere_image_urls = []

    for url in mhemi_img_url_text:
    
        browser.visit(url)
        html = browser.html
        soup = bs(html, 'html.parser')
        
        titles = soup.find('h2',class_="title")
    
        browser.click_link_by_text('Sample')
        
        img = browser.windows[0].next.url
        
        urls = {
            'title':titles.text,
            'mhemi_img_url':img
        }
         
        hemisphere_image_urls.append(urls)

        mars_data["hemisphere"] = hemisphere_image_urls
    
    
    return mars_data