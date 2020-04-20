#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


df = pd.read_csv('./auto-mpg.csv', header= None)


df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.mean())
print()
print(df['mpg'].mean())
print(df.mpg.mean())
print()
print(df[['mpg','weight']].mean())



print(df.median())
print()
print(df['mpg'].median())


print(df.max())
print()
print(df['mpg'].max())


print(df.min())
print()
print(df['mpg'].min())


print(df.std())
print()
print(df['mpg'].std())


print(df.corr())
print()
print(df[['mpg','weight']].corr())