#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


exam_data = {'수학' : [90,80,70], '영어' : [98,89,95], 
             '음악' : [85,95,100], '체육' : [100,90,90]}

df = pd.DataFrame(exam_data, index = ['준원','준서','전어'])
print(df)
print()


label1 = df.loc['준원']
position1 = df.iloc[0]
print(label1)
print()
print(position1)



label2 = df.loc[['준서','전어']]
position2 = df.iloc[[1,2]]
print(label2)
print()
print(position2)



label3 = df.loc["준원":'준서']
position3 = df.iloc[0:1]
print(label3)
print()
print(position3)