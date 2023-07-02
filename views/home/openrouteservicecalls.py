import requests
import re
import json

import os
#import pprint
API_KEY = f"{os.getenv('API_KEY')}"

def get_street_from_coordinates(lat, lon):
  
        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }
        call = requests.get('https://api.openrouteservice.org/geocode/reverse?api_key={}&point.lon={}&point.lat={}'.format(API_KEY, lon, lat), headers=headers)
        res = json.loads(call.text)
        #print(res)
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(res['features'][0]) # ['properties']['region']
        
        return res['features'][0]['properties']['label'], res['features'][0]['properties']['region']

def openrouteservice_request(body):
        headers = {
                'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
                'Authorization': API_KEY,
                'Content-Type': 'application/json; charset=utf-8'
                }
        call = requests.post('https://api.openrouteservice.org/v2/directions/driving-car/gpx', json=body, headers=headers)           
        #print(call.text)
        string_res = call.text

        #print(string_res)
        tag = 'rtept'
        reg_str = '</' + tag + '>(.*?)' + '>'
        res = re.findall(reg_str, string_res)
       
        string1 = str(res)
        tag1 = '"'
        reg_str1 = '"' + '(.*?)' + '"'
        final = re.findall(reg_str1, string1)
        #print(final)
        return final