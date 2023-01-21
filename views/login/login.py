from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.properties import StringProperty
Builder.load_file('views/login/login.kv')

class Login(BoxLayout):
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)




class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]