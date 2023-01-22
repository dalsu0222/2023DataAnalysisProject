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
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
 
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    print(row)

# +
# 유임 승차 비율이 가장 높은 역 찾기

import csv
 
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
 
mx = 0
rate = 0
mx_station = ''  # 역 이름과 몇 호선인지를 저장하는 변수
 
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] != 0 and (row[4]+row[6]) > 100000 :  # 비율 = 유임승차인원/전체(유임+무임)인원, 총 승차인원 100,000명 초과만
        rate = row[4] / (row[4]+row[6])
        if rate > mx :
            mx = rate
            mx_station = row[3] + ' ' + row[1]
            
print(mx_station, round(mx*100,2))

# +
# 유무임 승하차 인원이 가장 많은 역 찾기

import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

mx = [0] * 4  # [0,0,0,0], 각 라벨별 최댓값을 저장하는 변수
mx_station = [''] * 4  # [,,,]
label = ['유임승차','유임하차','무임승차','무임하차']

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
        if row[i] > mx[i-4] :  # 해당 역이 지금까지 저장된 최댓값보다 클 경우 값 갱신
            mx[i-4] = row[i]
            mx_station[i-4] = row[3] +' '+ row[1]
            
for i in range(4) :
    print(label[i]+' : '+mx_station[i], mx[i])

# +
# 모든 역의 유무임 승하차 비율을 파이 차트로 나타내기

import csv
import matplotlib.pyplot as plt
 
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

label = ['유임승차','유임하차','무임승차','무임하차']
c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']  # 걸러 지정
plt.rc('font', family='Malgun Gothic')
 
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    plt.figure(dpi=300)
    plt.title(row[3]+' '+row[1])
    plt.pie(row[4:8], labels=label, colors=c, autopct='%1.f%%')  # 파이 차트로 유무임 승하차 비율 나타내기, 비율을 수치로 표현
    plt.axis('equal')
    plt.savefig(row[3]+' '+row[1]+'.png')  # 역별 파이 차트를 이미지(.png)로 저장하기
    plt.show()
