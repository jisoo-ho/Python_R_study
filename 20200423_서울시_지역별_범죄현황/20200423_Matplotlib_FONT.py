# CCTV와 인구현황 그래프로 분석하기
import platform
import pandas as pd
import numpy as np

# 폰트 설정(특히 한글부분)
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus']=False

data_result = pd.read_csv('data_result.csv', encoding='utf-8')

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system.... sorry')
    
# CCTV 비율을 구하고 그에 따른 시각화 작업
data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100

data_result['CCTV비율'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
plt.show()

# 산점도(인구수와 소계)
plt.figure(figsize=(6,6))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()

# 인구수와 CCTV는 상관계수가 양의 값이므로 산점도와 직선
# 직선 구하기 (Polyfit을 이용한 회귀선)
# polyfit 함수를 이용해서 예측 모델 z의 계수를 생성
# z계수 : 기존 데이터들을 산점도로 시각화작업 한 경우 회귀선을 그려주는데 그려줄 때 필요한 
# 세타(기울어진 각도) 가 필요한데 그 세타값이 z 계수임
# 기울기를 조절하고 싶다면 z계수를 다시 뽑아야 한다.

fp1 = np.polyfit(data_result['인구수'], data_result['소계'],1)
fp1 # array([1.30916415e-03, 6.45066497e+02])
print(type(fp1)) # <class 'numpy.ndarray'>

# 만들어진 예측 모델을 이용한 그래프 그리기
f1 = np.poly1d(fp1) # y축 데이터
print(type(f1)) # <class 'numpy.poly1d'>

fx = np.linspace(100000, 700000, 100) # x축 데이터
print(type(fx)) # <class 'numpy.ndarray'>

plt.figure(figsize = (10, 10))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color = 'g')
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()
'''인구수가 310000 정도일 때, cctv는 1100대가 적당하다'''

# ----------------------------조금 더 설득력 있는 자료 만들기
'''
직선이 전체 데이터의 대표값 역할을 한다면
인구수가 300,000일 경우 CCTV는 1100대 정도여야 한다는 결론.

가독성 향상을 위해 오차를 계산할 수 있는 코드 작성 후,
오차가 큰 순으로 데이터를 정렬
'''

fp1 = np.polyfit(data_result['인구수'], data_result['소계'],1)

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)

data_result['오차'] = np.abs(data_result['소계']-f1(data_result['인구수']))

df_sort = data_result.sort_values(by = '오차', ascending =False)
df_sort.head()

# plot 크기 설정
plt.figure(figsize=(14, 10))

# 산점도
plt.scatter(data_result['인구수'], data_result['소계'],
            c=data_result['오차'], s = 50)

# 회귀선
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')

# 주요 10개 지역 구 이름 출력
for n in range(10):
    plt.text(df_sort['인구수'][n]*1.02, df_sort['소계'][n]*0.98,
             df_sort.index[n], fontsize=15)
    
plt.xlabel('인구수')         # x축 라벨
plt.ylabel('인구당비율')     # y축 라벨
plt.colorbar()              # 오른쪽에 색상 바
plt.grid()                  # 가이드 라인
plt.show()                  # 출력


'''데이터를 분석한다는 의미는
분석에 대한 결과가 있어야 하고,
이에 대한 결론이 나와야 한다.'''
