#############################
# R 에서 오라클 데이터 읽어오기
#############################

# R에서 데이터베이스에 접속해서 데이터를 가져오는 방법은 2가지 정도.
# 하나는 자바의 기능을 이용한 것.
# 또 다른 하나는 다른 언어의 기능을 사용하지 않고
# 순수 R의 패키지를 이용하는 방법.

# R에서는 Select 구문을 실행하는 경우 바로 data.frame으로 리턴.
# 관계형 데이터베이스의 데이터를 사용하는 것이
# 일반적인 프로그래밍 언어보다 편리.
setwd("C:/rStudy/20200407")

# 자바의 JDBC를 이용하기 위한 패키지 설정
install.packages("RJDBC")
install.packages("igraph")

# 라이브러리 등록
library(RJDBC)
library(rJava)
library(igraph)

# 작업 디렉토리 안에 data 디렉토리에 ojdbc6.jar 파일이 존재
jdbcDriver <- JDBC(driverClass="oracle.jdbc.OracleDriver",
                   classPath="C:/rStudy/dataset/ojdbc6.jar")

# 데이터베이스 연결
con <- dbConnect(jdbcDriver,
                 "jdbc:oracle:thin:@localhost:1521:XE",
                 "inventory",
                 "1234")

# 데이터베이스 연결 종료
# dbDisconnect(con)

# dbGetQuery나 dbSendQuery를 이용해서
# 첫 번째 매개변수로는 데이터베이스 연결변수를 주고
# 두 번째 매개변수로는 select 구문을 주면 데이터를 가져온다.

# dbGetQuery는 data.frame을 리턴하고
# dbGetQuerty는 무조건 모든 데이터를 가져와서
# data.frame을 만들기 때문에 많은 양의 데이터가 검색된 경우
# 메모리 부족 현상을 일으킬 수 있다.

# 이런 경우에는 dbSendQuery를 이용해서
# 데이터에 대한 포인터만 가져온 후
# fetch(커서, n=1)을 이용해서 

# 이런 경우에는 dbSendQuery를 이용해서 데이터에 대한 포인터만 가져온 후
# fetch(커서, n=1)을 이용해서
# n값으로 데이터 개수를 대입해서 필요한 만큼 데이터만 가져와서
# data.frame을 만들 수 있다.

# cursor는
# 데이터를 주고 다음으로 자동으로 넘어가는 특징을 가지고 있다.
# 하지만 전진만 하기 때문에 한 번 읽은 데이터를 다시 읽지 못한다.

# select 구문을 실행하고 저장하기
tablelists <- dbGetQuery(con,"select * from tab")

result <- dbGetQuery(con,"select * from PRODUCT_TABLE")

# 유형확인
class(result) # data.frame

#실행 결과를 가지고 그래프를 그릴 수 있는 프레임으로 변환
g <- graph.data.frame(result, directed=T)

#관계도 작성
plot(g,
     layout=layout.fruchterman.reingold,
     vertex.size=8,
     edge.array.size=0.5)

#오라클 쿼리 실행(sqldf 패키지)
#오라클 sql쿼리문을 이용하기 위한 패키지 설정
install.packages("sqldf")

# 오라클 sql 쿼리문을 이용하기 위한 라이브러리 등록
library(sqldf)

head(iris)

sqldf("select Species from iris")

#head
head(iris)

sqldf("select * from iris limit 4")

#subset
#subset : 조건을 만족하는 벡터, 행렬, 데이터 프레임의 일부를 반환한다.
subset(iris, Species %in% c("setosa"))
sqldf("select * from iris where Species in ('setosa')")

subset(iris, Sepal.Length >= 5 & Sepal.Length <= 5.2)
sqldf('select * from iris where "Sepal.Length" between 5 and 6')

#금일 날씨 xml 데이터
#http://www.weather.go.kr/weather/forecast/mid-term-xml.jsp?stnld=109
#JSON 샘플 데이터
#https://api.github.com/users/hadley/repos

####################################################
# XML 파싱( 데이터 크롤링과 방법은 비슷 )
####################################################
#html 파싱과 동일
#XML은 엄격한 HTML이고 태그의 해석을 브라우저가 하지 않고
#클라이언트가 직접 한다는 점이 HTML과 다른 점.
#모든 HTML파싱 방법은 XML에 적용 가능.
#XML파싱 방법으로는 파싱하지 못하는 HTML이 있을 수도 있다.

# 1. 태그의 내용 가져오기
#문자열을 가지고 올 주소를 생성
url <- 'http://www.weather.go.kr/weather/forecast/mid-term-xml.jsp?stnld=109'


#문자열 다운로드
#rvest 라이브러리를 ON 시켜야 한다.
weather <- read_html(url)
weather

tmn <- weather %>% html_nodes("tmn") %>% html_text()
tmn

# JSON 파싱
######################################
#jsonlite 패키지와 httr 패키지를 이용.
#frameJSON() 함수에 URL을 대입하면 data.frame으로 리턴

#즉, https://api.github.com/users/hadley/repos 데이터를
#data.frame으로 변환

#1.필요한 패키지 설치
install.packages("jsonlite")
install.packages("httr")

#2. 필요한 패키지 로드
rm(list=ls())

library(jsonlite)
library(httr)

#3.json 데이터 가져오기
df <- fromJSON("https://api.github.com/users/hadley/repos") # hadley 씨의 깃허브
head(df,1)


#Markdown
#기존에 우리가 인터넷 세상에서 보는 웹 페이지(=결국 문서지..)는
#HTML이라는 Markup(마크업) 언어인데,
#HTML을 제대로 쓰려면 태그 등을 알아야 하는 부담이 있다.
#이러한 Markup 언어의 단점을 보완하기 위해
#2004년 John Grube가 읽기도 쓰기도 쉬운 Markup 언어를 만들었는데,
#이게 바로 Markdown 이며 확장자는 .rm 을 사용

#R Markdown, knitr
#R에서도 이 Markdown을 활용하여
#코드 ,데이터가 연동된 Dynamic 한 문서를 만들 수 있는데,
#이게 바로 'R Markdown' 이며
#R과 Markdown 을 체계적으로 연결시켜주는 도구가 'knitr(니터라고 읽음) 패키지이다.

#Markdown 문서는 확장자가 .md인데, R Markdown 문서는 .rmd 인게 차이점.
#  * R 과 knitr를 활용한 데이터 연동형 문서 만들기(고석범)
# ** R Markdown document is written in markdown (an easy-to-write plain text format) and contains chunks of embedded R code, like the document below. 

# 데이터 분석용 프로그래밍 언어 : R
# 사람이 읽을 수 있는 문서를 만들어주는 언어(마크업 언어) : Markdown 
# 두 언어를 체계 있게 연결시키는 도구 : Knitr 패키지 
# 이 모두를 통합한 개발 환경 : Rstudio

