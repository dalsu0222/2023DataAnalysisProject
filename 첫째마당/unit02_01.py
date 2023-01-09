# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import csv
f = open('seoul.csv','r',encoding='cp949')  # open의 2,3번째 속성은 기본값이므로 생략 가능
data = csv.reader(f,delimiter=',')   #deilmeter : 구분자, 기본값은 ','로 생략 가능
print(data)

for row in data :
    print(row)   # 출력결과 '108'-> 문자열 데이터임을 의미 -> 실수 형태로 변환할 필요성 있음
f.close()

import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)  # header: 각 열의 데이터 속성 설명
print(header)
f.close()

import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)  # header: 각 열의 데이터 속성 설명
for row in data :
    print(row)   
f.close()

ㅉ


