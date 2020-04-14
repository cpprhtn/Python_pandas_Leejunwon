#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


df = pd.DataFrame([[15,'남','부곡중'],[19,'여','사대부고']],
                  index=["준원","윤영"],
                  columns = ["나이","성별","학교"])


print(df)
print("\n")


df.rename(columns={'나이' : 'age','성별' : 'sex','학교' : 'group'}, inplace=True)


df.rename(index={'준원' : 'std1','윤영' : 'std2'}, inplace=True) 
#True는 원본 데이터를 수정, False는 새로운 데이터로 생성



print(df)
