from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.toast import toast
from kivy.utils import  rgba

Builder.load_file('views/signup/signup.kv')

class Signup(BoxLayout):

    def __init__(self, **kw) -> None:
        super().__init__(**kw)

        