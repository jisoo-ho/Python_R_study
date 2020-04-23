# =============================================================================
#  강남 3구는 안전한가 ?
# =============================================================================

'''
강남 3구의 주민들이 자신들이 거주하는 구의 체감 안전도를
높게 생각한다는 기사를 확인해보도록 한다.
기사 원문 : http://news1.kr/articles/?1911504

Matplotlib 의 heatmap 등을 그릴 때
cmap의 디폴트 설정이 변경되어 heatmap 등에서 cmap을 적용할 때
옵션을 잡아주어야 동일한 효과가 나타난다.

Folium 0.4.0으로 버전업 되면서
choropleth 명령에서 geo_str 옵션명이 geo_data 옵션명으로 변경됨.
circle marker 적용할 때, fill=True 옵션을 반드시 사용해야 함.
'''

##########
# 데이터 정리하기
# 필요한 모듈을 import

import numpy as np
import pandas as pd

'''다운받은 데이터(csv) 파일을 읽는다,
콤마(,)로 천단위가 구분되어 있고, 한글 인코딩은 euc-kr
'''

crime_anal_police = pd.read_csv('./data/02. crime_in_Seoul.csv',
                                thousands = ',', encoding='euc-kr') # 천단위의 쉼표는 제거

r=crime_anal_police.head()
print(r)


'''관서별로 되어 있는 데이터를 소속 구별로 변경
1. 경찰서 이름으로 구 정보 얻기'''

# 구글 맵스를 사용해서 경찰서의 위치(위도, 경도) 정보를 받아온다.

import googlemaps

# 자신의 key를 사용.
gmaps_key = "AIzaSyDaqk0cpRrmBkT6-77TZLq2LUuml_mnro0"
gmaps = googlemaps.Client(key=gmaps_key)
r=gmaps.geocode('서울중부경찰서', language='ko')
print(r)


# 중부서, 수서서 => 서울**경찰서로 변경
station_name = []

for name in crime_anal_police['관서명']:
    station_name.append('서울'+ str(name[:-1])+'경찰서')
    
print(station_name)
print(type(station_name)) #<class 'list'>

# 경찰서 이름을 이용하여 주소 얻기
station_address = []
station_lat =[]
station_lng =[]

for name in station_name:
    tmp = gmaps.geocode(name, language='ko')
    station_address.append(tmp[0].get("formatted_address")) # 구글에서 보내준 데이터 안에 있는 key 명들임(JSON 형태)
    
    tmp_loc = tmp[0].get("geometry") # geometry도 구글에서 보내준 데이터의 key 명(JSON 형태)
    
    station_lat.append(tmp_loc['location']['lat']) # (JSON 형태 key 명)
    station_lng.append(tmp_loc['location']['lng']) # (JSON 형태 key 명)
    
    print(name+'-->' + tmp[0].get("formatted_address"))



print(station_address)
print(type(station_address)) # <class 'list'>


'''저장한 주소를 띄어쓰기, 공백으로 나누고, 구별이라는 컬럼으로 저장.'''
gu_name = []

for name in station_address:
    tmp = name.split()
    
    tmp_gu = [gu for gu in tmp if gu[-1] =='구'][0]
    
    gu_name.append(tmp_gu)

'''
tmp_gu = 
        for gu in tmp:
            if gu[-1] =='구'[0]:
name = '대한민국 서울특별시 중구 을지로동 수표로 27', ~~~
tmp = name.split()
tmp : '대한민국', '서울특별시', '중구', '을지로동', '수표로', '27'
gu : '대한민국'
     '서울특별시'
     '중구' 
       ~
     '27'
'''
    
crime_anal_police['구별'] = gu_name
print(crime_anal_police.head())


'''
금천 경찰서의 경우 관악구로 되어 있어서 금천구로 변경
'''
crime_anal_police[crime_anal_police['관서명']=='금천서']
crime_anal_police.loc[crime_anal_police['관서명']=='금천서',['구별']] =='금천구'

crime_anal_police[crime_anal_police['관서명']=='금천서']

#현재까지 작업 내용 저장.
crime_anal_police.to_csv('./data/02_crime_in_Seoul_include_gu_name.csv', sep = ',', encoding='utf-8')

# 읽기 내용 확인
pd.read_csv('./data/02_crime_in_Seoul_include_gu_name.csv', encoding='utf-8')
