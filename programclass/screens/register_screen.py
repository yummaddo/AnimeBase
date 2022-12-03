from kivy.uix.screenmanager import Screen
from abc import abstractmethod,ABC

import sys, os.path
pool_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/pool/')
sys.path.append(pool_dir)

from header_pool import HeaderPool
from menu_pool import MenuPool


class AbstructRegisterScreen(ABC):
    pass
        

class RegisterScreen(Screen):
    pass