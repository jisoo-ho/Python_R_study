# 네이버 웹툰 썸네일 가져오기

# 제목과 썸네일이 같이 존재하는 영역
from bs4 import BeautifulSoup
import requests

# 웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
print(type(html)) # <class 'requests.models.Response'>
soup = BeautifulSoup(html.text, 'html.parser')
print(type(soup)) # <class 'bs4.BeautifulSoup'>
html.close()

# 요일별 웹툰영역 추출하기
data1_list = soup.findAll('div',{'class':'col_inner'})
print(data1_list)
print(type(data1_list)) # <class 'bs4.element.Tag'>
# 전체 웹툰 리스트
'''
요일별 웹툰 영역 중 제목과 썸네일 영역을 하나의 리스트로 추출
'''

li_list=[]
    # 제목+썸네일 영역 추출
    # 해당 부분을 찾아 li_list와 병합
for data1 in data1_list:
    li_list.extend(data1.findAll('li'))
    
print(li_list)

# 각각의 요소 중 <img> 태그의 제목과 썸네일(~.jpg)만 추출하기
'''
<img alt="불발소년" height="90" onerror="this.src='https://ssl.pstatic.net/static/comic/images/migration/common/blank.gif'"
 src="https://shared-comic.pstatic.net/thumb/webtoon/743721/thumbnail/thumbnail_IMAG10_1a440839-f0da-4260-a107-8840f6fa4fc9.jpg" 
 title="불발소년" width="83"/>
'''

for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    print(title, img_src)

# 다운로드하기
'''
이미지 또는 동영상 링크가 있다면 다운로드 하는 방법은 쉽다.
from urllib.request import urlretrieve 를 추가한 뒤, 
urlretrieve 호출 시에 링크와 저장할 파일명을 넣으면 된다. (다운로드 할 때 파일명에 특수문자가 있으면 오류 발생)-제거필요
'''

# 특수문자 처리
'''
도중에 에러가 난 부분을 보면 파일명에 특수문자가 있는 경우
따라서 추출한 제목에서 특수문자는 다른 문자로 변경해주거나 삭제해 주어야 한다.

변경은 replace 를 하면 되는데,
여기서는 정규식 표현을 이용한 re모듈을 사용하여 삭제.
따라서 re모듈을 import
'''

# 저장폴더 생성
'''
여기서는 os 모듈을 참조
os.path.isdir : 이미 디렉토리가 있는지 검사
os.path.join : 현재 경로를 계산하여 입력을 ㅗ들어온 텍스트를 합하여 새로운 경로를 만듦

os.makedirs : 입력으로 들어온 경로로 폴더를 생성

모듈 참조와 아래 urlretrieve 부분도 변경
'''
