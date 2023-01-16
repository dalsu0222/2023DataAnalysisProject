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
# 시각화 전, 신도림의 0~100세이상 인구 구조 분석
import csv
f = open('age.csv')
data = csv.reader(f)
result = []  # 빈 리스트 만들기

for row in data :
    if '신도림' in row[0] :  # '신도림'이 포함된 행정구역 찾기
        for i in row[3:] :  # 0세부터 끝(100세 이상)까지 모든 연령에 대해 반복하기
            result.append(int(i))  # 정수로 형변환하여 저장
print(result)

# +
# 시각화 후, 신도림의 0~100세이상 인구 구조 분석 및 시각화
import csv
f = open('age.csv')
data = csv.reader(f)
result = []  # 빈 리스트 만들기

for row in data :
    if '신도림' in row[0] :  # '신도림'이 포함된 행정구역 찾기
        for i in row[3:] :  # 0세부터 끝(100세 이상)까지 모든 연령에 대해 반복하기
            result.append(int(i))  # 정수로 형변환하여 저장

# 시각화 작업
import matplotlib.pyplot as plt  # matplot library import
plt.style.use('ggplot')  # 격자무늬 지정
plt.plot(result)  # 그래프 종류 선택
plt.show()
