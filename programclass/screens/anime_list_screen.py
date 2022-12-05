from kivy.uix.screenmanager import Screen
from abc import abstractmethod,ABC
from kivy.graphics import Rectangle as r, Color as c, RoundedRectangle as rr

import sys, os.path
pool_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/pool/')
main_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/pool/main/')
main_menu_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/pool/all_menu_pool/')

sys.path.append(pool_dir)
sys.path.append(main_dir)
sys.path.append(main_menu_dir)

from header_pool import HeaderPool
from menu_pool import MenuPool
from main_anime_list_pool import MainAnimeListPool
from anime_list_menu_pool import AnimeListMenuPool


class AbstructAnimeListScreen(ABC):
    pass
        

class AnimeListScreen(Screen):
    pass