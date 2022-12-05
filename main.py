from kivymd.app import MDApp
from kivy.lang.builder import Builder

from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.core.window import Window


from programclass.screens.anime_list_screen import AnimeListScreen
from programclass.screens.find_anime_screen import FindAnimeScreen
from programclass.screens.find_people_screen import FindPeopleScreen
from programclass.screens.other_profile_screen import OtherProfileScreen
from programclass.screens.prefare_screen import PrefareScreen
from programclass.screens.profile_screen import ProfileScreen
from programclass.screens.register_screen import RegisterScreen


import os

Window.size = 500,800
Window.top = 30
Window.left = 500



class Main(MDApp):

    curent_index_of_menu = 0
    sm = ScreenManager()

    def build(self):
        Builder.load_file("uix//pool//header_pool.kv")
        Builder.load_file("uix//pool//menu_pool.kv")
    
        screns                      = [ os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','screens\\')) + "\\\\" + item for item in os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','screens')))]
        lists                       = [os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','list\\')) + "\\\\" + item for item in os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','list')))]
        lists_elements              = [os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','list\\','elements')) + "\\\\" + item for item in os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','list','elements')))]
        pools                       = [os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','pool\\')) + "\\\\" + item for item in os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','pool')))] 
        main_of_pool__menu_elements = [os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','pool','all_menu_pool\\')) + "\\\\" + item  for item in  os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','pool','all_menu_pool')))]
        main_of_pool_elements       = [os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','pool','main\\')) + "\\\\" + item  for item in  os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','pool','main')))]
        main_of_pool_elements_items = [os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','pool','main','elements\\')) + "\\\\" + item for item in os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), 'uix','pool','main','elements')))]
        self.UIX = [screns,lists,lists_elements,pools,main_of_pool_elements_items, main_of_pool_elements,main_of_pool__menu_elements]
        
        for directoty_path_list in self.UIX:
        
            for file_path in directoty_path_list:
                
                if file_path.endswith(".kv"):
                    Builder.load_file(file_path)
        
        return self.__init_secrens()
    # in screen manager
    def swap_screen(self, index_of_menu):        
        if index_of_menu != self.curent_index_of_menu:
            if index_of_menu > self.curent_index_of_menu:
                self.root.switch_to(self.menu_screen_objects[index_of_menu], direction='right')
            elif index_of_menu < self.curent_index_of_menu:
                self.root.switch_to(self.menu_screen_objects[index_of_menu], direction='left')
            self.curent_index_of_menu = index_of_menu
        
        
        
    def confirmation_process(self):
        self.root.switch_to(self.root.get_screen("profile"), direction='up')




    def __init_secrens(self):
        self.screens = ['anime_list', 'find_anime', 'find_people', 'other_profile', 'prefare_screen', 'profile','register']
        self.screens_ojects = [
            ProfileScreen(name=self.screens[5]),
            AnimeListScreen(name=self.screens[0]),
            FindAnimeScreen(name=self.screens[1]),
            PrefareScreen(name=self.screens[4]),
            FindPeopleScreen(name=self.screens[2]),
            OtherProfileScreen(name=self.screens[3]),
            RegisterScreen(name=self.screens[6])
        ]
        self.menu_screen = [
            self.screens[5],
            self.screens[0],
            self.screens[1],
            self.screens[4]
        ]
        self.menu_screen_objects = [
            self.screens_ojects[0],
            self.screens_ojects[1],
            self.screens_ojects[2],
            self.screens_ojects[3]
        ]
        
        for element_screen in self.screens_ojects:
            self.sm.add_widget(element_screen)
            
        self.sm.current = self.screens[-2]
        return self.sm
        

if __name__ == '__main__':
    Main().run()
