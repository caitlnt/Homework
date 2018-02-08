#CTa-HW11-Mission to Mars
#Part 02 - MongoDB and Flask Application

import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:\Chrome\chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    # create mars_data dict that we can insert into mongo
    mars_data = {}

    # visit mars.nasa.gov
    mars_url = "https://mars.nasa.gov/news/"
    browser.visit(mars_url)

    # search for news
    news_title = result.find('div', class_='content_title').text
    news_p = result.find('div', class_='rollover_description_inner').text

    # find button and click it to search
    button = browser.find_by_name("button")
    button.click()
    time.sleep(2)
    html = browser.html
    # create a soup object from the html
    img_soup = BeautifulSoup(html, "html.parser")
    elem = img_soup.find(id="gridMulti")
    img_src = elem.find("img")["src"]

    time.sleep(2)
    # add our src to mars data with a key of src
    mars_data["src"] = img_src
    # visit twitter to get weather report
    weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather)
    # grab our new html from twitter
    html = browser.html
    # create soup object from html
    forecast_soup = BeautifulSoup(html, "html.parser")
    report = forecast_soup.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    mars_report = report.find_all("p")
    # add it to our surf data dict
    mars_data["report"] = build_report(mars_report)
    # return our mars data dict
    return marsdata


# helper function to build surf report
def build_report(mars_report):
    final_report = ""
    for p in mars_report:
        final_report += " " + p.get_text()
        print(final_report)
    return final_report