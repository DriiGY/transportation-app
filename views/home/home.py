
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.uix.label import Label
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.clock import Clock
import random
from math import *
from kivy.core.image import Image
from kivy.graphics import Color, Line, SmoothLine
from kivy.graphics.context_instructions import Translate, Scale
from kivy.garden.mapview.mapview.utils import clamp
from kivy.garden.mapview.mapview import MapLayer, MIN_LONGITUDE, MIN_LATITUDE, MAX_LATITUDE, MAX_LONGITUDE 
from kivy.garden.mapview import MarkerMapLayer, MapView, MapMarkerPopup

from widgets.shadow import ShadowBox
from kivy.properties import StringProperty, BooleanProperty, ListProperty, ColorProperty, NumericProperty

import pprint
import requests
import re
import json
import os
from credentials import API_KEY


Builder.load_file('views/home/home.kv')

class Home(BoxLayout):
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        
        self.my_pin_placed = False
        self.dest_pin_placed = False
        self.exists = False
        self.my_pin = ""  # object type
        self.map_pos = []
        self.dest_pin_placed = False
        self.dest_pin = ""  # object type
        self.my_loc_flag_button = False
        self.dest_loc_flag_button = False
        self.list_of_lines = []
        self.route_points = []
        Clock.schedule_interval(self.get_name_me, 0.1)
        Clock.schedule_interval(self.get_name_dest, 0.1)
        
    def render(self, _):
        # self.get_map()
        # self.ids.main_map.center_on(self.ids.main_map_me.lat, self.ids.main_map_me.lon)
        self.ids.main_map.lat = 38.736946
        self.ids.main_map.lon = -9.142685
        self.ids.main_map.zoom = 14
        self.map_pos.append(self.ids.main_map.lat)
        self.map_pos.append(self.ids.main_map.lon)

 


    def on_press_my_location(self):
        
        if self.my_loc_flag_button==False:
            if self.dest_loc_flag_button == False:
                self.my_loc_flag_button = True
                self.ids.my_local_button.color = [1,0,0,1]
          
        else:
            self.my_loc_flag_button = False
            self.ids.my_local_button.color = [0,0,0,1]

    def on_press_destination(self):
        
        if self.dest_loc_flag_button == False:
            if self.my_loc_flag_button == False:
                self.dest_loc_flag_button = True
                self.ids.destination_local_button.color = [1,0,0,1]
           
        else:
            self.dest_loc_flag_button = False
            self.ids.destination_local_button.color = [0,0,0,1]
 

    def remove_pin(self, pin):
        self.ids.main_map.remove_widget(pin)
        

    def invalidate_line(self):

        if self.route_points:
            for i in self.route_points:
                self.remove_widget(i)
        if self.list_of_lines:
            for i in self.list_of_lines: 
                self.canvas.remove(i)
        self.route_points.clear()
        self.list_of_lines.clear()
        


    def on_touch_up(self, touch):
        # print(self.map_pos)
    
        if touch.y < self.ids.main_map.height+self.ids.main_map.pos[1] and touch.y > self.ids.main_map.pos[1]:
            if not touch.is_mouse_scrolling and self.ids.main_map.lat==self.map_pos[0] and self.ids.main_map.lon==self.map_pos[1] and not self.my_pin_placed and self.my_loc_flag_button:
                print(self.my_pin_placed)
                self.my_pin_placed = True 
                latitude = self.ids.main_map.get_latlon_at(touch.x-self.ids.main_map.pos[0], touch.y-self.ids.main_map.pos[1])[0]
                longitude = self.ids.main_map.get_latlon_at(touch.x-self.ids.main_map.pos[0], touch.y-self.ids.main_map.pos[1])[1]
                # we do not need to verify for x bc map occupies 100% of x
                self.my_pin = MapMarkerPopup(lat=latitude, lon=longitude, source='assets/imgs/preto.png')
                self.ids.main_map.add_widget(self.my_pin)
                label = self.get_street_from_coordinates(latitude, longitude)
                self.ids.my_location_label.text = label
                if self.my_pin and self.dest_pin:
                   
                    self.points_line()
            elif not touch.is_mouse_scrolling and self.ids.main_map.lat==self.map_pos[0] and self.ids.main_map.lon==self.map_pos[1] and self.my_pin_placed and self.my_loc_flag_button:
                self.remove_pin(self.my_pin)
                self.my_pin = ""
                self.invalidate_line()
                self.my_pin_placed = False
                self.ids.my_location_label.text = "Location"

            elif not touch.is_mouse_scrolling and   self.ids.main_map.lat==self.map_pos[0] and self.ids.main_map.lon==self.map_pos[1] and not self.dest_pin_placed  and self.dest_loc_flag_button  :
                
                self.dest_pin_placed = True
                latitude = self.ids.main_map.get_latlon_at(touch.x-self.ids.main_map.pos[0], touch.y-self.ids.main_map.pos[1])[0]
                longitude = self.ids.main_map.get_latlon_at(touch.x-self.ids.main_map.pos[0], touch.y-self.ids.main_map.pos[1])[1]
                self.dest_pin = MapMarkerPopup(lat=latitude, lon=longitude, source='assets/imgs/red.png')
                self.ids.main_map.add_widget(self.dest_pin)
                label = self.get_street_from_coordinates(latitude, longitude)
                self.ids.destination_label.text = label
                if self.my_pin and self.dest_pin:   
                    self.points_line()
            elif not touch.is_mouse_scrolling and   self.ids.main_map.lat==self.map_pos[0] and self.ids.main_map.lon==self.map_pos[1] and self.dest_pin_placed  and self.dest_loc_flag_button  :
                self.remove_pin(self.dest_pin)
                self.dest_pin = ""
                self.invalidate_line()
                self.dest_pin_placed = False
                self.ids.destination_label.text = "Location"
                 
            else:
                 # in case button is pressed when dragging map
                self.map_pos[0] = self.ids.main_map.lat
                self.map_pos[1] = self.ids.main_map.lon


    
    def get_name_me(self, *args):
        # when its just a empty string gives False like ""
        if self.my_pin:
            pass

    def get_name_dest(self, *args):
        if self.dest_pin:
            pass

    def get_street_from_coordinates(self, lat, lon):
        print("GET STREET FROM COORDINATES:")
        self.headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }
        self.call = requests.get('https://api.openrouteservice.org/geocode/reverse?api_key={}&point.lon={}&point.lat={}'.format(API_KEY, lon, lat), headers=self.headers)
        res = json.loads(self.call.text)
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(res['features'][0]['properties']['label'])
        return res['features'][0]['properties']['label']
    def openrouteservice_request(self, body):
        self.headers = {
                'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
                'Authorization': API_KEY,
                'Content-Type': 'application/json; charset=utf-8'
                }
        self.call = requests.post('https://api.openrouteservice.org/v2/directions/driving-car/gpx', json=body, headers=self.headers)           
        #print(self.call.text)
        self.string_res = self.call.text

        #print(self.string_res)

        self.tag = 'rtept'
        self.reg_str = '</' + self.tag + '>(.*?)' + '>'
        self.res = re.findall(self.reg_str, self.string_res)
        #print(self.res)
        print('_____________________________________')
        self.string1 = str(self.res)
        self.tag1 = '"'
        self.reg_str1 = '"' + '(.*?)' + '"'
        self.final = re.findall(self.reg_str1, self.string1)
        print()
        print()
        #print(self.final)
        return self.final



    def points_line(self, *args):
        if self.my_pin and self.dest_pin:
            #print(self.my_pin.lat)
            #print(self.my_pin.lon)
            self.start_lon = self.my_pin.lon
            self.start_lat = self.my_pin.lat

            self.end_lon = self.dest_pin.lon
            self.end_lat = self.dest_pin.lat
            self.body = {"coordinates":[[self.start_lon, self.start_lat],[self.end_lon, self.end_lat]]}
            self.res1 = self.openrouteservice_request(self.body)

            for i in range(0, len(self.res1)-1, 2):
                # print('lat= ' + self.res1[i])
                # print('lon= ' + self.res1[i+1])

                self.points_lat = self.res1[i]
                self.points_lon = self.res1[i+1]

                self.points_pop = MapMarkerPopup(lat=self.points_lat, lon=self.points_lon, source='assets/imgs/waypoints.png')
                self.route_points.append(self.points_pop)
                #print(type(self.points_pop))
                self.ids.main_map.add_widget(self.points_pop)

            with self.canvas:
                Color(0.5, 0, 0 ,1)
                for j in range(0, len(self.route_points)-1, 1):
                    self.lines = Line(points=(self.route_points[j].pos[0],self.route_points[j].pos[1], self.route_points[j+1].pos[0],self.route_points[j+1].pos[1] ), width=3)
                    self.list_of_lines.append(self.lines)

            Clock.schedule_interval(self.update_route_lines, 1/50)

    def update_route_lines(self, *args):
        for j in range(1, len(self.route_points), 1):
            self.list_of_lines[j-1].points = [self.route_points[j-1].pos[0],self.route_points[j-1].pos[1], self.route_points[j].pos[0], self.route_points[j].pos[1]]


    def press_next(self):
        # if self.my_pin_placed and self.dest_pin_placed:
        #     self.parent.manager.current = "scrn_booking_details"
            #self.parent.manager.transition.direction = "right"
        self.parent.manager.transition.direction = "left"
        self.parent.manager.current = "scrn_booking_details"
        
class Map(MapView):


    def __init__(self, **kw) -> None:
        super().__init__(**kw)



class ButtonIcon(ButtonBehavior, Label):
    color = ColorProperty([0,0,1,1])
    def __init__(self, **kw) -> None:
        super().__init__(**kw)


class ButtonCard(ToggleButtonBehavior, ShadowBox):
    icon = StringProperty("")
    text = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

