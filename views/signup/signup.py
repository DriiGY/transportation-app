from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.properties import StringProperty, ListProperty
from kivymd.toast import toast
from kivy.utils import  rgba
from kivy.uix.textinput import TextInput
import re
from email_validator import validate_email, EmailNotValidError

Builder.load_file('views/signup/signup.kv')

class Signup(BoxLayout):

    def __init__(self, **kw) -> None:
        
        super().__init__(**kw)
    def set_cursor(self, instance, dt):
        instance.cursor = (len(instance.text), 0)

    def check_birthdate(self, instance, text):
        if len(text) == 2 or len(text) == 5 :
            self.ids.birthdate.text += "/"
    
    

    def validate_name(self):
        name = self.ids.name.text
        valid = bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name))
        return valid

    def check_is_valid_number(self):
        number = self.ids.phone_number.text
        if len(number) == 9:
            return number.isdigit()
        else:
            return False
    def check_birthdate_form(self):
        # dd/mm/yyyy, dd-mm-yyyy or dd.mm.yyyy
        birthdate = self.ids.birthdate.text 
        valid = bool(re.fullmatch('^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2)) \
        (?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16| \
        [2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$', birthdate))
        return valid

    def check_email(self):
        try:
        
            if validate_email(self.ids.email.text):
                return True
        except:
            return False

    def check_password(self, password):
        ### Needs to have capital letter, special character numbers and 6 to 20 letters
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
         # compiling regex
        pat = re.compile(reg)
        
        # searching regex                
        mat = re.search(pat, password)
        
        # validating conditions
        if mat:
            return True
        else:
            return False

    def check_password_equal(self, password, conf_password):
        length_pass = len(password)
        length_conf_password = len(conf_password)  # confirmation password length
        if length_pass != length_conf_password:
            return False
        else:
            if password == conf_password:
                return True
            else: 
                return False
    def check_password_confirmation(self, instance, text):
        passw = self.ids.password.text
        if self.check_password_equal(passw, text):
            self.ids.confirmation_message.text = "Passwords match!"
            self.ids.confirmation_message.color = rgba("#2BC48A")
        else:
            self.ids.confirmation_message.text = "Passwords do not match!"
            self.ids.confirmation_message.color = [1,0,0,1]
    
    def on_checkbox_active(self):
        state_checkbox = self.ids.terms_checkbox.active
        if state_checkbox:
            return True
        return False

    # Signup button press
    def signup(self):
        #self.on_checkbox_active()
        self.parent.manager.current = "scrn_login"
