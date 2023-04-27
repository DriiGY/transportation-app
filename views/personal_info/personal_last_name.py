from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.toast import toast
from utils.send_to_mobile import send_sms
Builder.load_file('views/personal_info/personal_last_name.kv')

class PersonalLastName(MDBoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

    def update_last_name(self):
        name_first_field = self.ids.new_name.text.strip()
        name_first_field_repeat = self.ids.new_name_repeat.text.strip()
       
        if name_first_field == name_first_field_repeat:
            self.parent.manager.get_screen("scrn_personal").children[0].ids["last_name"].secondary_text = f"[size=18]{name_first_field.title()}[/size]"
            #send_sms("yuyu")
            self.parent.manager.current = "scrn_personal"
        else:
            toast("Fields must match!")