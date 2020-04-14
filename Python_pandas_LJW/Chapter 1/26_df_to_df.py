#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns


titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.tail())
print()
print(type(df))
print()


addition = df + 10
print(addition.tail())
print()
print(type(addition))
print()


subtraction = addition - df
print(subtraction.tail())
print()
print(type(subtraction))