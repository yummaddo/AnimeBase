from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.image import Image
from kivymd.uix.behaviors import CommonElevationBehavior,FakeCircularElevationBehavior,CircularRippleBehavior


class RoundedImage(FakeCircularElevationBehavior, CircularRippleBehavior, MDFloatLayout):
    pass


class ImageOfProfile(CommonElevationBehavior, MDFloatLayout):
    pass