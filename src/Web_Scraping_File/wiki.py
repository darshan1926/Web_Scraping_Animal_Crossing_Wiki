import os
import json
import sys
import requests
from bs4 import BeautifulSoup
from src.exception import CustomException

def web_scraping():
    topic = []
    try:
        url = "https://animalcrossing.fandom.com/wiki/Animal_Crossing_Wiki"
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        article_links = soup.find_all("a", class_="category-page__member-link")

        article_urls = []
        for link in article_links:
            article_url = link.get("href")
            article_urls.append(article_url)
            

        for article_url in article_urls:
            article_response = requests.get(article_url)
            article_content = article_response.content
            article_soup = BeautifulSoup(article_content, "html.parser")
    
            title = article_soup.find("h1", class_="page-header__title").text
            summary = article_soup.find("div", class_="wds-dropdown__content").text.strip()
            content = article_soup.find("div", class_="mw-parser-output").text.strip()
            topic.append({
                "title": title,
                "summary": summary,
                "content": content
            })
        with open("animal_crossing_wiki_articles.json", "w") as f:
            json.dump(topic, f)
            logging.info(f"PROGREM run succsessfully!")




    except Exception as e:
        raise CustomException(e, sys)
        logging.info(f"ERROR OCURRING!")
       #print(e)
    
if __name__=="__main__":
    web_scraping()
    