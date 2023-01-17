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
# unit08 코드에서 제주도 지역 찾기
import csv
f = open('gender.csv')
data = csv.reader(f)

m = []
f = []

name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
for row in data :
    if name in row[0] :
        for i in row[3:104] :
            m.append(-int(i))
        for i in row[106:] :
            f.append(int(i))
        break  # 입력받은 내용이 포함되는 데이터 중 처음 만나는 데이터만 m,f에 넣기

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(name+' 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()
# -

# pie() 함수 예제
import matplotlib.pyplot as plt
plt.pie([10, 20])
plt.show()

# 동그란 원 그리기
import matplotlib.pyplot as plt
size = [2441, 2312, 1031, 1233]
plt.axis('equal')
plt.pie(size)
plt.show()

# 레이블 추가하기
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')    # 그래프에 한글 표시
size = [2441, 2312, 1031, 1233]           # 데이터
label = ['A형','B형','AB형', 'O형']       # 레이블
plt.axis('equal')
plt.pie(size, labels=label)  # 라벨 달기
plt.show()  # 반시계 방향으로 나타남, 시작지점 3시방향

# 비율 및 범례 표시하기
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
size = [2441, 2312, 1031, 1233]
label = ['A형','B형','AB형', 'O형']
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%')  # 비율 표시(실수 형태)
plt.legend()  # 범례 표시
plt.show()

# 색 및 돌출 효과 정하기
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
size = [2441, 2312, 1031, 1233]
label = ['A형','B형','AB형', 'O형']
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']  # color 리스트로 다양한 값 설정
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%', colors=color, explode=(0,0,0.1,0))  # explode 속성으로 돌출정도 지정(0=돌출되지않음)
plt.legend()
plt.show()

# +
# 원하는 지역의 성별 인구 비율을 파이 차트로 그리기
import csv
 
f = open('gender.csv')
data = csv.reader(f)             # 데이터 불러오기

size = []                        # 남녀 인구수를 저장할 빈 리스트 만들기

name = input('찾고 싶은 지역의 이름을 알려주세요 : ') # 지역 이름 입력받기
for row in data :
    if name in row[0] :          # name과 일치하는 지역 찾기
        m = 0                    # 남성 인구수를 누적해서 더할 변수 초기화하기
        f = 0                    # 여성 인구수를 누적해서 더할 변수 초기화하기
        for i in range(101) :
            m += int(row[i+3])   # 남성 인구수를 누적해서 더하기(3~103번 데이터)
            f += int(row[i+106]) # 여성 인구수를 누적해서 더하기(106~206번 데이터)
        break
size.append(m)                   # 남성 인구수를 size 리스트에 더하기
size.append(f)                   # 여성 인구수를 size 리스트에 더하기

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
color = ['crimson', 'darkcyan']  # 색상 설정하기
plt.axis('equal')
 
plt.pie(size, labels=['남', '여'], autopct='%.1f%%', colors=color, startangle=90) # startangle->시계방향 3시기준 반시계방향만큼 간 곳에서 시작
plt.title(name+' 지역의 남녀 성별 비율')  # 제목 설정하기
plt.show()
