#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


df = pd.read_excel('./주가데이터.xlsx')
print(df.head(), '\n')
print(df.dtypes, '\n')

# 연, 월, 일 데이터 분리하기
df['연월일'] = df['연월일'].astype('str')   # 문자열 메소드 사용을 자료형 변경
dates = df['연월일'].str.split('-')        # 문자열을 split() 메서드로 분리
print(dates.head(), '\n')

# 분리된 정보를 각각 새로운 열에 담아서 df에 추가하기
df['연'] = dates.str.get(0)     # dates 변수의 원소 리스트의 0번째 인덱스 값
df['월'] = dates.str.get(1)     # dates 변수의 원소 리스트의 1번째 인덱스 값 
df['일'] = dates.str.get(2)     # dates 변수의 원소 리스트의 2번째 인덱스 값
print(df.head())