'''
BeautifulSoup - 파이썬 웹 크롤링 라이브러리
BeautifulSoup은 파이썬 웹 크롤링에 가장 널리 사용되는 라이브러리이자 툴 입니다.

웹 크롤링(Web crawling) 또는 스크래핑(Scrapping)은
웹 페이지들을 긁어와서 데이터를 추출하는 것을 말합니다.

웹 크롤러는 자동화된 방식으로 웹 페이지들을 탐색하는 컴퓨터 프로그램입니다.

파이썬과 BeautifulSoup 라이브러리를 이용하면
프로그래밍에 익숙하지 않은 비전공자나 입문자도 쉽게 크롤링을 할 수 있습니다.

BeautifulSoup 크롤링 예제에서 Requests와 BeautifulSoup 라이브러리를 사용하는데,
기본적으로 아나콘다 통합 패키지에 포함되어 있지만
설치되어 있지 않다면 설치를 진행합니다.

'''
# Requests 설치
# pip install requests

# BeautifulSoup 설치
# pip install beautifulsoup4

# https://search.naver.com/search.naver?query=날씨

# 네이버 날씨 미세먼지 가져오기
# 웹 페이지 가져오기
# 'https://search.naver.com/search.naver?query=날씨'

from bs4 import BeautifulSoup as bs # beautifulsoup4 : html 태그 파싱작업할 때 필요한 패키지
import requests # 웹 서버로부터 데이터를 요청할 때 필요한 패키지

# requests 가 가지고 있는 get 함수를 이용해서 서버에 요청
html = requests.get('https://search.naver.com/search.naver?query=날씨')
print(html)
print(type(html)) # <class 'requests.models.Response'>
print(type(html.text)) # <class 'str'> : 해당 링크의 모든 태그들을 다 가지고 들어온다

# 파싱
soup = bs(html.text, 'html.parser') # 읽어들인 것을 뷰티풀숩 객체로 만들었다
print(soup) # 읽어들인 모든 텍스트
print(type(soup)) # <class 'bs4.BeautifulSoup'>

# 요소 1개 찾기(find)
# 미세먼지 정보가 있는 div 요소만 추출
data1 = soup.find('div',{'class':'detail_box'}) # html도, json도 파싱 가능하다. 
print(data1) # div 태그에 class 명이 detail_box 인 애들을 모두 긁어온다.
print(type(data1)) # <class 'bs4.element.Tag'>

# 요소 모두 찾기(findAll)
'''
find와 사용방법이 똑같으나
find는 처음 매칭된 1개만,
findAll은 매칭된 모든 것을 리스트로 반환.
'''
data2 = data1.findAll('dd') # data1이 가지고있는 것들 중 태그명이 dd로 되어있는 것을 모두 가져온다.
# find('dd')로 했으면
# [<dd class="lv1"><span class="num">25㎍/㎥</span>좋음<span class="ico"></span></dd> 이거만 가져온다.

print(data2) # dd 태그를 가져온다
print(type(data2)) # <class 'bs4.element.ResultSet'> : 리스트 형태로 반환

# 내부 텍스트 추출
# span 태그에 속성과 속성값은 class="num"
fine_dust = data2[0].find('span',{'class':'num'}) # data2[0]번은 미세먼지, 1번은 초미세먼지, 2번은 오존지수
print(fine_dust)
print(type(fine_dust)) # <class 'bs4.element.Tag'>

# 내부 텍스트만 골라내도록 .text를 이용
fine_dust = data2[0].find('span',{'class':'num'}).text
print(fine_dust)
print(type(fine_dust)) # <class 'str'>

# 초미세먼지 추출
'''
data2 변수에서
미세먼지는 0번 인덱스,
초미세먼지는 1번 인덱스
'''
ultra_fine_dust = data2[1].find('span',{'class':'num'}).text
print(ultra_fine_dust)

# 오존지수 추출
ozone = data2[2].find('span',{'class':'num'}).text
print(ozone)

# 데이터프레임으로 만들기(미세먼지&오존)
import pandas as pd

weather = {'미세먼지':fine_dust,'초미세먼지':ultra_fine_dust,'오존':ozone}
print(weather)
df_weather = pd.DataFrame(weather, columns=['미세먼지','초미세먼지','오존'], index = ['20.04.21'])
print(df_weather)
