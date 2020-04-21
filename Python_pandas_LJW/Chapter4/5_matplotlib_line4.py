#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

#matplotlib 한글 폰트 오류 문제 해결
from matplotlib import rc
rc('font', family='AppleGothic')




df = pd.read_excel('시도별 전출입 인구수.xlsx', fillna=0,header=0)

#누락값을 앞 데이터로 채움
df = df.fillna(method='ffill')

 
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'],axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지',inplace=True)
df_seoul.head()

sr_one = df_seoul.loc['경기도']


plt.style.use('ggplot')


plt.figure(figsize=(14,5))


plt.xticks(size=10,rotation='vertical')


plt.plot(sr_one.index,sr_one.values,marker='o',markersize=10)

plt.title('서울 -> 경기 인구 이동',size=30)
plt.xlabel('기간',size=20)
plt.ylabel('이동 인구수',size=20)

plt.legend(labels=['서울 -> 경기'],loc='best',fontsize=15)

plt.show()