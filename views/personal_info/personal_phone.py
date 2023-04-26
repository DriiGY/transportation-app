from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
Builder.load_file('views/personal_info/personal_phone.kv')


class PersonalPhone(MDBoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()




