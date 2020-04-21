####### Pandas 를 사용한 데이터 분석 기초
'''
분석할 데이터의 양(volume)이 커지고,
데이터의 입출력 속도(velocity)가 빨라지고
데이터의 종류가 다양해(variety) 짐에 따라
기존보다 데이터를 분석하기 어려워졌고
이로 인해 데이터 분석 분야가 업계의 주목을 받는 것

빅데이터 Volume, Velocity, Variety의 세 가지'V'를 가진 데이터

빅데이터 분석에는
다양한 프로그래밍 언어와 기술이 사용되고 있는데 파이썬도 그 중 하나.

파이썬이 오픈소스 기반의 통계언어인 R과 더불어
빅데이터 분석 분야에서 인기가 높아진 것은 여러 가지 이유가 있지만,
Pandas라는 라이브러리 덕이 크다.
'''

####### Pandas Series
'''
파이썬이 인기있는 이유 중 하나는
파이썬의 기본 자료구조인 리스트, 튜플, 딕셔너리가 사용하기 편리하며
데이터를 다루는 데 효과적이기 때문.

Pandas 역시 효과적인 데이터 분석을 위한
고수준의 자료구조와 데이터 분석 도구를 제공.

Pandas의
Series는 1차원 데이터를 다루는 데 효과적인 자료구조이며,
DataFrame은 행과 열로 구성된 2차원 데이터를 다루는 데 효과적인 자료구조 이다.

Pandas를 이해하려면
가장 먼저 Pandas의 핵심 자료구조인 Series와 DataFrame을 알아야 한다.
'''

######## 파이썬 리스트, 튜플, 딕셔너리
# 리스트
mystock = ['kakao','naver']
print(mystock[0])
print(mystock[1])
for stock in mystock:
    print(stock)
    
# 튜플
'''
튜플은
리스트의 []와 달리 ()를 사용.
수정이 가능한 리스트와 달리 수정할 수 없다.
대신 리스트에 비해서 속도가 빠르다는 장점이 있다.

그래서 원소를 한 번 넣은 후에
수정할 필요가 없으며
속도가 중요한 경우에 리스트 대신 튜플을 사용.
'''

# 딕셔너리
exam_dic = {'key1':'room1', 'key2':'room2'}
print(exam_dic['key1'])
print(exam_dic['key2'])

print(type(exam_dic)) # class dict

# 리스트와 딕셔너리
kakao_daily_ending_prices = [92300, 94300, 92100, 92400, 92600]
for price in kakao_daily_ending_prices:
    print(price)


kakao_daily_ending_prices = {'2016-02-19':92600,
                             '2016-02-18':92400,
                             '2016-02-17':92100,
                             '2016-02-16':94300,
                             '2016-02-15':92300}

print(kakao_daily_ending_prices['2016-02-19'])

# 시리즈는 리스트와도 비슷하고 딕셔너리와도 비슷하다, 데이터분석을 한다고 하면 기본적인 라이브러리가 Pandas

###### Series 기초
'''
Pandas의 Series는 1차원 배열과 같은 자료 구조.
파이썬 리스트와 튜플도 1차원 배열과 같은 자료구조

사실 Pandas의 Series는
어떤 면에서는 파이썬의 리스트와 비슷하고
어떤 면에서는 파이썬의 딕셔너리와 닮은 자료구조

Series를 사용하기에 앞서
Pandas라는 모듈에서 직접 Seires와 DataFrame을
로컬 네임스페이스로 import
'''

import pandas as pd
print(pd.Series)

'''
Series를 직접 로컬 네임스페이스로 import 한 경우에는
pandas는 생략하고 바로 Series라고만 적으면 된다.
'''
from pandas import Series, DataFrame

kakao = Series([92600, 92400, 92100, 94300, 92300]) # 해당 값을 자체는 리스트인데 리스트를 시리즈화 시킨다.
# 시리즈는 리스트 구조가 아니라 인덱스 번호 까지 같이 함께 저장된다.
# 리스트 형태 구조를 갖고 있지만 인덱스번호도 같이 저장 -> index가 일종의 key가 되고 value를 함께 갖는다.
# --> 시리즈는 딕셔너리의 형태로도 볼 수 있다. (시리즈가 뭉쳐서 데이터프레임이 된다.)
print('kakao------------------------')
print(kakao)
print(type(kakao))

'''
Series 객체는
일차원 배열과 달리 값뿐만 아니라
각 값에 연결된 인덱스 값도 동시에 저장.

Series 객체 생성 시에
인덱스 값을 따로 지정하지 않으면
기본적으로 Series 객체는 0부터 시작하는 정숫값을 사용하여 인덱싱.
'''
print(kakao[0])
print(kakao[2])
print(kakao[4])

kakao2 = Series([92600, 92400, 92100, 94300, 92300], 
                index = ['2016-02-19','2016-02-18','2016-02-17','2016-02-16','2016-02-15'])
print('kakao2------------------------')
print(kakao2)
'''
kakao2 라는 Series 객체는
인덱스값으로 날짜에 해당하는 문자열을 지정했기 때문에
정숫값으로 인덱싱하는 것 대신 날짜를 의미하는 문자열을 사용하여
각 날짜에 대한 종가를 바로 얻어올 수 있다.
'''

