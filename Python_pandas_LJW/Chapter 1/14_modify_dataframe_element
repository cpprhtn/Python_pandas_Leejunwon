#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


exam_data = {'name' : ['seo','woo','lna'],
             'math' : [90,80,70], 
             'eng' : [98,89,95], 
             'music' : [85,95,100], 
             'pe' : [100,90,90]}
df = pd.DataFrame(exam_data)


df.set_index('name',inplace=True)
print(df)
print()


df.iloc[0][3] = 80
print(df)


df.loc['seo']['pe']= 90
print(df)


df.loc['seo','pe'] = 100
print(df)



df.loc['seo',['music','pe']] = 50
print(df)


df.loc['seo',['music','pe']] = 100,50
print(df)
