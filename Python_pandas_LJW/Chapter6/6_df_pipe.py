#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import seaborn as sns


titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]

# 각 열의 NaN 찾기 - 데이터프레임 전달하면 데이터프레임을 반환
def missing_value(x):    
    return x.isnull()    

# 각 열의 NaN 개수 반환 - 데이터프레임 전달하면 시리즈 반환
def missing_count(x):    # 
    return missing_value(x).sum()

# 데이터프레임의 총 NaN 개수 - 데이터프레임 전달하면 값을 반환
def totoal_number_missing(x):    
    return missing_count(x).sum()
    
# 데이터프레임에 pipe() 메소드로 함수 매핑
result_df = df.pipe(missing_value)   
print(result_df.head())
print(type(result_df))
print('\n')

result_series = df.pipe(missing_count)   
print(result_series)
print(type(result_series))
print('\n')

result_value = df.pipe(totoal_number_missing)   
print(result_value)
print(type(result_value))