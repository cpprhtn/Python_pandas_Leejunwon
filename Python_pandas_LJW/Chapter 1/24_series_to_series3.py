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


sr_add = std1.add(std2,fill_value=0)
sr_sub = std1.sub(std2,fill_value=0)
sr_mul = std1.mul(std2,fill_value=0)
sr_div = std1.div(std2,fill_value=0)


result = pd.DataFrame([sr_add,sr_sub,sr_mul,sr_div],
                      index=['add','sub','mul','div'])
print(result)