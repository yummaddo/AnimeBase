
from bs4 import BeautifulSoup
from random import choice
from pprint import pprint
from multiprocessing import Pool
from fake_useragent import UserAgent
import os,sys,time,requests,json

#link = 'https://allegro.pl/kategoria/turbosprezarki-kompletne-turbosprezarki-255509'
link = 'https://animevost.org/'
link_img = 'https://animevost.org'

pre_domen = 'page/0/'


class Data: 
    def __init__(self):
        pass
        
    def write_page(self, name_file,req=""):
        with open(os.path.join(os.path.dirname(sys.argv[0]), "data/"+name_file), 'w', encoding="UTF-8") as main_file:
            main_file.write(req)

    def write_image(self, name_file,req=""):
        with open(os.path.join(os.path.dirname(sys.argv[0]), "data/"+name_file), 'wb') as main_file:
            main_file.write(req.content)
            
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
        self.urls_of_anime_media = []
        
        
        
        print('!starting                   :: updating main page ')
        # self.pars_main_page(main_link)
        print('!starting                   :: updating all page with anime')
        # self.__pars_all_pages()
        print('!starting                   :: updating the url of links on anime')
        self.__pars_all_anime()
        print('!starting                   :: updating the media data')
        self.__pars_all_media()
        

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
        if (input("Re-parse all other page (280+ pages): ") == "1"):
            for page_number in range(1, self.max_number+1):
                time.sleep(0.1)
                self.__update_user_agent()
                time_to_load = time.time();
                link = self.link + f"page/{page_number}/"
                
                print('@Log                        ::proxy :{} '.format(self.proxy))
                print('@Log                        ::user_agent :{} '.format(self.header))
                print('#started parsing main domen ::link :{}'.format(link))
                execute_answer = requests.get(link, headers=self.header)
                time_to_load_page = time.time() - time_to_load
                self.data_dump.write_page(f"pages/page_namber_{page_number}.html", execute_answer.text)
                time_to_write_page =  time.time() - time_to_load_page - time_to_load
                print(f"@Time : load page number [{page_number}] {time_to_load_page} : heshed page time {time_to_write_page}");
                        
        else:
            pass


    def __pars_all_anime(self):
        if (input("Re-parse all anime urls: ") == "1"):
            time_to_load = time.time();
                
            for page_number in range(1, self.max_number+1):
                time.sleep(0.01)
                self.__update_user_agent()
                    # execute_answer = requests.get(self.link, headers=self.header)
                rq = self.data_dump.load_page(f"pages/page_namber_{page_number}.html")
                soup = BeautifulSoup(rq, 'lxml')
                div_block_with_table = soup.find_all( "div",  {"class": "shortstoryHead"})
                for item in div_block_with_table:
                    self.name_of_anime_pages.append(item.find("h2").text)
                    
                    self.urls_of_anime_pages.append(item.find("a").get('href'))

            with open(os.path.join(os.path.dirname(sys.argv[0]), "data/" + "urls.txt"), 'w', encoding="UTF-8") as main_file:
                for item in self.urls_of_anime_pages:
                    main_file.write(item + "\n")
            
            time_to_load_page = time.time() - time_to_load 
            print(f"@Time : get all links and anime name : {time_to_load_page} ");
            
        else: 
                  
            with open(os.path.join(os.path.dirname(sys.argv[0]), "data/" + "urls.txt"), 'r', encoding="UTF-8") as main_file:
                self.urls_of_anime_pages = main_file.read().split('\n')
                pprint(self.urls_of_anime_pages)
        
        if (input("Re-parse all other anime pages (2800+ pages) : ") == "1"):

            for index, url in enumerate(self.urls_of_anime_pages):
                
                time_to_load = time.time();
                time.sleep(0.01)
                self.__update_user_agent()
                print('\n@Log                        ::proxy :{} '.format(self.proxy))
                print('@Log                        ::user_agent :{} '.format(self.header))
                execute_answer = requests.get(url, headers=self.header)
                time_to_load_page = time.time() - time_to_load
                self.data_dump.write_page(f"animes/anime_with_index_{index}.html", execute_answer.text)
                time_to_write_page =  time.time() - time_to_load_page - time_to_load
                print(f"@Time : load anime [{index}] [{ self.name_of_anime_pages[index] }] {time_to_load_page} : heshed page time {time_to_write_page}");
            
        else:
            pass     
            
            
    def __pars_all_media(self):
        time_to_load = time.time();
        if (input("Re-parse all urls of media : ") == "1"):
            for url_index in range(len(self.urls_of_anime_pages)):
                time.sleep(0.0003)
                self.__update_user_agent()
                    # execute_answer = requests.get(self.link, headers=self.header)
                try:
                    rq = self.data_dump.load_page(f"animes/anime_with_index_{url_index}.html")
                    soup = BeautifulSoup(rq, 'lxml')
                    div_block_with_table = soup.find( "div",  {"class": "shortstoryContent"})
                    div_block_with_table = div_block_with_table.find_all("div")[0]
                    local_link = div_block_with_table.find("img")['src']
                    img_link = link_img + local_link
                    self.urls_of_anime_media.append(img_link)
                except FileNotFoundError:
                    print(f"@ERROR :  No such file or directory: animes/anime_with_index_{url_index}.html need upload the data")

                with open(os.path.join(os.path.dirname(sys.argv[0]), "data/" + "images_urls.txt"), 'w', encoding="UTF-8") as main_file:
                    for item in self.urls_of_anime_media:
                        main_file.write(item + "\n")

            time_to_load_page = time.time() - time_to_load
            print(f"@Time : get all links and anime name : {time_to_load_page} ");
        else:
                              
            with open(os.path.join(os.path.dirname(sys.argv[0]), "data/" + "images_urls.txt"), 'r', encoding="UTF-8") as main_file:
                self.urls_of_anime_media = main_file.read().split('\n')
                pprint(self.urls_of_anime_media)
            
            
        if (input("Re-parse all media: ") == "1"):

            for index, url in enumerate(self.urls_of_anime_media):
                if url != '':
                    time_to_load = time.time();
                    time.sleep(0.0003)
                    self.__update_user_agent()
                    print('\n@Log                        ::proxy :{} '.format(self.proxy))
                    print('@Log                        ::user_agent :{} '.format(self.header))
                    print('@Log                        ::load image :{} '.format(url))
                    execute_answer = requests.get(url, headers=self.header)
                    time_to_load_page = time.time() - time_to_load
                    self.data_dump.write_image(f"media/image_for_anime_with_index_{index}.jpg", execute_answer)
                    time_to_write_page =  time.time() - time_to_load_page - time_to_load
                    print('@Log                        ::saved into :{} '.format( f"data/media/image_for_anime_with_index_{index}.jpg"))
                    print(f"@Time : load img [{index}] [{ self.urls_of_anime_media[index] }] {time_to_load_page} : heshed img time {time_to_write_page}");
            
        else:
            pass


    def __update_user_agent(self):
        self.header = {'User-Agent': str(UserAgent())}


if __name__ == '__main__':
    Parser(link)