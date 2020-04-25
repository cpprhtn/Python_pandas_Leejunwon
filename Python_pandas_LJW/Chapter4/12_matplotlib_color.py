#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib


colors={}


for name, hex in matplotlib.colors.cnames.items():
	colors[name] = hex

 
print(colors)