print(kakao2['2016-02-19'])
print(kakao2['2016-02-18'])
# 시리즈는 인덱스 저장영역과 값 저장영역이 1:1로 매칭되어서 같이 저장된다.

'''
Series 객체의
index와 values 라는 이름의 속성을 통해 접근할 수 있다.
'''
print('for-----------------------------')
for date in kakao2.index:
    print(date)
    
for ending_price in kakao2.values:
    print(ending_price)

'''
Pandas의 Series는
서로 다르게 인덱싱된 데이터에 대해서도
알아서 덧셈 연산을 처리해 준다.
'''
# from pandas import Series, DataFrame
print('mine friend----------------------------')
mine = Series([10,20,30], index = ['naver','sk','kt'])
friend = Series([40,50,60], index = ['kt','naver','sk'])

merge = mine + friend
print(merge)
# index 값을 바꿔서 'kt' -> 'kt'로 하면 일치하는 인덱스 값이 다르므로 연산은 되지만 해당 인덱스를 못찾는 것은 NaN값이 출력

######### Pandas DataFrame
'''
Pandas의 Series가 1차원 형태의 자료구조라면
DataFrame은 여러 개의 칼럼(column)으로 구성된 2차원 형태의 자료구조.

Pandas의 DataFrame을 사용하면
로우와 칼럼으로 구성된 2차원 구조의 데이터를
쉽게 저장하고 조작할 수 있다.
'''

#DataFrame 생성
'''
DataFrame 객체를 생성하는 가장 쉬운 방법은
파이썬의 딕셔너리를 사용하는 것.

딕셔너리를 통해 각 칼럼에 대한 데이터를 저장한 후,
딕셔너리를 DataFrame클래스의 생성자 인자로 넘겨주면
DataFrame 객체가 생성된다.
'''

# 딕셔너리를 사용한 DataFrame 객체 생성
print('raw_data----------------------------')
from pandas import Series, DataFrame
raw_data = {'col0':[1,2,3,4],
            'col1':[10,20,30,40],
            'col2':[100,200,300,400]}

data = DataFrame(raw_data)
print(data)


#       Series('col0') Series('col2')
# index     value         value
# 0          1             10
# 1          2             20
# 2          3             30

# 위와 같이 구성되어있다.
# 딕셔너리 key값들은 col0,1,2로 총 3개로 되어있고, 시리즈가 총 3개로 각각의 인덱스가 부여된다.

'''
col0, col1, col2 라는 세 개의 칼럼이 존재
'col0', 'col1', 'col2' 라는 문자열은
DataFrame의 각 칼럼을 인덱싱하는 데 사용된다.

로우 방향으로는
Series와 유사하게 정수값으로 자동으로 인덱싱 된 것을
확인할 수 있다.

'''

# 'col0', 'col1', 'col2' 를 사용하여 각 컬럼을 선택
print('data["col"]----------------------------')
print(data['col0'])
print(data['col1'])
print(data['col2'])

'''
DataFrame에 있는 각 칼럼은 Series 객체임을 알 수 있다.
즉, DataFrame은
인덱스가 같은 여러 개의 Series 객체로 구성된 자료구조.

data라는 변수가 바인딩하는 DataFrame에는 3개의 Series 객체가 있다.
이는 'col0', 'col1', 'col2'라는 키(key)에 각각 대응되는 값(value)이고,
이것들을 하나의 파이썬 딕셔너리 객체로 생각하는 것.

따라서 'col0', 'col1', 'col2'라는 key를 통해
value에 해당하는 Series 객체에 접근할 수 있다.

'''
print('daeshin------------------------------------')
daeshin = {'open':[11650, 11100, 11200, 11100, 11000],
           'high':[12100,11800,11200,11100,11150],
           'low':[11600,11050,10900,10950,10900],
           'close':[11900, 11600, 11000, 11100, 11050]}
daeshin_day = DataFrame(daeshin)
print(daeshin_day)

'''
DataFrame 객체에는 칼럼의 순서는
DataFrame 객체를 생성할 때 columns 라는 키워드를 지정할 수 있다.
'''

daeshin_day2 = DataFrame(daeshin, columns = ['close', 'open', 'high', 'low']) #  순서 바꾸기
print(daeshin_day2)

'''
DataFrame 에서 인덱스 역시
DataFrame 객체를 생성하는 시점에 index를 통해 지정할 수 있다.

먼저 인덱싱에 사용할 값을 만든 후,
이를 DataFrame 객체 생성 시점에 지정하면 된다.
'''

print('daeshin 3 -------------------------------------')
date = ['20.02.29', '20.02.26', '20.02.25', '20.02.24', '20.02.23']
daeshin_day3 = DataFrame(daeshin, columns = ['open', 'high', 'low', 'close'], index = date)

print(daeshin_day3)

# DataFrame 칼럼, 로우 선택
'''
종가를 기준으로 데이터를 분석한다면
'close'칼럼에 대한 데이터만을 DataFrame 객체로부터 얻어낸다.
'''
close = daeshin_day3['close']
print(close)

