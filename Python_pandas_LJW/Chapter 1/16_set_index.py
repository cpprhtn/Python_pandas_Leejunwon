#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


exam_data = {'name' : ['seo','woo','lna'],
             'math' : [90,80,70], 
             'eng' : [98,89,95], 
             'music' : [85,95,100], 
             'pe' : [100,90,90]}
df = pd.DataFrame(exam_data)
print(df)
print()


ndf = df.set_index(['name'])
print(ndf)
print()
ndf2 = ndf.set_index('music')
print(ndf2)
print()
ndf3 = ndf.set_index(['math','music'])
print(ndf3)