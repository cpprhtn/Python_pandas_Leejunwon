#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import seaborn as sns


titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')


def add_10(n):
    return n + 10
    
# 데이터프레임에 applymap()으로 add_10() 함수를 매핑 적용
df_map = df.applymap(add_10)   
print(df_map.head())
