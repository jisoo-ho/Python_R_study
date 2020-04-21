# https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000
# 여기에 있는 썸네일 저장
# 파일명은 썸네일 제목
# 타이틀과 가격 DB에 저장 
# 이미지파일 압축, DB파일 하나

import errno
from bs4 import BeautifulSoup

import requests, re, os
from urllib.request import urlretrieve # 추가

# 저장폴더를 생성
try:
    if not(os.path.isdir('image2')): #이미지 폴더가 없으면
        os.makedirs(os.path.join('image2')) #폴더 생성
        print("이미지 폴더 생성 성공")
    
except OSError as e:
    if e.errno != errno.EEXIST: # 없으면
        print("폴더생성실패") # 실패 출력 
        exit()
        

# 웹페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000003")
print(type(html)) # <class 'requests.models.Response'>
soup = BeautifulSoup(html.text, 'html.parser')
print(type(soup)) # <class 'bs4.BeautifulSoup'>
html.close()



# 쇼핑몰 탑100 영역 추출하기
data1_list = soup.findAll('ul',{'class':'type_normal'})
print(data1_list)
print(type(data1_list)) # <class 'bs4.element.ResultSet'>


# 전체 리스트
li_list=[]
for data1 in data1_list:
    # 품명+썸네일 영역 추출
    li_list.extend(data1.findAll('li'))
    
print(li_list) #전체 데이터 확인


# 가격태그 100개 추출
li_price = data1.findAll('span',{'class':'num'})
print(type(li_price))# <class 'bs4.element.ResultSet'>
print(li_price)

#가격만 추출
li_price_list2 = []
for data in li_price:
    li_price_list2.append(data.text)
print(li_price[0])

#가격을 int 타입으로 변경
price_int_list = []
for li in li_price_list2:
    price = li
    price = re.sub(',','',price)
    price = int(price)
    price_int_list.append(price)
print(len(price_int_list))

#썸네일, 품명, 가격 추출
names = []
for li in li_list:
    img = li.find('img')
    title = img['alt']
    names.append(img['alt'])
    img_src = img['data-original']
    title = re.sub('[^0-9a-zA-Zㄱ-힗]','',title)
    urlretrieve(img_src, './image2/'+title+'.jpg')
print(len(names))

import sqlite3

con = sqlite3.connect("c:/work_python/digital_jisoo.db")

import pandas as pd
from pandas import Series, DataFrame

raw_data = {'제품명' : names,'가격' : price_int_list}

data = DataFrame(raw_data)
print(data)

data.to_sql('digital_jisoo', con, chunksize=1000, index = False)

read_df = pd.read_sql("SELECT * FROM digital_jisoo", con)
print(read_df)

con.commit()
con.close()
