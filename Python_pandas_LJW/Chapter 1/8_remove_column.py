#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


exam_data = {'수학' : [90,80,70], '영어' : [98,89,95], 
             '음악' : [85,95,100], '체육' : [100,90,90]}

df = pd.DataFrame(exam_data, index = ['준원','준서','전어'])
print(df)
print()


df4 = df[:]
df4.drop('수학',axis=1,inplace=True)
print(df4)
print()


df5 = df[:]
df5.drop(['영어','음악'],axis=1,inplace=True) #0일때는 행 삭제, 1일때는 열 삭제
print(df5)