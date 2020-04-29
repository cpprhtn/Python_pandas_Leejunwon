#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns


titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]


grouped = df.groupby(['class']) 

# 집계 : 각 그룹별 요약 통계정보를 집계
agg_grouped = grouped.apply(lambda x: x.describe())   
print(agg_grouped)
print('\n')

# z-score를 계산하는 사용자 함수 정의
def z_score(x):                          
    return (x - x.mean()) / x.std()

age_zscore = grouped.age.apply(z_score)   #기본값 axis=0 
print(age_zscore.head())
print('\n')

# 필터링 : age 열의 데이터 평균이 30보다 작은 그룹만을 필터링하여 출력
age_filter = grouped.apply(lambda x: x.age.mean() < 30)  
print(age_filter)   
print('\n')
for x in age_filter.index:
    if age_filter[x]==True:
        age_filter_df = grouped.get_group(x)
        print(age_filter_df.head())
        print('\n')