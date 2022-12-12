from kivy.uix.screenmanager import Screen
from abc import abstractmethod,ABC
from kivy.animation import Animation

import sys, os.path
pool_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/pool/')
main_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/pool/main/')

sys.path.append(pool_dir)
sys.path.append(main_dir)

from header_pool import HeaderPool
from menu_pool import MenuPool
from main_register_signup_pool import MainRegisterSignupPool


class AbstructSignupScreen(ABC):
    pass
        

class SignupScreen(Screen):
    anim_Passwordlay   = Animation(pos_hint={"center_x": .5}, duration=1,t = "in_out_quad") 
    anim_EmailLay      = Animation(pos_hint={"center_x": .5}, duration=1.1,t = "in_out_quad")
    anim_NameLay      = Animation(pos_hint={"center_x": .5}, duration=0.9,t = "in_out_quad")
    anim_button_register  = Animation(pos_hint={"center_y": 0.17}, duration=1,t = "out_cubic") 
    anim_button_login  = Animation(pos_hint={"center_y": 0.17}, duration=0.9,t = "out_cubic") 
    anim_images        = Animation(pos_hint={'center_y': .6}, duration=1.3,t = "in_out_quad")
   
    
    def anim_openning_the_screen_img(self, widget):
        self.anim_images.start(widget.ids.images_layout)

    
    def anim_openning_the_screen_text_input(self, widget):
        self.anim_EmailLay.start(widget.ids.EmailLay)
        self.anim_Passwordlay.start(widget.ids.PasswordLay)
        self.anim_NameLay.start(widget.ids.NameLay)
        
    
    def anim_openning_the_screen_buttons(self, widget):
        self.anim_button_register.start(widget.ids.REGISTERButton)
        self.anim_button_login.start(widget.ids.LOGINButton)
        