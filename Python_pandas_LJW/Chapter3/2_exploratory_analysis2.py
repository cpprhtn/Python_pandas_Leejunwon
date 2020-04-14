#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


df= pd.read_csv('./auto-mpg.csv', header=None)


df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']


print(df.count())
print()


print(type(df.count()))



unique_values = df['origin'].value_counts()
print(unique_values)
print()


print(type(unique_values))
