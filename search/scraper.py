from bs4 import BeautifulSoup
import requests
from .models import Item
from .word_counter import *

DOMAIN_NAME = 'https://www.coffeebeanshop.co.uk'
# 'http://www.kavaprodej.cz'


def trade_spider(max_pages):
    clean_database()
    for page in range(1, max_pages + 1):
        # url = DOMAIN_NAME + '/kava-jednodruhova-arabica/?page=' + str(page)
        url = DOMAIN_NAME + '/single-origin-coffees-c-285_176.html?osCsid=ad19f0da956c6ab04d72616a9f17736f'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for div in soup.findAll('div', {'class': 'prodListItem'}):
            link = div.find('a')
            get_single_item_data(link.get('href'))


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_detail in soup.findAll('div', {'class': 'CentreCell', 'id': 'content'}):
        item_name = item_detail.find('h1').string
        item_image_src = DOMAIN_NAME + '/' + item_detail.find('img', {'class': 'img-responsive'}).get('src')
        item_price = item_detail.find('span', {'class': 'prodInfoPrice'}).text
        item_price = ''.join(x for x in item_price if x.isdigit())
        # for p in item_detail.find('div', {'class': 'tab-pane active', 'id': 'pTabDetails'}).findAll('p'):
            # item_description += p.string

        item_description = item_detail.find('div', {'class': 'tab-pane active', 'id': 'pTabDetails'}).text or "no description"
        print("Create new item: "+item_name)
        new_item = Item.objects.get_or_create(title=item_name, url=item_url, image=item_image_src,
                                              price=item_price, description=item_description)[0]
        create_dictionary(item_name + " " + item_description, new_item)

    analyze_dictionary()
