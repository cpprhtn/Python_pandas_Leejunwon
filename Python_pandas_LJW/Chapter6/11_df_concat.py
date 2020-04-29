#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                    index=[0, 1, 2, 3])
 
df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                    index=[2, 3, 4, 5])

print(df1, '\n')
print(df2, '\n')

# 2개의 데이터프레임을 위 아래 행 방향으로 이어 붙이듯 연결하기 
result1 = pd.concat([df1, df2])
print(result1, '\n')


# ignore_index=True 옵션 설정하기 
result2 = pd.concat([df1, df2], ignore_index=True)
print(result2, '\n')

# 2개의 데이터프레임을 좌우 열 방향으로 이어 붙이듯 연결하기 
result3 = pd.concat([df1, df2], axis=1)
print(result3, '\n')

# join='inner' 옵션 적용하기(교집합)
result3_in = pd.concat([df1, df2], axis=1, join='inner')
print(result3_in, '\n')

# 시리즈 만들기
sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')

# df1과 sr1을 좌우 열 방향으로 연결하기
result4 = pd.concat([df1, sr1], axis=1)
print(result4, '\n')

# df2과 sr2을 좌우 열 방향으로 연결하기
result5 = pd.concat([df2, sr2], axis=1, sort=True)
print(result5, '\n')

# sr1과 sr3을 좌우 열 방향으로 연결하기
result6 = pd.concat([sr1, sr3], axis=1)
print(result6, '\n')

result7 = pd.concat([sr1, sr3], axis=0)
print(result7, '\n')
