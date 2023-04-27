from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
import os
from email.message import EmailMessage
import ssl
import smtplib
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
Builder.load_file('views/personal_info/personal_phone.kv')


class PersonalPhone(MDBoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

    def update_phone_number(self):
        star_numbers_pt = ['67','71','72','95','96','97','98','99', '68','73','74','75','76','91','92','93','94', '69','79','80','81','82','83', '84','85','86','87','88','89']
        phone_old_field = self.ids.old_phone_number.ids.name.text.strip()
        phone_new_field = self.ids.new_phone_number.ids.name.text.strip()
        # 9 is the length of mobile communications phone number in  portugal
        first_2_numbers = phone_new_field[:2]
        if len(phone_new_field) and first_2_numbers in star_numbers_pt:
            print("ok")
        # email_sender = os.getenv("emailSender")
        # email_code = os.getenv("emailCode")
        # email_receiver = os.getenv("emailReceiver")
        # subject = "check what i sent you"
        # body = """
        # What up little boy
        # """
        # em = EmailMessage()
        # em['From'] = email_sender
        # em['To'] = email_receiver
        # em['Subject'] = subject
        # em.set_content(body)
        # context = ssl.create_default_context()
        # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        #     smtp.login(email_sender, email_code)
        #     smtp.sendmail(email_sender, email_receiver, em.as_string())
        


class ClickableTextFieldNumber(MDRelativeLayout):
    hint_text = StringProperty()
    input_filter = StringProperty("null")
    def __init__(self, **kw) -> None:
        self.valid = False
        #Clock.schedule_interval(self.validate_username, 1)
        super(ClickableTextFieldNumber, self).__init__(**kw)       



