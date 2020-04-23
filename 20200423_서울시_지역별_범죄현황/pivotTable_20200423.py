####### 범죄데이터 구별로 정리하기
import pandas as pd
import numpy as np

from GangnamSafety_20200423 import station_lng, station_lat
crime_anal_raw = pd.read_csv('./data/02_crime_in_Seoul_include_gu_name.csv', encoding='utf-8')

crime_anal_raw.head()
### pandas의 pivot_table

'''
pd.pivot_table(df,                피벗 테이블을 만들기 위한 기본 데이터
               index = [],        pivot_table의 index를 설정(multi index도 가능)
               columns = [],      원하는 columns을 설정
               values = [],       columns에 해당하는 값
               aggfunc = [],      분석을 위한 파라미터
                                  예) np.sum, np.mean 사용
               fill_value = 0,    Nan 값을 채우기.
               margins = True)    모든 데이터의 결과를 아래에 붙일 것인지 설정

--> 원하는 컬럼을 인덱스화 시켜서 나머지 데이터들을 재정렬시켜주는 것이 피벗 테이블의 역할이다.
 : 데이터의 열 중에서 두 개의 열을 각각 행 인덱스, 열 인덱스로 사용하여
   데이터를 조회하여 펼쳐놓은 테이블 형태
   
※(주의)피벗테이블의 pd.pivot_table은 판다스의 함수이고 dataframe의 set index는 다른 종류이다.
'''

# pivot_table을 이용
# 저장한 데이터를 관서별에서 구별로..
crime_anal = pd.pivot_table(crime_anal_raw, index='구별', aggfunc=np.sum)
crime_anal.head()

print(crime_anal)
print(type(crime_anal)) # <class 'pandas.core.frame.DataFrame'>


'''
각 범죄별 검거율을 계산하고,
검거 건수는 검거율로 대체한 후, 검거 건수는 삭제
'''

crime_anal['강간검거율'] = crime_anal['강간 검거']/crime_anal['강간 발생']*100
crime_anal['강도검거율'] = crime_anal['강도 검거']/crime_anal['강도 발생']*100
crime_anal['살인검거율'] = crime_anal['살인 검거']/crime_anal['살인 발생']*100
crime_anal['절도검거율'] = crime_anal['절도 검거']/crime_anal['절도 발생']*100
crime_anal['폭력검거율'] = crime_anal['폭력 검거']/crime_anal['폭력 발생']*100


del crime_anal['강간 검거']
del crime_anal['강도 검거']
del crime_anal['살인 검거']
del crime_anal['절도 검거']
del crime_anal['폭력 검거']

print(crime_anal.head())

'''
100이 넘는 숫자들은 100으로 처리
'''

con_list = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

for column in con_list:
    crime_anal.loc[crime_anal[column]>100, column] =100
    
print(crime_anal.head())

# 컬럼 뒤에 발생이라는 단어 삭제 : rename()을 이용
crime_anal.rename(columns = {'강간 발생':'강간',
                             '강도 발생':'강도',
                             '살인 발생':'살인',
                             '절도 발생':'절도',
                             '폭력 발생':'폭력',}, inplace = True)

print(crime_anal.head())


################
# 데이터 표현을 위해 전처리 
'''
강도와 살인은 두 자리수,
절도와 폭력은 네 자리수로 구성 되어 있어
각각을 비슷한 범위에 놓고 비교하는 것이 편리하기 때문에
각 컬럼별로 정규화(normalize) 작업

각 항목의 최대값을 1로 두면,
추후 범죄발생 건수를 종합적으로 비교할 때 편리

각각, 강도, 살인, 절도, 폭력에 대하여
각 컬럼별로 정규화(normalize)

파이썬의 머신러닝에 관한 모듈 중
scikit learn에 있는 전처리(preprocessing) 도구에는
최소, 최대값을 이용하여 정규화시키는 함수가 존재 : MinMaxScaler()
'''

from sklearn import preprocessing

col =['강간', '강도', '살인', '절도', '폭력']

x = crime_anal[col].values
print(type(x)) # <class 'numpy.ndarray'>

min_max_scaler = preprocessing.MinMaxScaler()
print(type(min_max_scaler)) # <class 'sklearn.preprocessing._data.MinMaxScaler'>

x_scaled = min_max_scaler.fit_transform(x.astype(float))
print(type(x_scaled)) # <class 'numpy.ndarray'>

crime_anal_norm = pd.DataFrame(x_scaled, columns = col, index = crime_anal.index)
print(type(crime_anal_norm)) # <class 'pandas.core.frame.DataFrame'>


# 정규화된 데이터프레임에 검거율 추가
col2 = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

crime_anal_norm[col2] = crime_anal[col2]

print(crime_anal_norm.head())

# =============================================================================
# 사건, cctv, 인구
# 세 가지의 상관관계를 분석한다.
# =============================================================================

# CCTV_result.csv 에서 구별 인구수와 CCTV 개수만 추가
result_CCTV = pd.read_csv('./data/01. CCTV_result.csv', encoding='UTF-8', index_col = '구별')

crime_anal_norm[['인구수', 'CCTV']] = result_CCTV[['인구수', '소계']]

print("인구수와 CCTV 개수 =>", crime_anal_norm.head())

# 발생 건수의 합을 '범죄'라는 컬럼으로 합하여 추가

col = ['강간', '강도', '살인', '절도', '폭력']

crime_anal_norm['범죄'] = np.sum(crime_anal_norm[col], axis=1)

print("범죄라는 컬럼으로 합 =>", crime_anal_norm.head())

# 검거율도 통합하여 추가

col = ['강간검거율','강도검거율', '살인검거율','절도검거율','폭력검거율']

crime_anal_norm['검거'] = np.sum(crime_anal_norm[col], axis=1)

print("검거율도 통합 =>", crime_anal_norm.head())

