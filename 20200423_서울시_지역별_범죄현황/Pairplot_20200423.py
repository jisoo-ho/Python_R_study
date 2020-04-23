import matplotlib.pyplot as plt

import seaborn as sns # 다수의 상관관계 표현하기 위한 모듈
import platform       # 한글 폰트 설정하기 위한 모듈
import pandas as pd
import numpy as np
from pivotTable_20200423 import crime_anal_norm, crime_anal_raw
from GangnamSafety_20200423 import station_lng, station_lat


# 한글 폰트 설정
path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system.... sorry')
    
# pairplot() 상관관계 : '강도', '살인', '폭력'

#'''
sns.pairplot(crime_anal_norm, vars=["강도", "살인", "폭력"], kind = 'reg', size=3)
plt.show()
#'''
'''
강도와 폭력, 살인과 폭력, 강도와 살인 모두 양의 상관관계를 보임.
'''

# pairplot() 상관관계 : "인구수", "CCTV", "살인", "강도"
# '''
sns.pairplot(crime_anal_norm, x_vars=["인구수", "CCTV"], y_vars =["살인","강도"], kind='reg', size=3)
plt.show()
# '''

'''
전체적인 상관계수는 CCTV와 살인의 관계가 낮을지 몰라도
CCTV가 없을 때 살인사건 많은 구간 있음.
즉, CCTV수를 기준으로 좌측면에 살인과 강도의 높은 수를 갖는 데이터가 보임.
'''

# pairplot() 상관관계 : "인구수", "CCTV", "살인검거율", "폭력검거율"
sns.pairplot(crime_anal_norm, x_vars=["인구수", "CCTV"], y_vars=["살인검거율", "폭력검거율"], kind='reg', size=3) 
# kind='reg'를 작성해야 관계선이 그려진다
plt.show()
'''
살인 및 폭력 검거율과 CCTV의 관계가 음의 상관계수도 보여줌.
인구수와 살인 및 폭력 검거율도 음의 상관관계를 보임.
'''
# pairplot() 상관관계 : "인구수", "CCTV", "절도검거율", "강도검거율"
sns.pairplot(crime_anal_norm, x_vars=["인구수", "CCTV"], y_vars=["절도검거율","강도검거율"],kind = 'reg', size=3)
plt.show()


# 검거율의 합계인 검거 항목 최고 값을 100으로 한정한 후, 그 값으로 정렬
tmp_max = crime_anal_norm['검거'].max()
crime_anal_norm['검거'] = crime_anal_norm['검거'] / tmp_max *100
crime_anal_norm_sort = crime_anal_norm.sort_values(by='검거', ascending=False)
crime_anal_norm_sort.head()


# heatmap 으로 시각화
target_col = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']

crime_anal_norm_sort = crime_anal_norm.sort_values(by = '검거', ascending=False)

plt.figure(figsize=(10,10))

sns.heatmap(crime_anal_norm_sort[target_col],
            annot=True, fmt='f',
            linewidths=.5,     #linewidth는 칸 간격 의미.
            cmap = 'RdPu')

plt.title('범죄 검거 비율 (정규화된 검거의 합으로 정렬)')
plt.show()
'''
검거율이 절도가 가장 낮아서 잡기가 힘들다.
검거율이 보톤 좋은 지역들은 도봉구, 광진구, 강서구 등이 검거율이 좋다고 확인된다.
'''

# 발생 건수 정렬하여 heatmap으로 시각화
target_col = ['강간', '강도', '살인' ,'절도', '폭력', '범죄']

crime_anal_norm['범죄'] = crime_anal_norm['범죄'] / 5

crime_anal_norm_sort = crime_anal_norm.sort_values(by ='범죄', ascending=False)
plt.figure(figsize=(10,10))
sns.heatmap(crime_anal_norm_sort[target_col],
            annot=True, fmt='f',
            linewidths=.5,
            cmap='RdPu')

plt.title("범죄비율 (정규화 된 발생 건수로 정렬)")
plt.show()

# 작업물 저장
crime_anal_norm.to_csv('./data/02_crime_in_Seoul_final.csv', sep=',', encoding='utf-8') # 인코딩의 표준이 utf-8이기 때문에 이렇게 저장

# 읽기 내용 확인
pd.read_csv('./data/02_crime_in_Seoul_final.csv', encoding='utf-8') 

import json

geo_path = './data/02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

crime_anal_raw['lat'] = station_lat
crime_anal_raw['lng'] = station_lng

col = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']
tmp = crime_anal_raw[col] / crime_anal_raw[col].max()

crime_anal_raw['검거'] = np.sum(tmp, axis=1)

crime_anal_raw.head()



import folium
import webbrowser

############
# 지도를 이용한 시각화 작업을 위해 지도의 중심 좌표를 이용하여 12배 확대
map = folium.Map(location = [37.5502, 126.982], zoom_start=12)

# 로드된 지도 위에 각 경찰서 위치를 marking
for n in crime_anal_raw.index:
    folium.Marker([crime_anal_raw['lat'][n], crime_anal_raw['lng'][n]]).add_to(map)
    
map
map.save('folium_kr.html')
webbrowser.open_new("folium_kr.html")


################
# 지도를 이용한 시각화 작업을 위해 지도의 중심 좌표를 이용하여 12배 확대
map = folium.Map(location = [37.5502, 126.982], zoom_start=12)

# 로드된 지도 위에 각 경찰서의 검거율을 x10 배수의 크기(반지름)로 원을 그려준다.(외경 선과 내면 색 지정)
# .add_to()함수로 불러온 map 에 더해줌
for n in crime_anal_raw.index:
    folium.CircleMarker([crime_anal_raw['lat'][n], crime_anal_raw['lng'][n]],
                        radius = crime_anal_raw['검거'][n]*10,
                        color = '#3186cc',
                        fill_color = '#3186cc',
                        fill=True).add_to(map)

# map html파일로 저장 후 열기
map
map.save('folium_kr2.html')
webbrowser.open_new("folium_kr2.html")


##############
map = folium.Map(location = [37.5502, 126.982], zoom_start=12)

map.choropleth(geo_data=geo_str,
               data = crime_anal_norm['범죄'],
               columns = [crime_anal_norm.index, crime_anal_norm['범죄']],
               fill_color='PuRd',   #PuRd, YlGnBu
               key_on = 'feature.id')

for n in crime_anal_raw.index:
    folium.CircleMarker([crime_anal_raw['lat'][n], crime_anal_raw['lng'][n]],
                        radius = crime_anal_raw['검거'][n]*10,
                        color = '#3186cc',
                        fill_color = '#3186cc',
                        fill=True).add_to(map)

map.save('folium_kr3.html')
webbrowser.open_new("folium_kr3.html")
