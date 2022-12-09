from kivymd.uix.list import IRightBodyTouch,ThreeLineAvatarIconListItem
from kivymd.uix.behaviors import FakeCircularElevationBehavior,CircularRippleBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior


class ContainerAnimeElementOfList(BoxLayout):
    adaptive_width = True
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


class ColliderAnimeElementOfList(BoxLayout,FakeCircularElevationBehavior):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    

class AnimeElementOfList(BoxLayout,ButtonBehavior):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)