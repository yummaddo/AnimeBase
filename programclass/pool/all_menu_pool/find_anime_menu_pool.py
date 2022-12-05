from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.properties import StringProperty
from kivy.graphics import Rectangle as r, Color as c, RoundedRectangle as rr


class FindAnimeMenuPool(CommonElevationBehavior,MDFloatLayout):
    element_index = StringProperty()
