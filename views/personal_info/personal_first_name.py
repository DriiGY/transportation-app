from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.toast import toast

Builder.load_file('views/personal_info/personal_first_name.kv')

class PersonalFirstName(MDBoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

    def update_first_name(self):
        name_first_field = self.ids.new_name.text.strip()
        name_first_field_repeat = self.ids.new_name_repeat.text.strip()
        #print(name_first_field, name_first_field_repeat)
        if name_first_field == name_first_field_repeat:
            self.parent.manager.current = "scrn_settings"
        else:
            toast("Fields must match!")
