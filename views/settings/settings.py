from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

Builder.load_file('views/settings/settings.kv')


class SettingsScreen(BoxLayout):
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()
    
    def go_back(self):
        self.parent.manager.current = "scrn_home"


