from kivymd.uix.list import IRightBodyTouch,ThreeLineAvatarIconListItem
from kivymd.uix.button import MDFlatButton 
from kivymd.uix.behaviors import FakeCircularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty

class ContainerAnimeElementOfList(IRightBodyTouch, MDFloatLayout):
    adaptive_width = True


class AnimeElementOfList(FakeCircularElevationBehavior,ThreeLineAvatarIconListItem):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    