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
from main_register_pool import MainRegisterPool


class AbstructRegisterScreen(ABC):
    pass
        

class RegisterScreen(Screen):
    anim_Passwordlay   = Animation(pos_hint={"center_x": .5}, duration=1.1,t = "in_out_quad") 
    anim_EmailLay      = Animation(pos_hint={"center_x": .5}, duration=1.1,t = "in_out_quad")
    anim_button_sign   = Animation(pos_hint={"center_x": .72}, duration=1.2,t = "out_circ")
    anim_button_login  = Animation(pos_hint={"center_x": .29}, duration=1.2,t = "out_circ") 
    anim_images        = Animation(pos_hint={'center_y': .6}, duration=1.4,t = "in_out_quad")
    anim_google_lay    = Animation(pos_hint={'center_y': .1}, duration=1.2,t = "in_out_quad")
    
    
    
    def anim_openning_the_screen_img(self, widget):
        self.anim_images.start(widget.ids.images_layout)

    
    def anim_openning_the_screen_text_input(self, widget):
        self.anim_EmailLay.start(widget.ids.EmailLay)
        self.anim_Passwordlay.start(widget.ids.PasswordLay)
    
    
    def anim_openning_the_screen_google_lay(self, widget):
        self.anim_google_lay.start(widget.ids.GoogleLay)


    def anim_openning_the_screen_buttons(self, widget):
        self.anim_button_sign.start(widget.ids.SIGNUPButton)
        self.anim_button_login.start(widget.ids.LOGINButton)
        
        
