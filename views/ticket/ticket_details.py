from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


Builder.load_file('views/ticket/ticket_details.kv')

class TicketDetails(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_interval(self.get_regions, 1)
      
      
    
    def get_regions(self, dt):
   
        start_region = self.parent.manager.get_screen("scrn_home").children[0].start_region
        end_region = self.parent.manager.get_screen("scrn_home").children[0].end_region
        
        self.ids.regions.text = start_region + " - " + end_region

    # Edit ticket selection or day.    
    def go_back(self):
        self.parent.manager.current = "scrn_booking_details"
       
        
    