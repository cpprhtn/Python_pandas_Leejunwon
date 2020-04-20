#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5], 3:]
df_ns.index = ['South','North']
df_ns.columns = df_ns.columns.map(int)
print(df_ns.head())
print()

#선 그래프
df_ns.plot()

#행, 열 전치하여 다시그리기
tdf_ns = df_ns.T
print(tdf_ns.head())
print()
tdf_ns.plot()
