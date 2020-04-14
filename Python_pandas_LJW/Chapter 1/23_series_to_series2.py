#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


std1 = pd.Series({'kor':np.nan,'en':80,'math':90})
std2 = pd.Series({'math':80,'kor':90})

print(std1)
print()
print(std2)
print()


addition = std1 + std2
subtraction = std1 - std2
multiplication = std1*std2
division = std1/std2
print(type(division))
print()


result = pd.DataFrame([addition,subtraction,multiplication,division],
                      index=['add','sub','multi','div'])
print(result)