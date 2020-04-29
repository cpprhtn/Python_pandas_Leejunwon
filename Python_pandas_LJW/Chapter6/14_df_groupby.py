#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns


titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

print('승객 수:', len(df))
print(df.head())
print('\n')

# class 열을 기준으로 분할
grouped = df.groupby(['class']) 
print(grouped)
print('\n')

# 그룹 객체를 iteration으로 출력: head() 메소드로 첫 5행만을 출력
for key, group in grouped:
    print('* key :', key)
    print('* number :', len(group))    
    print(group.head())
    print('\n')
    
# 연산 메소드 적용
average = grouped.mean()
print(average)
print('\n')

# 개별 그룹 선택하기
group3 = grouped.get_group('Third')
print(group3.head())
print('\n')

# class 열, sex 열을 기준으로 분할
grouped_two = df.groupby(['class', 'sex']) 

# grouped_two 그룹 객체를 iteration으로 출력
for key, group in grouped_two:
    print('* key :', key)
    print('* number :', len(group))    
    print(group.head())
    print('\n')
    
# grouped_two 그룹 객체에 연산 메소드 적용
average_two = grouped_two.mean()
print(average_two)
print('\n')
print(type(average_two))

# grouped_two 그룹 객체에서 개별 그룹 선택하기
group3f = grouped_two.get_group(('Third','female'))
print(group3f.head())