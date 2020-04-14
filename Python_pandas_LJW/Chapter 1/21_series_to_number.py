#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


student1 = pd.Series({'kor':100,'en':80,'math':90})
print(student1)
print()


percentage = student1/200

print(percentage)
print()
print(type(percentage))