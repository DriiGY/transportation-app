from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


Builder.load_file('views/ticket/ticket_details.kv')

class TicketDetails(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)


    # Edit ticket selection or day.    
    def go_back(self):
        self.parent.manager.current = "scrn_booking_details"
       
        
    