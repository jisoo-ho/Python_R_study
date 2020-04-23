# =============================================================================
# 외국인 거주자 인구수 데이터
# =============================================================================

import matplotlib.pyplot as plt

import seaborn as sns # 다수의 상관관계 표현하기 위한 모듈
import platform       # 한글 폰트 설정하기 위한 모듈
import pandas as pd
import numpy as np

import json

import folium
import webbrowser


pop_Seoul = pd.read_excel('./data/01. population_in_Seoul.xls', encoding='utf-8')

pop_Seoul.head()

pop_Seoul = pd.read_excel('./data/01. population_in_Seoul.xls',
                          header=2, # 2줄 건너뛰고 읽어온다
                          usecols='B, D, J', # 원하는 셀만 골라서 가져오기
                          encoding='utf-8')

pop_Seoul.head() 

# 알기 쉬운 컬럼명으로 변경
pop_Seoul.rename(columns={pop_Seoul.columns[0]:'구별',
                          pop_Seoul.columns[1]:'인구수',
                          pop_Seoul.columns[2]:'외국인거주인구'}, inplace=True)
pop_Seoul.head()

pop_Seoul.drop([0], inplace=True)
pop_Seoul.head()


# '구별' 컬럼의 중복값제거
pop_Seoul['구별'].unique()

# '구별' 컬럼의 NULL 값 확인
pop_Seoul[pop_Seoul['구별'].isnull()] # NULL 값이 있는 행 번호 & 값들을 함께 반환시켜준다.

# '구별' 컬럼의 NULL값 있는 행 제거
pop_Seoul.drop([26],inplace=True)
pop_Seoul.head()

#비율 추가
pop_Seoul['외국인비율']=pop_Seoul['외국인거주인구']/pop_Seoul['인구수']*100

#각 컬럼 확인
pop_Seoul.sort_values(by='인구수', ascending=False).head()
pop_Seoul.sort_values(by='외국인거주인구', ascending=False).head()

# 시각화 작업을 위한 구 이름('구별')을 index 화
pop_Seoul.set_index('구별', inplace=True)
pop_Seoul


geo_path = './data/02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

# # 지도를 이용한 시각화 작업을 위해 지도의 중심 좌표를 이용하여 12배 확대
map = folium.Map(location = [37.5502, 126.982], zoom_start=12)

map.choropleth(geo_data=geo_str,
               data = pop_Seoul['외국인비율'],
               columns = [pop_Seoul.index, pop_Seoul['외국인비율']],
               fill_color='PuRd',
               key_on = 'feature.id')

map.save('folium_foreingn.html')
webbrowser.open_new("folium_foreingn.html")
