
from bs4 import BeautifulSoup
from random import choice
from pprint import pprint
from multiprocessing import Pool
from fake_useragent import UserAgent
import os,sys,time,requests,json

#link = 'https://allegro.pl/kategoria/turbosprezarki-kompletne-turbosprezarki-255509'
link = 'https://animevost.org/'
pre_domen = 'page/0/'


class Data: 
    def __init__(self):
        pass
        
    def write_page(self, name_file,req=""):
        with open(os.path.join(os.path.dirname(sys.argv[0]), "data/"+name_file), 'w', encoding="UTF-8") as main_file:
            main_file.write(req)
    def load_page(self, name_file):
        with open(os.path.join(os.path.dirname(sys.argv[0]), "data/"+name_file), 'r', encoding="UTF-8") as main_file:
            return main_file.read()    
    

class Parser:
    """docstring for Alergo"""
    def __init__(self,main_link):
        self.http_proxy = 'https://free-proxy-list.net/'
        self.proxy = {}
        self.link = main_link
        self.data_dump = Data()
        self.header = {}
        self.max_number = 0
        self.name_of_anime_pages = []
        self.urls_of_anime_pages = []
        
        
        print('!starting                   :: updating main page ')
        self.pars_main_page(main_link)
        print('!starting                   :: updating all page with anime')
        self.__pars_all_pages()
        print('!starting                   :: updating the url of links on anime')
        self.__pars_all_anime()

    def pars_main_page(self,link):
        if (input("Re-parse main page: ") == "1"):
            self.__update_user_agent()
            # self.proxy = self.update_poxi()
            time_to_load = time.time();
            print('@Log                        ::proxy :{} '.format(self.proxy))
            print('@Log                        ::user_agent :{} '.format(self.header))
            print('#started parsing main domen ::link :{}'.format(self.link))
            execute_answer = requests.get(self.link, headers=self.header)
            pprint(execute_answer)
            time_to_load_page = time.time() - time_to_load
            self.data_dump.write_page("main_page.html", execute_answer.text)
            time_to_write_page =  time.time() - time_to_load_page - time_to_load
            print(f"@Time : load page {time_to_load_page} : heshed page time {time_to_write_page}");
            self.__start_parse("request", execute_answer)
            
        else:
            self.__start_parse("local")

           
    def __start_parse(self, typing="local", req=""):
        if typing == "local":
            self.__parse_local()
        elif typing == "request":
            self.__parse_request(req)


    def __parse_request(self, req):
        soup = BeautifulSoup(req.text, 'lxml')
        self.__get_max_page_numbes(soup)


    def __parse_local(self):
        soup = self.data_dump.load_page("main_page.html")
        soup = BeautifulSoup(soup, 'lxml')
        self.__get_max_page_numbes(soup)


    def __get_max_page_numbes(self, soup):
        div_block_with_table_numbers = soup.find( "div",  {"id": "dle-content"})
        table_with_numbers = div_block_with_table_numbers.find_all("table")
        tr_with_numbers = table_with_numbers[-1].find("tr")
        all_links = tr_with_numbers.find_all("a")
        self.max_number = int(all_links[-1].text)
        print(f"@Log page with anime on site [{self.max_number}] ")
        
    def __pars_all_pages(self):
        if (input("Re-parse all other page: ") == "1"):
            for page_number in range(1, self.max_number+1):
                time.sleep(0.1)
                self.__update_user_agent()
                time_to_load = time.time();
                
                print('@Log                        ::proxy :{} '.format(self.proxy))
                print('@Log                        ::user_agent :{} '.format(self.header))
                print('#started parsing main domen ::link :{}'.format(self.link))
                link = self.link + f"page/{page_number}/"
                execute_answer = requests.get(self.link, headers=self.header)
                time_to_load_page = time.time() - time_to_load
                self.data_dump.write_page(f"pages/page_namber_{page_number}.html", execute_answer.text)
                time_to_write_page =  time.time() - time_to_load_page - time_to_load
                print(f"@Time : load page number [{page_number}] {time_to_load_page} : heshed page time {time_to_write_page}");
                
        
        else:
            pass
        
    def __pars_all_anime(self):
        time_to_load = time.time();
            
        for page_number in range(1, self.max_number+1):
            time.sleep(0.01)
            self.__update_user_agent()
                # execute_answer = requests.get(self.link, headers=self.header)
            rq = self.data_dump.load_page(f"pages/page_namber_{page_number}.html")
            soup = BeautifulSoup(rq, 'lxml')
            div_block_with_table = soup.find( "ul",  {"class": "raspis raspis_fixed"})
            res_text = [item.text for item in div_block_with_table.find_all("li")]
            res_link = [item.find("a").get('href') for item in div_block_with_table.find_all("li")]
                
            self.name_of_anime_pages.extend(res_text)
            self.urls_of_anime_pages.extend(res_link)
                
                # self.data_dump.write_page(f"pages/page_namber_{page_number}.html", execute_answer.text)
            if page_number % 30 == 0:
                pprint( self.name_of_anime_pages )
                pprint( self.urls_of_anime_pages )

        time_to_load_page = time.time() - time_to_load    
        print(f"@Time : get all links and anime name : {time_to_load_page} ");

        if (input("Re-parse all other anime pages: ") == "1"):

            for index, url in enumerate(self.urls_of_anime_pages):
                
            
                time_to_load = time.time();
                time.sleep(0.1)
                self.__update_user_agent()
                print('\n@Log                        ::proxy :{} '.format(self.proxy))
                print('@Log                        ::user_agent :{} '.format(self.header))
                execute_answer = requests.get(url, headers=self.header)
                time_to_load_page = time.time() - time_to_load
                self.data_dump.write_page(url, execute_answer.text)
                time_to_write_page =  time.time() - time_to_load_page - time_to_load
                print(f"@Time : load anime [{index}] [{ self.name_of_anime_pages[index] }] {time_to_load_page} : heshed page time {time_to_write_page}");
            
        else:
            pass
            

    def __update_user_agent(self):
        self.header = {'User-Agent': str(UserAgent())}


if __name__ == '__main__':
    Parser(link)