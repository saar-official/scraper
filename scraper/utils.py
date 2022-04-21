import requests
import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url, reqs=None, soup=None):
        self.url = url
        self.reqs = requests.get(self.url)
        self.soup = BeautifulSoup(self.reqs.text, 'html.parser')

    def is_clean(self, link):
        glitch_words = ["twitter", "facebook", "pib.gov.in",
                        "t.co", "whatsapp", "google", "linkedin"]
        for g_word in glitch_words:
            if g_word in link:
                return False
        return True

    def scrape_links(self):
        urls = []
        for link in self.soup.find_all('a'):
            if self.is_clean(link.get('href')):
                urls.append(link.get('href'))
        return urls


# SCRAPING TABLES FROM WEBPAGE {SETTING THE ANCHOR AND REVERSE ITERATING}


    def scrape_tables(self):
        page = pd.read_html(self.url)
        tables = []
        for table in range(int(len(page)/2)):
            df = page[table]
            Array2d = df.to_numpy()
            Array2d = Array2d
            temp_table = Array2d.tolist()
            tables.append(temp_table)
        return tables

    def scrape_images(self):
        image_data = []
        images = self.soup.select('img')
        for image in images:
            src = image.get('src')
            image_data.append(src)
        final_image_data = list(set(image_data))
        return final_image_data

    def preprocess(self, hs):
        remove_space = re.sub(' +', ' ', hs)
        remove_n = re.sub('\n', '', remove_space)
        remove_r = re.sub('\r', '', remove_n)
        return remove_r

    def scrape_text(self):
        final_text = []
        page = pd.read_html(self.url)
        try:
            SOUP = self.soup
            for data in SOUP('tbody'):
                data.decompose()
            hs = SOUP.text
        except:
            hs = self.soup.text
            print('soup:', hs)
        final_text = self.preprocess(hs)
        val0 = re.search("Posted On", final_text).span()[1]+34
        val = re.search("\*\*", final_text).span()[0]
        return [final_text[val0:val]]

    def scrape_page(self):
        text = self.scrape_text()
        assets = {}
        images = self.scrape_images()
        tables = self.scrape_tables()
        imp_links = self.scrape_links()
        exported_data = {}
        assets = {"images": images, "tables": tables, "imp_links": imp_links}
        exported_data.update({"text": text[0]})
        exported_data.update({"assets": assets})
        exported_data.update({"link": self.url})
        print(exported_data)
        return exported_data
