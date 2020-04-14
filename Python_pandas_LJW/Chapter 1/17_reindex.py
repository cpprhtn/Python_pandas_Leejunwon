#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}


df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df)
print()


new_index = ['r0','r1','r2','r3','r4']
ndf = df.reindex(new_index)
print(ndf)
print()


new_index = ['r0','r1','r2','r3','r4']
ndf2 = df.reindex(new_index,fill_value=0) #null값 대신 0을 채움
print(ndf2)