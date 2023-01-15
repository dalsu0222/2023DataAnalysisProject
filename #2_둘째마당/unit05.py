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
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)

high = []  # 최고 기온 값을 저장한 리스트 high 생성
low = []  # 최저 기온 값을 저장할 리스트 low 생성

for row in data :
    if row[-1] != '' and row[-2] != '' :  # 최고 기온 값과 최저 기온 값이 존재한다면
        date = row[0].split('-')  # 날짜 값을 - 문자를 기준으로 구분하여 저장
        if 2001 <= int(date[0]) :  # 2001년 이후 데이터라면
            if date[1] == '02' and date[2] == '22' :  # 2월 22일 이라면
                high.append(float(row[-1]))  # 최고 기온 값을 high 리스트에 저장
                low.append(float(row[-2]))   # 최저 기온 값을 low 리스트에 저장
                
plt.rc('font', family='Malgun Gothic')  # 맑은 고딕을 기본 글꼴로 설정
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지
plt.title('내 생일의 기온 변화 그래프')
# high 리스트에 저장된 값을 hotpink색으로 그리고 레이블을 표시
plt.plot(high,'hotpink',label='high')
# low 리스트에 저장된 값을 skyblue색으로 그리고 레이블을 표시
plt.plot(low,'skyblue',label='low')
plt.legend()  # 범례 표시
plt.show()  # 그림 나타내기
# -


