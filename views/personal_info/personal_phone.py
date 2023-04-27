from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
import os
from email.message import EmailMessage
import ssl
import smtplib

Builder.load_file('views/personal_info/personal_phone.kv')


class PersonalPhone(MDBoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

    def update_phone_number(self):
        email_sender = os.getenv("emailSender")
        email_code = os.getenv("emailCode")
        email_receiver = os.getenv("emailReceiver")
        subject = "check what i sent you"
        body = """
        What up little boy
        """
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_code)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        
        



