#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd 


dict_data = {'a':1,'b':2,'c':3}


sr = pd.Series(dict_data)


print(type(sr))
print("\n")

print(sr)