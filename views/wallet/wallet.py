from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.properties import StringProperty
Builder.load_file('views/wallet/wallet.kv')


class Wallet(MDBoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()



class PaymentCardsListItem(MDBoxLayout):
    card_icon = StringProperty("")
    card_number = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()