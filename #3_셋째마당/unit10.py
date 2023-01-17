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
# 제주도 연령대별 성별 비율 -> 꺾은선 그래프로 표현하기
import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []

name = input('궁금한 동네를 입력해주세요:')
for row in data :
    if name in row[0] :
        for i in range(3,104) :
            m.append(int(row[i]))      # 남성 데이터 저장하기
            f.append(int(row[i+103]))  # 여성 데이터 저장하기    
        break
        
import matplotlib.pyplot as plt
plt.plot(m, label='Male')  # 꺾은선 그래프
plt.plot(f, label='Female')
plt.legend()
plt.show()

# +
# 제주도 연령대별 성별 비율 -> 막대 그래프로 표현하기
import csv
f = open('gender.csv')
data = csv.reader(f)
result = []

name = input('궁금한 동네를 입력해주세요:')
for row in data :
    if name in row[0] :
        for i in range(3,104) :
            result.append(int(row[i]) - int(row[i+103]))  # 차이에 주목하기
        break
        
import matplotlib.pyplot as plt
plt.bar(range(101), result)  # 막대그래프로 출력
plt.show()
# -

# 산점도 -> scatter() 함수로 표현하기
import matplotlib.pyplot as plt
plt.scatter([1,2,3,4], [10,30,20,40])
plt.style.use('ggplot')  # 격자무늬스타일 지정
plt.show()

# scatter() 이용하여 버블차트 그리기
import matplotlib.pyplot as plt
plt.scatter([1,2,3,4], [10,30,20,40], s=[30,60,90,120], c=range(4) , cmap='jet') 
# ↑c로 색상  지정, cmap으로 사용될 색상 종류 결정
plt.style.use('ggplot')  # 격자무늬스타일 지정
plt.colorbar()  # 그래프 옆에 컬러바 추가
plt.show()

# +
# 서로 다른 100개의 점으로 산점도 파악하기
import matplotlib.pyplot as plt
import random
x = []
y = []
size = []  # 크기에 따라 다른 색으로 표현하기 위한 size 리스트 생성
for i in range(100) :
    x.append(random.randint(50,100))
    y.append(random.randint(50,100))
    size.append(random.randint(10,100))
    
plt.scatter(x, y, s=size, c=size, cmap='jet', alpha=0.7) 
# ↑c에서 range()쓰면 순서대로 색 부여, alpha속성으로 투명도 조절(0~1, 0에 가까울수록 투명)
plt.colorbar()
plt.show()

# +
# 제주도의 연령대별 성별 비율을 산점도로 표현하기
import csv
import math
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
size = []

name = input('궁금한 동네를 입력해주세요 : ')
for row in data :
    if name in row[0] :
        for i in range(3,104) :
            m.append(int(row[i]))
            f.append(int(row[i+103]))
            size.append(math.sqrt(int(row[i])+int(row[i+103])))  # 제곱근으로 남녀총인구수 점의 크기 조절
        break

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.figure(figsize=(10,5), dpi=300)
plt.title(name+' 지역의 성별 인구 그래프')
plt.scatter(m, f, s=size, c=range(101), alpha=0.5, cmap='jet')
plt.colorbar()
plt.plot(range(max(m)),range(max(m)), 'g')  # y=x 형태의 추세선 그리기
plt.xlabel('남성 인구수')  # x축 이름 달기
plt.ylabel('여성 인구수')  # y축 이름 달기
plt.show()
