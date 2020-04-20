#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


df= pd.read_csv('./auto-mpg.csv', header=None)


df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']


df.plot(x='weight',y='mpg',kind='scatter')