'''
DataFrame 객체의 칼럼 이름과 인덱스 값을 확인하려면
각각 columns와 index 속성을 사용.
'''
print(daeshin_day.columns)
print(daeshin_day.index)


print('SQLite -----------------------------------------')
import sqlite3 # DB저장하려면 sqlite3 모듈을 일단 임포트 해야한다.

print(sqlite3.version) #2.6.0
print(sqlite3.sqlite_version) #3.31.1

con = sqlite3.connect("c:/work_python/kospi.db") # 128비트 암호화기능 보유(데이터를 그냥 저장하는게 아닌 암호화 시켜서 저장/복원할 수 있음)
# 실제로 저장되는 파일의 확장자명은 .db 로 저장 -> 이렇게 저장해야 다른 db에 이식 가능
print(type(con)) #<class 'sqlite3.Connection'>

cursor = con.cursor() # 얘가 cursor 쿼리를 실행시키는 것(객체전달받아야함) -> 자바의 pstmt, stmt 와 같은 기능 (쿼리문 실행시키는 기능)

# 테이블 생성(close는 내장값이여서 closing으로 명명)
cursor.execute("CREATE TABLE kakao(Date text, Open int, High int, Low int, Closing int, Volume int)")
cursor.execute("INSERT INTO kakao VALUES('16.06.03', 97000, 98600, 96900, 98000, 321405)")

cursor.execute("SELECT * FROM kakao")
print(cursor.fetchone()) #('16.06.03', 97000, 98600, 96900, 98000, 321405) 출력
print(cursor.fetchone()) # 한 번에 데이터를 하나만 가져오는 것(rs.next()로 넘겨주는 것 처럼 한번에 하나 가져오는 것)

con.commit()
#con.close()

cursor.execute("SELECT * FROM kakao")
print(cursor.fetchall()) # 한 번에 모든 데이터를 가져오는 것

cursor.execute("SELECT * FROM kakao")
kakao = cursor.fetchall()
print(type(kakao)) # <class 'list'>
print(kakao[0][0]) #16.06.03
print(kakao[0][1]) #97000
print(kakao[0][2]) #98600
print(kakao[0][3]) #96900
print(kakao[0][4]) #98000
print(kakao[0][5]) #321405


con.commit()
con.close()

# web 데이터 읽기
import pandas_datareader.data as web
import pandas as pd
import datetime as dt

#야후증권 
#https://finance.yahoo.com/
import yfinance
import sqlite3

# 추출할 시작 날짜 종료 날짜 설정
start = dt.datetime(2018, 1, 1)
end = dt.datetime(2019, 1, 1)

# 야후증권으로부터 삼성전자 주식 추출
samsung = web.get_data_yahoo("005930.KS", start, end)

print(type(samsung)) #<class 'pandas.core.frame.DataFrame'>

# 상위 5개만 출력
sf = samsung.tail(5)
print(sf)

# 삼성전자 1년 데이터 데이터베이스에 저장
con = sqlite3.connect('c:/work_python/kospi3.db')

# dataframe은 DB에 저장할 수 있는 함수를 제공. : to_sql()
# Auto Commit이 기본
samsung.to_sql('samsung',con,chunksize=1000)

# dataframe은 DB를 통해 조회할 수 있는 쿼리도 제공
readed_df = pd.read_sql("SELECT * FROM samsung", con, index_col = 'Date')
print(readed_df)

'''
기본 설정값

DataFrame.to_sql(name,
                 con,
                 flavor = 'sqlite',
                 schema= None,
                 if_exists ='fail',
                 index = True,
                 index_label = None,
                 chunksize =None,
                 dtype=None)
'''

'''
name : SQL 테이블 이름으로 파이썬 문자열 형태로 나타낸다.
con : Cursor 객체

flavro : 사용한 DBMS를 지정할 수 있는데 'sqlite'또는 'mysql'을 사용할 수 있다. 기본값은 sqlite

schema : Schema를 지정할 수 있는데 기본값은 None 이다.

if_exists : 데이터베이스에 테이블이 존재할 때 수행 동작을 지정한다. 'fail', 'replace', 'append'중 하나를 사용할 수 있는데 기본값은 'fail'이다.
 'fail'은 데이터베이스에 테이블이 있다면 아무 동작도 수행하지 않는다.
 'repalce'는 테이블이 존재하면 기존 테이블을 삭제하고
 'append'는 테이블이존재하면 데이터만을 추가한다.

index : DataFrame의 index를 데이터베이스에 칼럼으로 추가할지에 대한 여부를 지정한다. 기본값은 True이다.

index_label : 인덱스 칼럼에 대한 라벨을 지정할 수 있다. 기본값은 None 이다.

chunksize : 한 번에 저장되는 로우의 크기를 정수값으로 지정할 수 있다.
 기본값은 None으로 DataFrame 내의 모든 로우가 한 번에 저장된다.
 
dtype : 칼럼에 대한 SQL 타입을 파이썬 딕셔너리로 넘겨줄 수 있다.
'''

