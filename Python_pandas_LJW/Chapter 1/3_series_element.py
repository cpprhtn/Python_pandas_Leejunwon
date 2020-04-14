#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


tup_data = ("준원","2002-05-13","남",True)
sr = pd.Series(tup_data,index = ["이름","생년월일","성별","학생여부"])
print(sr)


#원소를 1개 선택
print(sr[0])
print(sr['이름'])


#여러개의 원소선택(인덱스 리스트 사용)
print(sr[[1,2]])
print("\n")
print(sr[['생년월일','성별']])


#여러개의 원소선택(인덱스 범위지정)
print(sr[1 : 2])
#정수형 위치 인덱스 사용시 범위의 끝(2)이 포함되지 않는
print("\n")
print(sr['생년월일':'학생여부'])
