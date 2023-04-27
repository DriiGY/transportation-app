from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.toast import toast
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
Builder.load_file('views/personal_info/personal_first_name.kv')

class PersonalFirstName(MDBoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

    def update_first_name(self):
        name_first_field = self.ids.new_name.ids.name.text.strip()
        name_first_field_repeat = self.ids.new_name_repeat.ids.name.text.strip()
        #print(name_first_field, name_first_field_repeat)
        
        if name_first_field == name_first_field_repeat:
            self.parent.manager.get_screen("scrn_personal").children[0].ids["first_name"].secondary_text = f"[size=18]{name_first_field.title()}[/size]"
            self.parent.manager.current = "scrn_personal"
        else:
            toast("Fields must match!")


class ClickableTextFieldUsernamee(MDRelativeLayout):
    hint_text = StringProperty()
    def __init__(self, **kw) -> None:
        self.valid = False
        #Clock.schedule_interval(self.validate_username, 1)
        super(ClickableTextFieldUsernamee, self).__init__(**kw)
        
    