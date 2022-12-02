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




Window.size = 500,800
Window.top = 30
Window.left = 500


class Main(MDApp):
    
    sm = ScreenManager()

    def build(self):
        Builder.load_file("uix//screens//anime_list_screen.kv")
        Builder.load_file("uix//screens//find_anime_screen.kv")
        Builder.load_file("uix//screens//find_people_screen.kv")
        Builder.load_file("uix//screens//other_profile_screen.kv")
        Builder.load_file("uix//screens//prefare_screen.kv")
        Builder.load_file("uix//screens//profile_screen.kv")
        Builder.load_file("uix//screens//register_screen.kv")

        return self.__init_secrens()


    def __init_secrens(self):
        self.screens = ['anime_list', 'find_anime', 'find_people', 'other_profile', 'prefare_screen', 'profile','register']
        self.screens_ojects = [
            AnimeListScreen(name=self.screens[0]),
            FindAnimeScreen(name=self.screens[1]),
            FindPeopleScreen(name=self.screens[2]),
            OtherProfileScreen(name=self.screens[3]),
            PrefareScreen(name=self.screens[4]),
            ProfileScreen(name=self.screens[5]),
            RegisterScreen(name=self.screens[6])
        ]
        for element_screen in self.screens_ojects:
            self.sm.add_widget(element_screen)
            
        return self.sm
        

if __name__ == '__main__':
    Main().run()
