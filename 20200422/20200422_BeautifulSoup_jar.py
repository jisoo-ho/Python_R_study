# BeautifulSoup 기본 사용

# 예제로 사용할 html 문서
# 카페의 (BeautifulSoup 기본 사용 데이터) 게시글 내용 복사
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# soup.prettify() : html 문서의 계층 구조를 알기 쉽게 보여준다
print(soup.prettify())

# title 태그 반환
soup.title
print(soup.title)

# title 태그 이름('title') 을 반환
soup.title.name
print(soup.title.name) # 지정한 태그의 이름까지 꺼낼 경우

# title 태그의 문자열을 반환
soup.title.string
print(soup.title.string)

# title 태그의 부모 태그의 이름을 반환
soup.title.parent.name
print(soup.title.parent.name)

# 첫 p 태그를 반환
soup.p
print(soup.p)

# 'class' 속성이 있는 첫 p 태그를 반환
# soup.p['class']
print(soup.p['class'])

# a 태그 반환
soup.a
print(soup.a)

# 모든 a 태그를 리스트 형태로 반환
soup.find_all()
print(soup.find_all('a'))

# soup.find() : 설정한 값에 해당하는 태그 반환
# id가 'link3'인 태그 반환
soup.find(id="link3")

# get() : href 속성을 반환
for link in soup.find_all('a'):
    print(link.get('href'))
    
# get_text() : html 문서 안에 있는 텍스트 반환
print(soup.get_text())

# Requests 기본 사용
'''
html 소스 가져오기
Requests를 사용하면 아래와 같이 간단한 코드만으로
웹페이지의 html 소스를 가져올 수 있다.
'''

import requests

# requests.get() 에 의한 response에는 다양한 정보가 포함되어 있다.
r = requests.get('http://google.com')
html = r.text
print(html)

'''
웹페이지의 content를 유니코드 형태가 아니라 bytes 형태로 얻기 위해서는
r.text가 아닌 r.content를 사용할 수도 있다.
'''
r = requests.get('https://google.com')
html = r.content
print(html)

# response 객체 : request.get()의 반환 객체
'''
response 객체는 HTTP request에 의한 서버의 응답 정보를 갖고 있다.
status_code, headers, encoding, ok 등의 속성을 이용하면
다양한 정보를 얻을 수 있다.
'''

import requests

r = requests.get('https://google.com')
html = r.content
print(r.status_code) # 200 : 잘 실행됨!
print(r.headers['Content-Type'])
print(r.encoding)
print(r.ok)

'''
status_code는
정상일 경우 200, 페이지가 발견되지 않을 경우 404

encoding 방식은 ISO-8859-1 이고,
요청에 대한 응답이 정상적으로 이루어졌음을 알 수 있다.

(status_code가 200보다 작거나 같은 경우 True, 그렇지 않은 경우 False)
'''

'''
만약 인코딩 방식이 달라서 한글이 제대로 표시되지 않으면
아래와 같이 인코딩 방식을 변경
'''

r.encoding = 'utf-8'

'''
requests를 이용해서 html 소스를 가져왔지만,
단순한 문자열 형태이기 때문에 파싱(parsing)에 적합하지 않다.

그렇기 때문에 BeautifulSoup을 이용해서
파이썬이 html 소스를 분석하고 데이터를 추출하기 편리하도록 객체로 변환
'''

# 많이 본 네이버 뉴스
'''
파이썬과 BeautifulSoup을 이용하면
웹 크롤러를 간단하게 만들 수 있다.
네이버 뉴스의 '많이 본 뉴스' 가져오기
'''

import requests
from bs4 import BeautifulSoup

'''
주소 :
'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&date=20200422'

위의 주소에서 알 수 있듯이 맨 뒤에 날짜를 바꿔주면
해당하는 날짜의 많이 본 뉴스를 볼 수 있다.
'''
url = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&date=20200422'
r = requests.get(url)
html = r.content
soup = BeautifulSoup(html, 'html.parser')

# 원하는 데이터 추출하기
# 네이버 많이 본 뉴스 페이지에 헤드라인만 추출해서 출력
titles_html = soup.select('.ranking_section > ol> li > dl > dt > a')

# 30개의 헤드라인이 순서대로 출력
for i in range(len(titles_html)):
    print(i+1, titles_html[i].text)

    
#삼성전자 주식 일별시세 가져오기
'''
네이버 증권에서 제공하는 삼성전자 종목(005930)의 일별시세를 가져오기

주소 : http://finance.naver.com/item/sise_day.nhn?code=005930
위의 주소와 같이 뒷부분에 code=005930와 같이 종목코드를 입력해주면 해당 종목의 일별시세를 볼 수 있다.
'''

# 원하는 데이터 추출하기
'''
종목의 일별시세 페이지에서
날짜, 종가, 거래량만 추출해서 출력해보기
'''

'''
개발자 도구(ctrl+shift+i 또는 f12)를 통해 소스를 보면 날짜, 종가, 거래량이 나온 부분 찾을 수 있다.
'table', 'tr, 'td' 태그 안의 텍스트임을 알 수 있다.
'''
import requests
from bs4 import BeautifulSoup as bs

# 종목의 코드와 페이지 수를 입력하는 함수
def print_stock_price(code, page_num):
    
    # result에는 날짜, 종가, 거래량이 추가
    result = [[], [], []]
    
    # 주소 뒷부분에 &page=2 와 같은 형식으로 연결해주면
    # 해당 페이지의 일별시세 볼 수 있다
    for n in range(page_num):
        url = 'http://finance.naver.com/item/sise_day.nhn?code=' + code + '&page=' + str(n+1) #페이지값은 문자열로! #주소줄 기입 시 한줄로!
        r= requests.get(url)
        html = r.content
        soup = bs(html,'html.parser')
        
        # table 안의 tr 태그를 리스트형태로 가져온다
        tr = soup.select('table > tr')
        
        # 첫번째 tr태그는 th태그가,
        # 마지막 tr태그는 페이지 넘버가 있어서 제외
        for i in range(1, len(tr)-1):
            #text가 없는 row가 존재.
            if tr[i].select('td')[0].text.strip():
                #text가 있는 row에 대해서
                #첫 번째(날짜),두번재(종가),일곱번째(거래량)
                #td태그의text를 가져온다.
                result[0].append(tr[i].select('td')[0].text.strip())
                result[1].append(tr[i].select('td')[1].text.strip())
                result[2].append(tr[i].select('td')[6].text.strip())

    for i in range(len(result[0])):
        print(result[0][i],result[1][i],result[2][i])
#------------------print_stock_price() END -----------------------------#
        
# 해당 종목의 코드와 50 페이지 입력
stock_code = '005930'
pages = 50

# 날짜, 종가, 거래량이 최근순으로 출력
print_stock_price(stock_code, pages)
