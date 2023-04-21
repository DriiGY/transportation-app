from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.toast import toast
from utils.send_to_mobile import send_sms
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
Builder.load_file('views/personal_info/personal_password.kv')


##
#
# Create a widget from ClickableTextFieldPassword instead of 2:ClickableTextFieldPassword and ClickableTextFieldPasswordd (one more d)
# Mobile code should be in a new screen or a dialog box
##
class PersonalPassword(MDBoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

    def update_password(self):
        password_field = self.ids.new_password.ids.password.text.strip()
        password_field_repeat = self.ids.new_password_repeat.text.strip()
        #old_password widget must match previous password
        if password_field == password_field_repeat and len(password_field)>0 and len(password_field_repeat)>0:
          
            #send_sms("yuyu")
            self.parent.manager.current = "scrn_personal"
        else:
            toast("Fields must match!")


class ClickableTextFieldPasswordd(MDRelativeLayout):
    hint_text = StringProperty("")
    # Here specify the required parameters for MDTextFieldRound:
    # [...]

