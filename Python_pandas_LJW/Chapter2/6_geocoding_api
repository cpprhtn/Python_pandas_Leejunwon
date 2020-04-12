#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import googlemaps
import pandas as pd

my_key = ""


maps = googlemaps.Client(key=my_key)

lat = []
lng = []


places = ['seoul','busan']

i =0
for place in places:
    i = i + 1
    try:
        print(i, place)
        
        geo_location = maps.geocode(place)[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])
        
    except:
        lat.append('')
        lng.append('')
        print(i)
        
        
df = pd.DataFrame({'위도':lat, '경도':lng}, index=places)
print()
print(df)