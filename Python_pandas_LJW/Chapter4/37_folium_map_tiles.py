#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import folium


seoul_map2 = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)
seoul_map3 = folium.Map(location=[37.55,126.98], tiles='Stamen Toner', 
                        zoom_start=15)


seoul_map2.save('./seoul2.html')
seoul_map3.save('./seoul3.html')