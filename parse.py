import requests
import json
from bs4 import BeautifulSoup
import time
from random import choice
from pprintpp import pprint
from multiprocessing import Pool
from fake_useragent import UserAgent

#link = 'https://allegro.pl/kategoria/turbosprezarki-kompletne-turbosprezarki-255509'
link = 'https://animevost.org/'
pre_domen = 'page/0/'


class Data: 
    def __init__(self):
        self.data_infor
        self.data_link
        
    def __set__(self, arg, name="saved_page_obj.html"):
        with open(name, "w", encoding="UTF-8"):
            pass
        
        


class Parser:
    """docstring for Alergo"""
    def __init__(self,main_link):
        self.http_proxy = 'https://free-proxy-list.net/'
        self.proxy = {}
        self.link = main_link
        self.header = {}
        print('!starting                   :: updating data')
        self.pars_main_page(main_link)

    def pars_main_page(self,link):
        self.__update_user_agent()
        self.proxy = self.update_poxi()

        print('@Log                        ::proxy :{} '.format(self.proxy))
        print('@Log                        ::user_agent :{} '.format(self.header))
        print('#started parsing main domen ::link :{}'.format(self.link))
        execute_answer = requests.get(link, headers=self.header)
        

    def get_page_numbes(self, main_domen):
        

    def __update_user_agent(self):
        self.header = {'User-Agent': str(UserAgent())}


if __name__ == '__main__':
    Parser(link)