#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


student1 = pd.Series({'kor':100,'eng':80,'math':90})
student2 = pd.Series({'math':80,'kor':90,'eng':80})

print(student1)
print()
print(student2)
print()


addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1/student2
print(type(division))
print()


result = pd.DataFrame([addition,subtraction,multiplication,division],
                      index = ['add','sub','multi','div'])
print(result)