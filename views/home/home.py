
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.clock import Clock
from kivy.graphics import Color, Line
from kivy.garden.mapview import MapView, MapMarkerPopup
from kivy.properties import StringProperty, ColorProperty

from widgets.shadow import ShadowBox

from plyer import gps
from .openrouteservicecalls import get_street_from_coordinates, openrouteservice_request


Builder.load_file('views/home/home.kv')

class Home(BoxLayout):
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        # check if starting point was placed.
        self.my_pin_placed = False

        # check if end point was placed.
        self.dest_pin_placed = False

        # starting point pin marker.
        self.my_pin = ""  # object type

        # end point pin marker.
        self.dest_pin = ""  # object type

        
        # Check if starting point button was pressed.
        self.my_loc_flag_button = False

        # Check if ending point button was pressed.
        self.dest_loc_flag_button = False

        #  Used to check if user clicks inside the map view
        self.map_pos = []

        # Markers between start and end point. will be used to draw the lines between each of these points.
        self.route_points = []

        # List of lines created by every two points next to each other till we reach end point.
        self.list_of_lines = []


        # Region of starting point
        self.start_region = ""

        # Region of ending point
        self.end_region = ""
        
        
       
    def render(self, _):
        # When class object is created render is ran.
        # Add the center position of map view. What user sees when loads Home component.
        # !!! Own user gps location will be added, in the future. !!!


        self.ids.main_map.lat = 38.736946
        self.ids.main_map.lon = -9.142685
        self.ids.main_map.zoom = 14
        self.map_pos.append(self.ids.main_map.lat)
        self.map_pos.append(self.ids.main_map.lon)

    # Update start region where start pin is located on the map.
    def set_start_region(self, reg):
        self.start_region = reg
    
    # Update end region where end pin is located on the map.
    def set_end_region(self, reg):
        self.end_region = reg
 
    # Changes place pin button colors for start pin button. Pin can only be placed when this button is selected.
    def on_press_my_location(self):
        
        if self.my_loc_flag_button==False:
            if self.dest_loc_flag_button == False:
                self.my_loc_flag_button = True
                self.ids.my_local_button.color = [1,0,0,1]
          
        else:
            self.my_loc_flag_button = False
            self.ids.my_local_button.color = [0,0,0,1]

    # Changes place pin button colors for end pin button. Pin can only be placed when this button is selected.
    def on_press_destination(self):
        
        if self.dest_loc_flag_button == False:
            if self.my_loc_flag_button == False:
                self.dest_loc_flag_button = True
                self.ids.destination_local_button.color = [1,0,0,1]
           
        else:
            self.dest_loc_flag_button = False
            self.ids.destination_local_button.color = [0,0,0,1]
 
    # Remove pin from map, start or end.
    def remove_pin(self, pin):
        self.ids.main_map.remove_widget(pin)
        
    # Remove path between the two points when one pin has been removed or hasnt been placed.
    def invalidate_line(self):

        if self.route_points:
            for i in self.route_points:
                self.remove_widget(i)
        if self.list_of_lines:
            for i in self.list_of_lines: 
                self.canvas.remove(i)
        self.route_points.clear()
        self.list_of_lines.clear()
        

    # Creates pins on map, if both are placed path is created.
    def on_touch_up(self, touch):
        
        # If user pressed on the map view component:
        if touch.y < self.ids.main_map.height+self.ids.main_map.pos[1] and touch.y > self.ids.main_map.pos[1]:
            # If mouse is not being scroll and start point button is being placed and start pin has not been placed.
            if not touch.is_mouse_scrolling and self.ids.main_map.lat==self.map_pos[0] and self.ids.main_map.lon==self.map_pos[1] and not self.my_pin_placed and self.my_loc_flag_button:
                
                self.my_pin_placed = True 

                # Get latitude and longitude where user pressed
                latitude = self.ids.main_map.get_latlon_at(touch.x-self.ids.main_map.pos[0], touch.y-self.ids.main_map.pos[1])[0]
                longitude = self.ids.main_map.get_latlon_at(touch.x-self.ids.main_map.pos[0], touch.y-self.ids.main_map.pos[1])[1]
                
                # Place marker where user pressed
                self.my_pin = MapMarkerPopup(lat=latitude, lon=longitude, source='assets/imgs/preto.png')

                # Add pin to mapview
                self.ids.main_map.add_widget(self.my_pin)

                # Get label and region. Label will be used in every component describing the adress of a point. Like my_location_label, ... 
                # Region is used in the ticket details.
                label, region = get_street_from_coordinates(latitude, longitude)

                # Set start region for the ticket details to be updated.
                self.set_start_region(region)

                # Updates start point description label. Default is "start"
                self.ids.my_location_label.text = label

                # If both points are placed we created path between them.
                if self.my_pin and self.dest_pin:
                    self.points_line()

            # If mouse is not being scroll and start point button is being placed and start pin has been placed remove pin and remove path between points if both were placed.
            elif not touch.is_mouse_scrolling and self.ids.main_map.lat==self.map_pos[0] and self.ids.main_map.lon==self.map_pos[1] and self.my_pin_placed and self.my_loc_flag_button:
                # Erase path line between
                if self.my_pin and self.dest_pin:
                    self.invalidate_line()

                # Remove pin from map view.
                self.remove_pin(self.my_pin)
                self.my_pin = ""

                self.my_pin_placed = False  # Flag

                # Reset label to default text.
                self.ids.my_location_label.text = "Start"

            # If mouse is not being scroll and end point button is being placed and end pin has not been placed.
            elif not touch.is_mouse_scrolling and   self.ids.main_map.lat==self.map_pos[0] and self.ids.main_map.lon==self.map_pos[1] and not self.dest_pin_placed  and self.dest_loc_flag_button  :
                
                self.dest_pin_placed = True

                # Get latitude and longitude where user pressed
                latitude = self.ids.main_map.get_latlon_at(touch.x-self.ids.main_map.pos[0], touch.y-self.ids.main_map.pos[1])[0]
                longitude = self.ids.main_map.get_latlon_at(touch.x-self.ids.main_map.pos[0], touch.y-self.ids.main_map.pos[1])[1]

                # Place marker where user pressed
                self.dest_pin = MapMarkerPopup(lat=latitude, lon=longitude, source='assets/imgs/red.png')

                # Add pin to mapview
                self.ids.main_map.add_widget(self.dest_pin)

                # Get label and region. Label will be used in every component describing the adress of a point. Like destination_label, ... 
                # Region is used in the ticket details.
                label, region = get_street_from_coordinates(latitude, longitude)

                # Set end point region for the ticket details to be updated.
                self.set_end_region(region)

                # Updates end point description label. Default is "Destination"
                self.ids.destination_label.text = label

                 # If both points are placed we created path between them.
                if self.my_pin and self.dest_pin:   
                    self.points_line()
            
            # If mouse is not being scroll and end point button is being placed and end pin has been placed remove pin and remove path between points if both were placed.
            elif not touch.is_mouse_scrolling and   self.ids.main_map.lat==self.map_pos[0] and self.ids.main_map.lon==self.map_pos[1] and self.dest_pin_placed  and self.dest_loc_flag_button  :
                # Erase path line between points if end point is removed.
                if self.my_pin and self.dest_pin:
                    self.invalidate_line() 

                 # Remove pin from map view.
                self.remove_pin(self.dest_pin)
                self.dest_pin = ""

                self.dest_pin_placed = False  # Flag

                # Reset label to default text.
                self.ids.destination_label.text = "Destination"
                 
            else:
                 # in case button is pressed when dragging map
                self.map_pos[0] = self.ids.main_map.lat
                self.map_pos[1] = self.ids.main_map.lon



    # Get
    def points_line(self, *args):
        # Get latitude and longitude of both pins 
        self.start_lon = self.my_pin.lon
        self.start_lat = self.my_pin.lat

        self.end_lon = self.dest_pin.lon
        self.end_lat = self.dest_pin.lat

        # Get all points between them to create markers in those points. And use these markers to create a path line.
        self.body = {"coordinates":[[self.start_lon, self.start_lat],[self.end_lon, self.end_lat]]}
        self.res1 = openrouteservice_request(self.body)

        for i in range(0, len(self.res1)-1, 2):

            self.points_lat = self.res1[i]
            self.points_lon = self.res1[i+1]

            # Place marker in every point.
            self.points_pop = MapMarkerPopup(lat=self.points_lat, lon=self.points_lon, source='assets/imgs/waypoints.png')
            self.route_points.append(self.points_pop)
           
           # Add all marker points to map view.
            self.ids.main_map.add_widget(self.points_pop)

        # Every adjacent two markers a line is created. The sum of this lines makes a path between start and end pins.
        with self.canvas:
            Color(0.5, 0, 0 ,1)
            for j in range(0, len(self.route_points)-1, 1):
                self.lines = Line(points=(self.route_points[j].pos[0],self.route_points[j].pos[1], self.route_points[j+1].pos[0],self.route_points[j+1].pos[1] ), width=3)
                self.list_of_lines.append(self.lines)

        # If mapview changes view (user zooms out, for example), line is updated to fit this change. 
        Clock.schedule_interval(self.update_route_lines, 1/50)

    def update_route_lines(self, *args):
        for j in range(1, len(self.route_points), 1):
            self.list_of_lines[j-1].points = [self.route_points[j-1].pos[0],self.route_points[j-1].pos[1], self.route_points[j].pos[0], self.route_points[j].pos[1]]

    # Button next on_press(). If both pins are placed user can move on in the ticket sale.
    def press_next(self):
        # 
        # !!! UNCOMMENT AFTER !!!
        #

        # if self.my_pin_placed and self.dest_pin_placed:
        #     self.parent.manager.current = "scrn_booking_details"
            #self.parent.manager.transition.direction = "right"
        self.parent.manager.transition.direction = "left"
        self.parent.manager.current = "scrn_booking_details"

# Map component        
class Map(MapView):


    def __init__(self, **kw) -> None:
        super().__init__(**kw)


# Icon label that acts has a button
class ButtonIcon(ButtonBehavior, Label):
    color = ColorProperty([0,0,1,1])
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

# BoxLayout that acts has a button.
class ButtonCard(ToggleButtonBehavior, ShadowBox):
    icon = StringProperty("")
    text = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

