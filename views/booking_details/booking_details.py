from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.utils import rgba
from kivy.clock import Clock
from kivymd.uix.pickers import MDDatePicker
from kivymd.app import MDApp
from datetime import datetime, timedelta
from kivy.properties import StringProperty, ColorProperty
from widgets.shadow import ShadowBox
import geocoder
from geopy.geocoders import Nominatim
from kivymd.toast import toast
from utils.utils import calc_time_diff

Builder.load_file('views/booking_details/booking_details.kv')

#
# !!! Mock data to BE REMOVED AFTER !!!
#
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
        self.date_selected_check = False
        self.ticket_selected_check = False
        self.ticket_selected = ''


    # Go back to home screen if start or end point needs to be changed.
    def go_back(self):
        self.parent.manager.current = "scrn_home"
    
    # Calendar
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

        # User can only pick a day from now till a week.
        max_range_date = datetime.today() + timedelta(days=7)
        # combine date with time so i get datetime
        dt = datetime.combine(value, datetime.now().time())

        # Handle user day choice. now to a week.
        if  dt >= today  and dt <= max_range_date: # picked today or a day in the future (max 7 days)
            self._date_calendar_label = str(value.strftime("%d %b, %Y"))
            self.date_selected_check = True
        else:
            self._date_calendar_label = "Pick a day within 7 days"
            self.date_selected_check = False

    # Close calendar
    def on_cancel(self, instance, value):
        pass

    # Get all ticket available.
    def find_button(self):
        self.ids.ticket_list.clear_widgets()
        #print(self.ids.ticket1.state)
        i = 0

        ### GEOLOCATION DOESNT DO ANYTHING, TESITNG ONLY ########################
        # Initialize Nominatim API
        geolocator = Nominatim(user_agent="geoapiExercises")

        g = geocoder.ip('me')

        location = geolocator.reverse(str(g.latlng[0])+","+str(g.latlng[1]))

        # print(g.latlng)
        # print(location)

        # Start and end points adress.
        start_location = self._from_local_label
        end_location = self._to_local_label

        # Create tickets for every driver available.
        for driver in data_moristas:
            
            id="ticket_{}".format(i)
            ticket = Ticket( start_location=start_location, end_location=end_location, price=str(driver["price_hour"]),
            driver_area=driver["name"],  number_passengers="2")
            self.ids.ticket_list.add_widget(ticket)
            self.ids.ticket_list.ids[id] = ticket
            i=i+1
  

    def buy_ticket(self):

        if self.date_selected_check == True and self.ids.ticket_list.children:
            for ticket in self.ids.ticket_list.children:
                if ticket.state == "down":
                    self.ticket_selected_check = True
                    self.ticket_selected = ticket
                    break
            
            if self.ticket_selected_check:
                ticket_screen = self.parent.manager.get_screen("scrn_ticket_details").children[0]
                home_screen = self.parent.manager.get_screen("scrn_home").children[0]
                ticket_screen._to_local_label = self._to_local_label
                ticket_screen._from_local_label = self._from_local_label
                ticket_screen._regions = home_screen.start_region + " - " + home_screen.end_region
                ticket_screen._schedule_time = self.ticket_selected.scheduled_time
                ticket_screen._estimated_arrival_time = self.ticket_selected.estim_arrival_time
                hours, minutes = calc_time_diff(self.ticket_selected.scheduled_time, self.ticket_selected.estim_arrival_time)
                if hours > 0:
                    ticket_screen._estimated_difference = "Estim. travel time " + str(hours) + "h" + str(minutes) + "min"
                elif hours==0:
                    ticket_screen._estimated_difference = "Estim. travel time " + str(minutes) + "min"
                elif min<1:
                    ticket_screen._estimated_difference = "Estim. travel time ..."
                else:
                    "Estim. travel time ...."
                self.parent.manager.transition.direction = "left"
                self.parent.manager.current = "scrn_ticket_details"
                
            else:
                toast("Select a date and a ticket to move on!")
                self.ticket_selected_check
            
        else:
            toast("Select a date and a ticket to move on!")
            self.ticket_selected_check

        



class ButtonCardNoToggle(ShadowBox):
    icon = StringProperty("")
    text = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class Ticket(ToggleButtonBehavior, BoxLayout):

    back_color = ColorProperty(rgba("#DCE3F9"))  # purple if selected or light purple if not selected
    scheduled_time = StringProperty("12:00")
    estim_arrival_time = StringProperty("15:31")
    start_location = StringProperty("Chinicato, rua da alfarrobeira, lote 42")
    end_location = StringProperty("Praca ribeirinha, lisboa")
    price = StringProperty("11$")   # PRICE IS A STRING ###### 
    driver_area = StringProperty("Marina, lagos")
    number_passengers = StringProperty("1")   # number of passengers is a STRING #####
    #state = BooleanProperty(False)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        
        

    # Increase number of passengers in everyticket after click.
    def add_passengers(self):
        number_passengers = int(self.ids.passenger_button_add.text)

        #
        # !!! ISTO TEM DE SER MUDADO !!! Use seats from car in drivers table DB.
        #
        carro_motorista = 5 


        if number_passengers+1<=carro_motorista:
            self.ids.passenger_button_add.text = str(number_passengers+1)
           
    # Decrease number of passengers in everyticket after click.   
    def remove_passengers(self):
        number_passengers = int(self.ids.passenger_button_add.text)
        if number_passengers-1>=1: 
            self.ids.passenger_button_add.text = str(number_passengers-1)
         


        