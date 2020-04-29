#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import seaborn as sns


titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
df['ten'] = 10
print(df.head())
print('\n')


def add_two_obj(a, b):    # 두 객체의 합
    return a + b
    
# 데이터프레임의 2개 열을 선택하여 적용
# x=df, a=df['age'], b=df['ten']
df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['ten']), axis=1)   
print(df.head())
