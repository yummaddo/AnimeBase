from kivymd.uix.list import IRightBodyTouch, OneLineAvatarListItem,ImageRightWidget,IconLeftWidget
from kivymd.uix.button import MDFlatButton 
from kivymd.uix.behaviors import FakeCircularElevationBehavior
from kivy.properties import StringProperty

class ContainerFriendsListOnProfile(IconLeftWidget, MDFlatButton):
    pass


class FriendsListOnProfile(FakeCircularElevationBehavior,OneLineAvatarListItem):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
