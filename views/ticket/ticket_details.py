from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout




Builder.load_file('views/ticket/ticket_details.kv')

class TicketDetails(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
    
    def go_back(self):
        self.parent.manager.current = "scrn_booking_details"