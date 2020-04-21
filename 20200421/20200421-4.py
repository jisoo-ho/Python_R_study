# 이 페이지의 코드를 가지고 쇼핑몰의 이미지를 긁어와서 머신러닝으로 학습을 시킬 때 사용할 수 있다.
import errno
from bs4 import BeautifulSoup

import requests, re, os
from urllib.request import urlretrieve # 추가

# 저장폴더를 생성
try:
    if not(os.path.isdir('image')): #이미지 폴더가 없으면
        os.makedirs(os.path.join('image')) #폴더 생성
        print("이미지 폴더 생성 성공")
    
except OSError as e:
    if e.errno != errno.EEXIST: # 없으면
        print("폴더생성실패") # 실패 출력 
        exit()

# 웹페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
print(type(html)) # <class 'requests.models.Response'>
soup = BeautifulSoup(html.text, 'html.parser')
print(type(soup)) # <class 'bs4.BeautifulSoup'>
html.close()

# 요일별 웹툰영역 추출하기
data1_list = soup.findAll('div',{'class':'col_inner'})
#print(data1_list)

# 전체 웹툰 리스트
li_list=[]
for data1 in data1_list:
    # 제목+썸네일 영역 추출
    li_list.extend(data1.findAll('li'))
    # 해당 부분을 찾아 li_list와 병합
#print(li_list)

#각각 썸네일과 제목 추출하기
for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    #print(title,img_src)
    # 해당 영역의 글자가 아닌 것은 ''로 치환
    title = re.sub('[^0-9a-zA-Zㄱ-힗]','',title)
    #주소, 파일경로+파일명+확장자
    urlretrieve(img_src, './image/'+title+'.jpg')
    
