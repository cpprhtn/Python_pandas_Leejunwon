#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns


titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

# class 열, sex 열을 기준으로 분할
grouped = df.groupby(['class', 'sex'])  

# 그룹 객체에 연산 메서드 적용
gdf = grouped.mean()
print(gdf)
print('\n')
print(type(gdf))

# class 값이 First인 행을 선택하여 출력
print(gdf.loc['First'])
print('\n')

# class 값이 First이고, sex 값이 female인 행을 선택하여 출력
print(gdf.loc[('First', 'female')])
print('\n')

# sex 값이 male인 행을 선택하여 출력
print(gdf.xs('male', level='sex'))
