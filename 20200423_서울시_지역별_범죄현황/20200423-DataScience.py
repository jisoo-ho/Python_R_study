'''
서울시 구별 CCTV 현황 분석하기

서울시 각 구별 CCTV 수를 파악하고,
인구대비 CCTV 비율을 파악해서 순위 비교

인구대비 CCTV의 평균치를 확인하고
그로부터 CCTV가 과하게 부족한 구를 확인

Python 기본 문법 / Pandas 와 Matplotlib의 기본적 사용법을 이용한 시각화
단순한 그래프 표현에서
한 단계 더 나아가 경향을 확인하고 시각화하는 기초 확인
 
'''

import pandas as pd
import numpy as np

# CCTV 데이터와 인구 데이터 합치고 분석하기
CCTV_Seoul = pd.read_csv('./data/01. CCTV_in_Seoul.csv', encoding='utf-8')
print(type(CCTV_Seoul)) # <class 'pandas.core.frame.DataFrame'>

CCTV_Seoul.head()

CCTV_Seoul.columns # dtype='object' : dtype 은 실제 데이터의 타입
print(type(CCTV_Seoul.columns)) # <class 'pandas.core.indexes.base.Index'>
'''.columns 가 반환하는 타입은 원래 LIST 타입이다.'''
'''시리즈는 index 구역과 value 구역으로 나뉘어 있다.'''

CCTV_Seoul.columns[0] # 여기서 시리즈의 인덱스번호로 찾아준 것임. CCTV_Seoul.columns 의 데이터 타입이 object 인 이유
print(type(CCTV_Seoul.columns[0])) # <class 'str'>

# 컬럼명 변경 : 기관명을 구별로 변경
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True) # 0번의 컬럼명을 구별로 변경, 그 결과값을 다시 CCTV_Seoul.columns[0]에 반영
CCTV_Seoul.head()


# 인구 데이터 읽기 1
pop_Seoul = pd.read_excel('./data/01. population_in_Seoul.xls', encoding='utf-8')
pop_Seoul.head()

# 인구 데이터 읽기 2 - 필요한 데이터만 선별하여 읽기
pop_Seoul = pd.read_excel('./data/01. population_in_Seoul.xls',
                          header=2, # 2줄 건너뛰고 읽어온다
                          usecols='B, D, G, J, N', # 원하는 셀만 골라서 가져오기
                          encoding='utf-8')

pop_Seoul.head() # 컬럼명이 동일하기 때문에 .1, .2 가 붙어서 출력된다.

# 알기 쉬운 컬럼명으로 변경
pop_Seoul.rename(columns={pop_Seoul.columns[0]:'구별',
                          pop_Seoul.columns[1]:'인구수',
                          pop_Seoul.columns[2]:'한국인',
                          pop_Seoul.columns[3]:'외국인',
                          pop_Seoul.columns[4]:'고령자'}, inplace=True)
pop_Seoul.head()

# CCTV 데이터 파악하기
CCTV_Seoul.sort_values(by='소계', ascending=True).head()

CCTV_Seoul.sort_values(by='소계', ascending=False).head()

# 최근증가율 = (2016년+2015년+2014년)/2013년도 이전 * 100
CCTV_Seoul['최근증가율']=(CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + \
                     CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전'] * 100
    
    
CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head() # 종로구가 가장 크다.

# 서울시 인구 데이터 파악하기
pop_Seoul.head()

# 첫 번째 합계 행 삭제
pop_Seoul.drop([0], inplace=True)
pop_Seoul.head()

# '구별' 컬럼의 중복값제거
pop_Seoul['구별'].unique()

# '구별' 컬럼의 NULL 값 확인
pop_Seoul[pop_Seoul['구별'].isnull()] # NULL 값이 있는 행 번호 & 값들을 함께 반환시켜준다.

# '구별' 컬럼의 NULL값 있는 행 제거
pop_Seoul.drop([26],inplace=True)
pop_Seoul.head()

'''
데이터분석
1. 분석 데이터 수집
 - 수집하는 방법
 1) 어느 사이트의 데이터를 이용하는 방법
 2) 기사 & 문서를 이용하는 방법
 3) SNS를 이용하는 방법 - API를 이용하면 가능하다.
    --> data 폴더 생성
    
2. 수집된 데이터 형식 확인 및 local 전처리
 - 프로그램에서 검사하는게 아닌 PC에서 검사해야 한다.(1차 전처리)
 (excel or csv 파일등은 일단 열어보고 다 필요한지 어디에 있는지, 한글이 깨졌는지를 모두 확인해야 한다.)
    --> 1차 전처리 된 폴더 생성
    
3. 분석 prg에서 수집 데이터 읽기
 - R로 할 것인지, Python 으로 할 것인지
    --> 1차에서 하기 힘든것들은 프로그램을 통해서 전처리 진행
    
4. 읽은 데이터 확인 및 2차 전처리 
'''

# 외국인 비율과 고령자 비율 추가
pop_Seoul['외국인비율']=pop_Seoul['외국인']/pop_Seoul['인구수']*100
pop_Seoul['고령자비율']=pop_Seoul['고령자']/pop_Seoul['인구수']*100
pop_Seoul.head()

#각 컬럼 확인
pop_Seoul.sort_values(by='인구수', ascending=False).head()
pop_Seoul.sort_values(by='외국인', ascending=False).head()
pop_Seoul.sort_values(by='외국인비율', ascending=False).head()
pop_Seoul.sort_values(by='고령자', ascending=False).head()
pop_Seoul.sort_values(by='고령자비율', ascending=False).head()

#### CCTV 데이터와 인구 데이터 합치고 분석하기

# 두 개의 데이터프레임을 합할 경우 동일 컬럼명은 하나('구별')로 통일된다.
data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')
data_result.head()
type(data_result) # pandas.core.frame.DataFrame

# CCTV에 대한 '소계' 컬럼을 제외한 나머지 CCTV 데이터 삭제
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
data_result.head()

# 시각화 작업을 위한 구 이름('구별')을 index 화
data_result.set_index('구별', inplace=True)
data_result.head()

# CCTV와 각 컬럼에 대한 상관관계 분석
# 상관관계 함수 : np.corrcoef()
np.corrcoef(data_result['고령자비율'], data_result['소계'])
'''array([[ 1.        , -0.28078554],
       [-0.28078554,  1.        ]])'''
    
np.corrcoef(data_result['외국인비율'], data_result['소계'])
'''array([[ 1.        , -0.13607433],
       [-0.13607433,  1.        ]])'''
    
np.corrcoef(data_result['인구수'], data_result['소계'])
'''array([[1.        , 0.30634228],
       [0.30634228, 1.        ]])'''

data_result.sort_values(by='소계', ascending=False).head(5)

# 데이터 저장
data_result.to_csv('data_result.csv')

# 데이터 읽히는지 확인하기
pd.read_csv('data_result.csv', encoding='utf-8')
