#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


df = pd.read_csv('stock-data.csv')


print(df.head())
print('\n')
print(df.info())

# 문자열 데이터(시리즈 객체)를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])   #df에 새로운 열로 추가


print(df.head())
print('\n')
print(df.info())
print('\n')
print(type(df['new_Date'][0]))

# 시계열 값으로 변환된 열을 새로운 행 인덱스로 지정. 기존 날짜 열은 삭제
df.set_index('new_Date', inplace=True)
df.drop('Date', axis=1, inplace=True)


print(df.head())
print('\n')
print(df.info())
