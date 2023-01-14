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
#그림 4-2
import matplotlib.pyplot as plt

plt.plot([10,20,30,40])  # 한개의 리스트 입력 -> y축으로 작동
plt.show

# +
#그림 4-3
import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[12,43,25,15])  # 두 개의 리스트 입력 -> x축,y축 순
plt.show

# +
#그림 4-4
import matplotlib.pyplot as plt

plt.title('plotting')  # 제목 넣기(영어로)
plt.plot([10,20,30,40])  # 두 개의 리스트 입력 -> x축,y축 순
plt.show

# +
#그림 4-5
import matplotlib.pyplot as plt

plt.title('legend')
plt.plot([10,20,30,40], label='asc')  # 증가를 의미하는 asc 범례
plt.plot([40,30,20,10], label='desc')  # 감소를 의미하는 desc 범례
plt.legend()  # 그래프에 범례 표시, loc=0~10으로 위치지정 가능
plt.show

# +
#그림 4-6
import matplotlib.pyplot as plt

plt.title('color')
plt.plot([10,20,30,40], color='skyblue', label='skyblue')  # 그래프 색상 지정 가능
plt.plot([40,30,20,10], 'pink', label='pink')  # color 속성 생략 가능
plt.legend()  # 그래프에 범례 표시
plt.show

# +
#그림 4-7
import matplotlib.pyplot as plt

plt.title('linestyle')
#빨간색 dashed 그래프
plt.plot([10,20,30,40], color='r', linestyle='--', label='dashed')  # plt.plot([1,2,3,4],'r--')로 색상과 선모양 동시 작성 가능
# 초록색 dotted 그래프
plt.plot([40,30,20,10], color='g', ls=':', label='dotted')
plt.legend()  # 그래프에 범례 표시
plt.show

# +
#그림 4-8
import matplotlib.pyplot as plt

plt.title('marker')
#빨간색 원형 마커 그래프
plt.plot([10,20,30,40], 'r.', label='circle')   # r.-- 과 같이 색상-마커모양-선모양 순으로 동시작성 가능
#초록색 삼각형 마커 그래프
plt.plot([40,30,20,10], 'g^', label='triangle up') 
plt.legend()  # 그래프에 범례 표시
plt.show
# -


