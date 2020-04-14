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



a = df.loc['seo','music']
print(a)
b=df.iloc[0,2]
print(b)



c=df.loc['seo',['music','pe']]
print(c)
d=df.iloc[0,[2,3]]
print(d)
e=df.loc['seo','music':'pe']
print(e)
f=df.iloc[0,2:]
print(f)



g=df.loc[['seo','woo'],['music','pe']]
print(g)
h=df.iloc[[0,2],[2,3]]
print(h)
i=df.loc['seo':'woo','music':'pe']
print(i)
j=df.iloc[0:2,2:]
print(j)
