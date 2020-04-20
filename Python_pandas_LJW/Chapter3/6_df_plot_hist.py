#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5], 3:]
df_ns.index = ['South','North']
df_ns.columns = df_ns.columns.map(int)


tdf_ns = df_ns.T
tdf_ns.plot(kind='hist')