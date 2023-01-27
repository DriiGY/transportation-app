from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivymd.app import MDApp

Builder.load_file('views/splash/splash.kv')

class Splash(BoxLayout):
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()
        Clock.schedule_once(self.render, .1)
        self.on_start()
    def render(self, _):
        self.ids.progress.start()
    def on_start(self):
        Clock.schedule_once(self.login, 3)
        
    
    def login(self, *args):
        self.parent.manager.current = "scrn_login"
        

