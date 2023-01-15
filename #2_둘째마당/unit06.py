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

# hist 함수
import matplotlib.pyplot as plt
plt.hist([1,1,2,3,4,5,6,6,7,8,10])
plt.show()

# 주사위 시뮬레이션
import random
print(random.randint(1,6))  # 1이상 6이하 정수중 랜덤으로 1개 추출

# +
# 주사위 시뮬레이션 ver 2
import random
import matplotlib.pyplot as plt

dice = []
for i in range(10000) :  # 주사위 10000번 굴리기
    dice.append(random.randint(1,6))
print(dice)

plt.hist(dice, bins=6)  # bins 속성:가로축의 구간 개수를 설정
plt.show  # 히스토그램 결과 반복 실행 횟수가 통계적 확률(1/6)에 수렴

# +
# 기온데이터를 히스토그램으로 표현하기 - 모든 최고 기온 데이터 추출
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        result.append(float(row[-1]))
        
plt.hist(result, bins=100, color='r')  # 히스토그램으로 나타내기
plt.show()

# +
# 기온데이터를 히스토그램으로 표현하기 - 8월 최고 기온 데이터 추출
import csv
import matplotlib.pyplot as plt
 
f = open('seoul.csv')
data = csv.reader(f)
next(data)
aug = []                          # 8월의 최고 기온 값을 저장할 aug 리스트 생성

for row in data :
    if row[-1] != '' :  # 값이 존재하는지 먼저 확인해야 EOF 에러 발생 X
        month = row[0].split('-')[1]  # -로 구분된 값 중 2번째 값을 month에 저장
        if month == '08':               # 8월달이라면
            aug.append(float(row[-1]))  # aug 리스트에 최고 기온 값 추가

plt.hist(aug, bins=100, color='r')
plt.show()

# +
#1월과 8월의 데이터를 히스토그램으로 시각화하기
import csv
import matplotlib.pyplot as plt
 
f = open('seoul.csv')
data = csv.reader(f)
next(data)
 
aug = []                          # 8월의 최고 기온 값을 저장할 aug 리스트 생성
jan = []                          # 1월의 최고 기온 값을 저장할 jan 리스트 생성

for row in data :
    if row[-1] != '' :
        month = row[0].split('-')[1]  # -로 구분된 값 중 2번째 값을 month에 저장
        if month == '08':               # 8월달이라면
            aug.append(float(row[-1]))  # aug 리스트에 최고 기온 값 추가
        if month == '01':               # 1월달이라면
            jan.append(float(row[-1]))  # jan 리스트에 최고 기온 값 추가

plt.hist(aug, bins=100, color ='r', label='Aug')
plt.hist(jan, bins=100, color ='b', label='Jan')
plt.legend()
plt.show()

# +
#기온 데이터를 상자 그림으로 표현하기
import matplotlib.pyplot as plt
import random

result = []
for i in range(13) :
    result.append(random.randint(1, 1000))
print(sorted(result))

plt.boxplot(result)  # 위에서부넡 최대값, 3/4값, 중앙값, 1/4값, 최솟값 표시
plt.show()

#1/4, 2/4, 3/4에 위치한 정확한 값 출력
import numpy as np

result = np.array(result)
print("1/4: "+str(np.percentile(result,25)))
print("2/4: "+str(np.percentile(result,50)))
print("3/4: "+str(np.percentile(result,75)))

# +
#서울의 최고 기온 데이터를 상자 그림으로 그리기
import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        result.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.boxplot(result)       # 상자 그림으로 나타내기 
plt.show()

# +
#1월과 8월의 데이터를 상자 그림으로 시각화하기
import csv
import matplotlib.pyplot as plt
 
f = open('seoul.csv')
data = csv.reader(f)
next(data)
 
aug = []                          # 8월의 최고 기온 값을 저장할 aug 리스트 생성
jan = []                          # 1월의 최고 기온 값을 저장할 jan 리스트 생성

for row in data :
    if row[-1] != '' :
        month = row[0].split('-')[1]  # -로 구분된 값 중 2번째 값을 month에 저장
        if month == '08':               # 8월달이라면
            aug.append(float(row[-1]))  # aug 리스트에 최고 기온 값 추가
        if month == '01':               # 1월달이라면
            jan.append(float(row[-1]))  # jan 리스트에 최고 기온 값 추가

import matplotlib.pyplot as plt
plt.boxplot(aug)       # 상자 그림으로 나타내기 
plt.boxplot(jan)       # 그림에서 빈 동그라미의 의미 -> 이상치(outlier)값 표현
plt.show()

# +
#최고 기온 데이터를 월별로 분류하고 상자 그림으로 그리기
import matplotlib.pyplot as plt
import csv
 
f = open('seoul.csv')
data = csv.reader(f)
next(data)
 
# 월별 데이터를 저장할 리스트 month 생성(12개)
month = [[],[],[],[],[],[],[],[],[],[],[],[]]
 
for row in data :
    if row[-1] != '' :
        # 월과 같은 번호의 인덱스에 월별 데이터 저장(예:1월→month[0] )
        month[int(row[0].split('-')[1])-1].append(float(row[-1]))

plt.boxplot(month)
plt.show()

# +
import matplotlib.pyplot as plt
import csv
 
f = open('seoul.csv')
data = csv.reader(f)
next(data)

day = []                # 일별 데이터를 저장할 리스트 day 생성
for i in range(31) :
    day.append([])      # day 리스트 내 31개 리스트 생성

for row in data :
    if row[-1] != '' :
        if row[0].split('-')[1] == '08':   # 8월이라면
           # 최고 기온 값 저장
           day[int(row[0].split('-')[2])-1].append(float(row[-1]))

plt.style.use('ggplot')   # 그래프 스타일 지정(ggplot->배경이 회색 격자 무늬, 중앙값 선 색 변경)
plt.figure(figsize=(10,5), dpi=300)  # 그래프 크기 수정(가로 10 세로 5)
plt.boxplot(day, showfliers=False)   # 아웃라이어(이상치) 값 생략
 
plt.show()
