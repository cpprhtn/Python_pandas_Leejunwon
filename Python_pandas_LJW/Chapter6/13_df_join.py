#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


pd.set_option('display.max_columns', 10)                
pd.set_option('display.max_colwidth', 20)              
pd.set_option('display.unicode.east_asian_width', True)

# 주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel('./stock price.xlsx', index_col='id')
df2 = pd.read_excel('./stock valuation.xlsx', index_col='id')

# 데이터프레임 결합(join)
df3 = df1.join(df2)
print(df3)
print('\n')

# 데이터프레임 결합(join) - 교집합
df4 = df1.join(df2, how='inner')
print(df4)

