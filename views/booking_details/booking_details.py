from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock
from kivymd.uix.pickers import MDDatePicker
from kivymd.app import MDApp
import inspect
import pprint
from datetime import date, datetime, timedelta
from kivy.properties import StringProperty, BooleanProperty, ListProperty, ColorProperty, NumericProperty
from widgets.buttons import FlatButton
from widgets.shadow import ShadowBox
import geocoder
from geopy.geocoders import Nominatim

Builder.load_file('views/booking_details/booking_details.kv')

data_moristas = [
    {
        "id": 1,
        "name":"Joao Carvalho",
        "price_hour": 10,
        "hour_start":9,
        "hour_end":18,
        "time_available":"17:30"
    },
    {
        "id": 2,
        "name":"Simoes",
        "price_hour": 11,
        "hour_start":12,
        "hour_end": 20,
        "time_available":"14:30"
        

    },
    {   
        "id": 3,
        "name":"Alecrim Silva",
        "price_hour": 10,
        "hour_start":10,
        "hour_end":19,
        "time_available":"18:00"
        

    },
    {   
        "id": 4,
        "name":"Pauleta costa",
        "price_hour": 10,
        "hour_start":10,
        "hour_end":19,
        "time_available":"19:00"
        

    },
    {   
        "id": 5,
        "name":"Piruka m6",
        "price_hour": 43,
        "hour_start":12,
        "hour_end":23,
        "time_available":"19:00"
        

    }
]


class BookingDetails(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()
        Clock.schedule_interval(self.get_to_local, 1)
        Clock.schedule_interval(self.get_from_local, 1)

    def get_start_location(self):
        return  self.parent.manager.get_screen("scrn_home").children[0].ids.my_location_label.text    
    
    def get_end_location(self):
        return  self.parent.manager.get_screen("scrn_home").children[0].ids.destination_label.text   

    def go_back(self):
        self.parent.manager.current = "scrn_home"
    
    def get_to_local(self, dt):
    #     o = inspect.getmembers(self.parent.manager.get_screen("scrn_home").children[0], lambda a:not(inspect.isroutine(a)))
    #     pp = pprint.PrettyPrinter(indent=4)
    #     pp.pprint(o)
        self.ids.from_local_label.text = self.get_start_location()
    def get_from_local(self, dt):
        self.ids.to_local_label.text = self.get_end_location()
    
    
    def show_date_picker(self):
       
        
       date_dialog = MDDatePicker(
        primary_color=self.app.colors.primary,
        accent_color="white",
        selector_color=rgba("#2BC48A"),
        text_color="black",
        text_button_color=rgba("#2BC48A")
       )
       date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
       
       date_dialog.open()
       
    
    def on_save(self, instance, value, date_range):
        today = datetime.today()
        max_range_date = datetime.today() + timedelta(days=7)
        # combine date with time so i get datetime
        dt = datetime.combine(value, datetime.now().time())
        if  dt >= today  and dt <= max_range_date: # picked today or a day in the future (max 7 days)
            self.ids.date_calendar_label.text = str(value.strftime("%d %b, %Y"))
        else:
            self.ids.date_calendar_label.text = "Pick a day within 7 days"

    def on_cancel(self, instance, value):
        pass

    def find_button(self):
        self.ids.ticket_list.clear_widgets()
        #print(self.ids.ticket1.state)
        i = 0
        # Initialize Nominatim API
        geolocator = Nominatim(user_agent="geoapiExercises")
        g = geocoder.ip('me')
        location = geolocator.reverse(str(g.latlng[0])+","+str(g.latlng[1]))
        print(g.latlng)
        print(location)
        start_location = self.get_start_location()
        end_location = self.get_end_location()
        for driver in data_moristas:
            
            id="ticket_{}".format(i)
            ticket = Ticket( start_location=start_location, end_location=end_location, price=str(driver["price_hour"]),
            driver_area=driver["name"],  number_passengers="2")
            self.ids.ticket_list.add_widget(ticket)
            self.ids.ticket_list.ids[id] = ticket
            i=i+1
  
    def buy_ticket(self):
        self.parent.manager.transition.direction = "left"
        self.parent.manager.current = "scrn_ticket_details"



class ButtonCardNoToggle(ShadowBox):
    icon = StringProperty("")
    text = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class Ticket(ToggleButtonBehavior, BoxLayout):
    
    back_color = ColorProperty(rgba("#DCE3F9"))  # purple if selected or light purple if not selected
    scheduled_time = StringProperty("15:00")
    estim_arrival_time = StringProperty("15:31")
    start_location = StringProperty("Chinicato, rua da alfarrobeira, lote 42")
    end_location = StringProperty("Praca ribeirinha, lisboa")
    price = StringProperty("11$")   # PRICE IS A STRING ###### 
    driver_area = StringProperty("Marina, lagos")
    number_passengers = StringProperty("1")   # number of passengers is a STRING #####
    # state = BooleanProperty(False)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        
        

    # Make function that increases numbr of passengers in everyticket after click
    ##  HERE ####
    def add_passengers(self):
        number_passengers = int(self.ids.passenger_button_add.text)
        carro_motorista = 5  # ISTO TEM DE SER MUDADO
        if number_passengers+1<=carro_motorista:
            self.ids.passenger_button_add.text = str(number_passengers+1)
           
       
    def remove_passengers(self):
        number_passengers = int(self.ids.passenger_button_add.text)
        if number_passengers-1>=1: 
            self.ids.passenger_button_add.text = str(number_passengers-1)
         


        