
from bs4 import BeautifulSoup
from random import choice
from pprintpp import pprint
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
        print('!starting                   :: updating main page ')
        self.pars_main_page(main_link)
        print('!starting                   :: updating all page with anime')
        self.__pars_all_pages()



    def pars_main_page(self,link):
        if (input("Re-parse main page: ") == "1"):
            self.__update_user_agent()
            # self.proxy = self.update_poxi()
            time_to_load = time.time();
            print('@Log                        ::proxy :{} '.format(self.proxy))
            print('@Log                        ::user_agent :{} '.format(self.header))
            print('#started parsing main domen ::link :{}'.format(self.link))
            execute_answer = requests.get(self.link, headers=self.header)
            time_to_load_page = time.time() - time_to_load
            self.data_dump.write_page("main_page.html", execute_answer.text)
            time_to_write_page =  time.time() - time_to_load_page - time_to_load
            print(f"@Time : load page {time_to_load_page} : heshed page time {time_to_write_page}");
            self.__start_parse("request", execute_answer.text)
            
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

            

    def __update_user_agent(self):
        self.header = {'User-Agent': str(UserAgent())}


if __name__ == '__main__':
    Parser(link)