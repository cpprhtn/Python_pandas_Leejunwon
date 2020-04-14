#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


exam_data = {'수학' : [90,80,70], '영어' : [98,89,95], 
             '음악' : [85,95,100], '체육' : [100,90,90]}

df = pd.DataFrame(exam_data, index = ['준원','준서','전어'])
print(df)
print()


df2 = df[:]
df2.drop('준서',inplace=True)
print(df2)
print()


df3 = df[:]
df3.drop(['준서','전어'],axis=0, inplace=True)
print(df3)