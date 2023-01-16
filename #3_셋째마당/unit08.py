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
# unit7 연장선, 지역이름받아 인구분포 출력하기
import csv
 
f = open('age.csv')
data = csv.reader(f)
result = []
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')  # 지역이름 입력받기
 
for row in data :
    if name in row[0] :                   # 입력받은 내용이 포함된 값 찾기
        for i in row[3:] :
            result.append(int(i))

import matplotlib.pyplot as plt
plt.style.use('ggplot')                   # 그래프 스타일 적용
plt.rc('font', family ='Malgun Gothic')   # 폰트를 맑은고딕으로 설정
plt.title(name +' 지역의 인구 구조')      # 제목 넣기
plt.plot(result)
plt.show()
# -

# 막대그래프 그리기 - bar() 함수
import matplotlib.pyplot as plt
plt.bar([0,1,2,4,6,10],[1,2,3,5,6,7])  # 첫번째는 막대를 표시할 위치 입력, 두번째는 막대의 높이 입력
plt.show()

import matplotlib.pyplot as plt
plt.bar(range(6),[1,2,3,5,6,7])  # 오름차순 표현
plt.show()

# +
# 우리동네(신도림) 인구 구조를 막대 그래프로 표현
import csv
f = open('age.csv')
data = csv.reader(f)

result = []
for row in data :
    if '신도림' in row[0] :
        for i in row[3:] :
            result.append(int(i))

import matplotlib.pyplot as plt
plt.bar(range(101), result)
plt.show()
plt.barh(range(101), result)  # 수평 방향으로 막대그래프 그리기, 첫째 값이 y축 둘째값이 막대의 너비
plt.show()

# +
# 항아리 모양 그래프 그리기
# 데이터 접근법 ver1 (여자 정보 뒤에서 접근)
import csv
f = open('gender.csv')
data = csv.reader(f)
m = []  # 남자 정보 저장
f = []  # 여자 정보 저장

for row in data :
    if '신도림' in row[0] :
        for i in range(0,101) :  # 나이 구간의 길이만큼 반복
            m.append(int(row[i+3]))  # 3~103 인덱스 값 저장
            f.append(int(row[-(i+1)]))  # 뒤에서부터 접근하여 값 저장
f.reverse()  # 뒤에서부터 역순으로 저장된 값을 뒤집기

# +
# 항아리 모양 그래프 그리기
# 데이터 접근법 ver2 (여자 정보 앞에서 접근)
import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []

for row in data :
    if'신도림'in row[0] :
        for i in row[3:104] :
            m.append(int(i))    # 남성 데이터를 리스트 m에 저장
        for i in row[106:] :
            f.append(int(i))    # 여성 데이터를 리스트 f에 저장
            
# 데이터 시각화(ver2 채택)
import matplotlib.pyplot as plt
plt.barh(range(101), m)
plt.barh(range(101), f)
plt.show()  # m(남자), f(여자) 데이터 둘 다 양수라서 겹쳐서 보임 -> m 데이터를 음수로 두어 겹침 현상 해결!

# +
# 항아리 모양 그래프 그리기
# ★★★접근법 ver2 이용 + 겹침 현상 해결 + 지역이름 입력받기 최종 코드★★★
import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []

name = input('찾고 싶은 지역의 이름을 알려주세요 : ')

for row in data :
    if name in row[0] :
        for i in row[3:104] :
            m.append(-int(i))    # 음수로 저장하여 데이터가 겹쳐보이는 현상 해결
        for i in row[106:] :
            f.append(int(i))  
            
# 데이터 시각화
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.title(name+' 지역의 남녀 성별 인구 분포')  # 제목 넣기
plt.rcParams['axes.unicode_minus'] = False  # matplotlib에서 마이너스기호가 깨지는 에러 해결

plt.barh(range(101), m, label='남성')  # 라벨 추가
plt.barh(range(101), f, label='여성')
plt.legend()  # 범례 표시
plt.show()
