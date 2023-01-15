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
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data :
    print(row)  # 현재 최고기온 data는 ''로 둘러싸인 문자열 형태
f.close()

import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data :
    row[-1] = float(row[-1])  # 아직 빈 문자열값 -> 실수 변환 에러 해결 안된 상태
    print(row)
f.close()

import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data :
    if row[-1] == '' :
        row[-1] = -999  # -999를 넣어 빈 문자열이 있던 자리라고 표시
    row[-1] = float(row[-1])  
    print(row)
f.close()

# +
import csv  # csv 모듈 불러오기

max_temp = -999  # 최고 기온 값을 저장할 변수
max_date = ''    # 최고 기온이 가장 높았던 날짜를 저장할 변수

f = open('seoul.csv')
data = csv.reader(f)
header = next(data)  # 맨 윗줄을 header 변수에 저장하기
for row in data :
    if row[-1] == '' :
        row[-1] = -999  # -999를 넣어 빈 문자열이 있던 자리라고 표시
        
    row[-1] = float(row[-1])  # 문자열로 저장된 최고 기온 값을 실수로 변환
    
    if max_temp < row[-1] : # 더 높은 최고기온 값을 발견할경우 갱신
        max_date = row[0]
        max_temp = row[-1]
    
    """print(row)"""
f.close()
print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은 ',max_date,'로, ',max_temp,'도였습니다.')
# -


