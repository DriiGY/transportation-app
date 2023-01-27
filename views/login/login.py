from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.toast import toast
from kivy.utils import  rgba
from email_validator import validate_email, EmailNotValidError
from kivyauth.google_auth import initialize_google, login_google, logout_google
import re
Builder.load_file('views/login/login.kv')

class Login(BoxLayout):
    
    def __init__(self, **kw) -> None:
        # client_id = open("client_id.txt")
        # client_secret = open("client_secret.txt")
        # initialize_google(self.after_login, self.error_listener, client_id.read(), client_secret.read())
        # print(client_id.read())
        super().__init__(**kw)

    def login(self):
        pass_validate = self.check_password(self.ids.password.ids.password.text)
        if self.ids.email.valid and pass_validate:

            self.parent.manager.current = "scrn_home"
        else:
            
            toast("E-mail/password invalid!")
    # def login_by_google(self):
    #     login_google()

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
    
    # def forgot_pass(self):
    #     if self.ids.email.valid == True:
    #         #################################
    #         ### ADD SEND EMAIL TO RESET PASSWORD SCREEN
    #         ###################################
    #         toast("We sent an email to " + self.ids.email.ids.email.text)
    #     else: 
    #         toast("Add a valid email to the email field")

    # def after_login(self, name, email, photo_uri):
    #     print(name, email)
    #     self.parent.manager.current = "scrn_home"

    # def error_listener(self):
    #     print("Login Failed!")
    def forgot_pass(self):
        if self.ids.email.valid:
            
            toast(f"We sent an email to {self.ids.email.ids.email.text}")
        else:
            toast("Fill email field and press again!")
    def signup(self):
        self.parent.manager.current = "scrn_signup"

class ClickableTextFieldPassword(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]

class ClickableTextFieldUsername(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

    def __init__(self, **kw) -> None:
        self.valid = False
        #Clock.schedule_interval(self.validate_username, 1)
        super(ClickableTextFieldUsername, self).__init__(**kw)
        
    def check_focus(self, instance, text):
        try:
            # Validating the `testEmail`
            validate_email(self.ids.email.text)

            
            # it is updated with its normalized form
            #testEmail = emailObject.email
            #toast('Test Kivy Toast')


            # If the `testEmail` is valid
            # set valid to true
            self.valid = True
            self.ids.icon.icon = "check-bold"
            self.ids.icon.icon_color = rgba("#006400")

        except EmailNotValidError as errorMsg:
            # If `testEmail` is not valid
            # we print a human readable error message
            # Do nothing
            self.valid = False
            self.ids.icon.icon = "close"
            self.ids.icon.icon_color = rgba("#DC3545")

