from kivymd.uix.list import IRightBodyTouch,ThreeLineAvatarIconListItem
from kivymd.uix.behaviors import FakeCircularElevationBehavior,CircularRippleBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior


class ContainerFindAnimeElementOfList(BoxLayout):
    adaptive_width = True
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


class ColliderFindAnimeElementOfList(BoxLayout,FakeCircularElevationBehavior):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    

class FindAnimeElementOfList(BoxLayout,ButtonBehavior):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)