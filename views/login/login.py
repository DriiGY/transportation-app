from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivymd.app import MDApp

Builder.load_file('views/login/login.kv')

class Login(BoxLayout):
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

