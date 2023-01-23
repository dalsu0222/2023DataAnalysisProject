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

# +
import csv
f = open('subwaytime.csv')
data = csv.reader(f)

for row in data :
    print(row)

# +
import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

for row in data :
    row[4:] = map(int, row[4:])  # map 함수를 이용하여 정수로 형변환
    print(row)

# +
# 출근 시간대 사람들이 가장 많이 타고 내리는 역 찾기
# 1. 승차 기준
import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = 0
mx_station = ''
for row in data :
    row[4:] = map(int, row[4:])
    if sum(row[10:15:2]) > mx :
        mx = sum(row[10:15:2])  # 10~14인덱스가 2씩증가하면서 sum함수 인자로 추가
        mx_station = row[3] + '(' + row[1] + ')'        
print(mx_station, mx)

# 2. 하차 기준
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = 0
mx_station = ''

for row in data :
    row[4:] = map(int, row[4:])
    a = row[11:16:2]
    if sum(a) > mx :
        mx = sum(a)
        mx_station = row[3] + '(' + row[1] + ')'        
print(mx_station, mx)

# +
# 밤 11시에 사람들이 가장 많이 타고 내리는 역을 찾는 코드
import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = 0
mx_station = ''
t = int(input('몇 시의 승차인원이 가장 많은 역이 궁금하세요? : '))

for row in data :
    row[4:] = map(int, row[4:])
    a = row[2 * t - 4]  # 입력 받은 시각의 승차 인원 값 추출하기 by 규칙 -> i = 4 + (t-4)*2
    if a > mx :
        mx = a
        mx_station = row[3] + '(' + row[1] + ')'        
print(mx_station, mx)

# +
# 시간대별로 승차&하차 인원이 가장 많은 역을 찾는 코드
# 1. 승차 기준
import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = [0] * 24  # 시간대별 최대 승차 인원 저장 리스트 초기화
mx_station = [''] * 24  # 시간대별 최대 승차 인원 역 이름 저장 리스트 초기화

for row in data :
    row[4:] = map(int, row[4:])
    for j in range(24) :
        a = row[j * 2 + 4]  # 데이터 관찰으로 j(0~)와 인덱스 i와의 관계 찾기, i = 승차 시간
        if a > mx[j] :
            mx[j] = a
            mx_station[j] = row[3]+'('+str(j+4)+'시'+')'  # 역이름, 시간대 추가
print(mx_station)
print(mx)

import matplotlib.pyplot as plt  # 그래프 그리기
plt.rc('font', family ='Malgun Gothic')
#plt.figure(dpi = 300)
plt.bar(range(24), mx, color = 'r')
plt.xticks(range(24), mx_station, rotation =90)
plt.show()

#2. 하차 기준
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = [0] * 24
mx_station = [''] * 24

for row in data :
    row[4:] = map(int, row[4:])
    for j in range(24) :
        b = row[5 + j * 2]
        if b > mx[j] :
            mx[j] = b
            mx_station[j] = row[3]+'('+str(j+4)+'시'+')'
#plt.figure(dpi = 300)
plt.rc('font',family = 'Malgun Gothic')
plt.bar(range(24), mx, color = 'b')
plt.xticks(range(24), mx_station, rotation = 90)
plt.show()

# +
# 지하철 시간대별 승하차 인원 추이를 나타내는 코드

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

s_in = [0] * 24  # 승차 인원 저장 리스트 초기화
s_out = [0] * 24  #  하차 인원 저장 리스트 초기화

for row in data :
    row[4:] = map(int, row[4:])
    for i in range(24) :
        s_in[i] += row[4 + i * 2]  # 시간대별로 승차 인원 합 구하기
        s_out[i] += row[5 + i * 2]  # 시간대별로 하차 인원 합 구하기
        
import matplotlib.pyplot as plt
plt.figure(dpi = 300)
plt.rc('font', family = 'Malgun Gothic')
plt.title('지하철 시간대별 승하차 인원 추이')  # 제목 추가
plt.plot(s_in, label = '승차')  # 승차 인원을 꺾은선 그래프로 표현
plt.plot(s_out, label = '하차')  # 하차 인원을 꺾은선 그래프로 표현
plt.legend()
plt.xticks(range(24), range(4,28))
plt.show()  # 1e7 = 1*10^7
