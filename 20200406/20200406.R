############# 크롤링 작업
install.packages("rvest")
library(rvest)

naver <- read_html("http://www.naver.com")
naver

# 1. 웹에서 데이터를 가져오기 위한 패키지 설치
install.packages("rvest")

# 2. 패키지 메모리 로드
library(rvest)

# 3. 문자열을 가지고 올 주소를 생성
url <- 'http://tv.naver.com/r/category/drama'


# 4. 문자열 다운로드
cast <- read_html(url)

# 5. 문자열 확인
cast

# 6. span 안에 내용들이 출력
craw <- cast %>% html_nodes(".tit") %>% html_nodes('span')
craw

# 7. tit 클래스 안에 있는 span 안에 내용 가져오기
craw <- cast %>% html_nodes(".tit") %>% html_nodes('span') %>% html_text()
craw

# 8. tooltip 태그 안의 내용 가져오기 (전체 페이지에서 tooltip 태그를 찾아서 시작태그와 닫는태그 사이에 있는걸 가져온다.(tooltip 태그가 없으면 값 증발))
craw <- cast %>% html_nodes("tooltip") %>% html_text()
craw


#########################
# 한겨레 신문에서 데이터를 검색한 후
# 검색 결과를 가지고 워드 클라우드 만들기

# 한겨레 신문사에서 지진으로 뉴스 검색하는 경우
# url
# http://search.hani.co.kr/Search?command=query&keyword=%EC%A7%80%EC%A7%84&sort=d&period=all&media=news
# http://search.hani.co.kr/Search?  : Search 가 URL 패턴명 지정(서블릿에서 어노테이션 같은 역할)
# command, keyword, sort, period, media 는 파라미터명(수정 불가 값들)
# command=query&  : query와 같이 형식이 정해진 애들은 수정할 수 없다.
#   keyword=%EC%A7%80%EC%A7%84& : 검색어는 한글이 깨져서 들어갔기 때문에 원하는 검색어를 입력하면 된다.
#   sort=d&
#   period=all&
#   media=news
# --> 검색한 기사를 가져올 경우, 실제 기사 원본 내부의 글자들이 필요하기 때문에 링크들에 관련된 주소를 다 뽑아와야 한다.

# http://search.hani.co.kr/Search?command=query&keyword="검색어 입력부분"&sort=d&period=all&media=news

# 기사 검색이나 SNS 검색을 하는 경우
# 검색어를 가지고 검색하면 그 결과는 검색어를 가진 URL의 모임이다
# 기사나 SNS 글이 아니다

# ★ 검색결과에서 URL을 추출해서 그 URL의 기사 내용을 다시 가져와야 함(링크를 모두추출해서 링크에 다시 접속한 후 해당 기사 내용을 하나씩 모두 읽어온다.)
# ★ dt 태그안에 있는 a태그의 href 속성의 값이 실제 기사의 링크이다.

# 실제 기사에서 클래스가 text 안에 있는 내용이 기사 내용이다.

# 1. 기존의 변수를 모두 제거
rm(list=ls()) # R 스튜디오에 있는 모든 변수를 제거하는 함수 remove 함수

# 2. 필요한 패키지 설치
install.packages("stringr")
install.packages("wordcloud")
install.packages("KoNLP")
install.packages("dplyr")
install.packages("RColorBrewer")
install.packages("rvest")

# 3. 필요한 패키지 로드
library(stringr)      # 문자열 조작하는 전문 패키지
library(wordcloud)    # 시각화작업 시 필요한 패키지
library(KoNLP)        # 명사 추출과 같은 작업을 위한 사전을 포함하고 있는 패키지
library(dplyr)        # 데이터프레임을 수정하거나 합하거나 하는 데이터프레임에 관련된 함수를 가진 패키지
library(RColorBrewer) # 색상과 관련된 패키지, 시각화작업에서 필요하다.
library(memoise)      # mf <- 메모(f)는 f의 메모 사본인 mf를 작성한다. 
# 메모된 복사본은 기본적으로 같은 기능의 더 게으른 버전이다. 
# 즉, 새로운 호출의 답을 저장하고, 오래된 호출의 답을 다시 사용한다. 
# 적절한 상황에서, 이것은 정말 멋진 속력을 낼 수 있다.



# 4. 웹에서 문자열을 가져와서 html 파싱을 하기 위한 패키지 로드
library(rvest)        # 웹 페이지 크롤링 시 가장 기본적인 패키지


# 5. 기사 검색을 위한 url 생성
url <- 'http://search.hani.co.kr/Search?command=query&keyword=코로나19&sort=d&period=all&media=news'
# &media=news
# &media=magazine
# &media=common

# 6. url에 해당하는 데이터 가져오기
k <- read_html(url, encoding="utf-8") # url 에 있는 값을 UTF-8 방식으로 읽어와서 k변수에 저장 
k

# 7. dt 태그 안에 있는 a 태그 들의 href 속성의 값을 가져오기
k <- k %>%              # href 가 a태그 안에 있고, 기사 제목들에 관련된 a태그는 dt태그 
  html_nodes("dt") %>% # 내부에 있기 때문에 전체 페이지에서 %>% dt 시작태그와 닫는 태그를 모두 찾아온다.
  html_nodes("a") %>% # 그 결과값을 다시 html_nodes 함수에 전달하면 dt 태그 사이에서 a 태그만 다시 추출 
  html_attr("href")
k

# 8. k에 저장된 모든 URL 에 해당하는 데이터의 클래스가 text인 데이터를 읽어서 파일에 저장
# for(임시변수 in 컬렉션이름){}
# ★ 중요(페이지 내 기사 크롤링하는 방법)
for(addr in k){                                         # 첫 번째 URL(k)을 꺼내서 addr 에 할당
  temp <- read_html(addr) %>% html_nodes(".text") %>%  # 그래서 그 주소로 다시 읽어들인다.(첫 번째 기사를 읽음) %>%
                                                       # 그 결과를 .text에 넘기면 클래스 속성값이 text인 것만 읽음
    html_text()                                        # 시작/끝태그가 text인 것만 읽어서 temp 에 저장 
  cat(temp, file="temp.txt", append=TRUE)             # temp가 갖고있는 값을 temp.txt에다가 계속 추가하겠다.
}
# 다시 두번째를 읽어서 반복하고 temp.txt에 append 덧붙여서 쓰여진다. 그래서 계속 추가 추가 추가 반복

# 9. 파일의 모든 내용 가져오기 
txt <- readLines("temp.txt")
head(txt)

# 10. 명사만 추출
useNIADic() # 세종사전보다 많은 단어 포함 
nouns <- extractNoun(txt)  # 명사들만 추출
nouns

# 11. 빈도수 만들기 - 각 단어가 몇 번씩 나왔는지
wordcount <- table(unlist(nouns)) # 리스트를 풀어주는 함수 unlist
wordcount
class(wordcount) # table
 
# 12. 데이터프레임으로 변환
df_word <- as.data.frame(wordcount, stringsAsFactors = F)
df_word
class(df_word) # data.frame

# 13. 필터링
df_word <- filter(df_word, nchar(Var1) >= 2)

# 14. 워드클라우드 색상 판 생성
pal <- brewer.pal(8, "Dark2")

# 15. 시드 설정
set.seed(1234)

# 16. 워드 클라우드 생성
wordcloud(words=df_word$Var1,
          freq=df_word$Freq,
          min.freq = 2, max.words = 200,
          random.order = F,
          rot.per = .1, scale=c(4,0.3),
          colors=pal)


#######################################################동아일보 태그
# http://news.donga.com/search?p=1&query=코로나19&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1
# http://news.donga.com/search?
# p=1&
# query=코로나19&
# check_news=1&
# more=1&
# sorting=1&
# search_date=1&
# v1=&
# v2=&
# range=1

url <- 'http://news.donga.com/search?p=1&query=코로나19&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'

k <- read_html(url, encoding="utf-8") # url 에 있는 값을 UTF-8 방식으로 읽어와서 k변수에 저장 
k

# 7. dt 태그 안에 있는 a 태그 들의 href 속성의 값을 가져오기
k <- k %>%              # href 가 a태그 안에 있고, 기사 제목들에 관련된 a태그는 dt태그 
  html_nodes(".txt") %>% # 내부에 있기 때문에 전체 페이지에서 %>% dt 시작태그와 닫는 태그를 모두 찾아온다.
  html_nodes("a") %>%  # 그 결과값을 다시 html_nodes 함수에 전달하면 dt 태그 사이에서 a 태그만 다시 추출 
  html_attr("href")
k

# 8. k에 저장된 모든 URL 에 해당하는 데이터의 클래스가 text인 데이터를 읽어서 파일에 저장
# for(임시변수 in 컬렉션이름){}
# ★ 중요(페이지 내 기사 크롤링하는 방법)
for(addr in k){                         
  temp <- read_html(addr) %>% html_nodes(".article_txt") %>%
    html_text()                                       
  cat(temp, file="temp2.txt", append=TRUE)      
}
# 다시 두번째를 읽어서 반복하고 temp.txt에 append 덧붙여서 쓰여진다. 그래서 계속 추가 추가 추가 반복

# 9. 파일의 모든 내용 가져오기 
txt <- readLines("temp2.txt")
head(txt)

# 10. 명사만 추출
useNIADic() # 세종사전보다 많은 단어 포함 
nouns <- extractNoun(txt)  # 명사들만 추출
nouns

# 11. 빈도수 만들기 - 각 단어가 몇 번씩 나왔는지
wordcount <- table(unlist(nouns)) # 리스트를 풀어주는 함수 unlist
wordcount
class(wordcount) # table

# 12. 데이터프레임으로 변환
df_word <- as.data.frame(wordcount, stringsAsFactors = F)
df_word
class(df_word) # data.frame

# 13. 필터링
df_word <- filter(df_word, nchar(Var1) >= 2)

# 14. 워드클라우드 색상 판 생성
pal <- brewer.pal(8, "Dark2")

# 15. 시드 설정
set.seed(1234)

# 16. 워드 클라우드 생성
wordcloud(words=df_word$Var1,
          freq=df_word$Freq,
          min.freq = 2, max.words = 200,
          random.order = F,
          rot.per = .1,
          scale=c(4,0.3),
          colors=pal)

#########################################
# R 키보드를 이용한 데이터 입력

# c() 함수를 이용한 데이터 입력
# x <- c(10.4, 5, 6, 3.1, 6.4, 21.7)
# x
# [1] 10.4, 5.6, 3.1, 6.4, 21.7

# scan() 함수는 외부의 텍스트파일을 불러올 때 외에도 키보드 입력에도 이용할 수 있는 함수이며, 일반적으로 R Console 에서 프롬프트가
# [1]과 같이 보여지나, scan() 함수를 실행할 경우는 '1:'과 같은 형태로 출력된다.

# scan() 함수 이용
x <- scan()

# console 에서 입력
# 1: 24
# 2: 75
# 3: 36
# 4:
# Read 3 items

x <- scan(what=" ")
# console에서 입력
x

# edit() 함수는 데이터 편집기 창을 직접 띄워
# 데이터를 직접 입력하는 방식으로
# 편집기는 셀의 형식을 띄고 있으며,
# 각 셀에 데이터를 입력한 후 수정할 경우는
# 메뉴에서 <편집> - <데이터 편집기>를 선택하여 수정할 수 있다.

# edit() 함수를 이용하여 데이터 입력기를 호출한 후 데이터를 입력한다.

age = data.frame()
age = edit(age)
age

library(KoNLP)
library(wordcloud)
library(stringr)

useSejongDic()
#정규표현식 예
text <- c("phone:010-1234-5678",
          "home:02-123-1234",
          "이름:홍길동")

grep("[[:digit:]]",text, value=T)# ■ 텍스트라는 변수가 가진 것 중 숫자들이 포함된것들만 추출해달라 : grep 함수
#---------------------------------------
# [1] "phone:010-1234-5678" "home:02-123-1234"
#---------------------------------------

gsub("[[:digit:]]","x",text) # 숫자부분을 x 표시로 바꿔달라고 요청

# 한글 문자열분석에서 매우 중요한 정규표현식.
grep("[가-힣]", text, value=T)

# 영문 소문자가 포함된 것들만 출력 요청
grep("[[:lower:]]", text, value=T)

# 정수로 쓴 표현만 인식
# 1~9로 시작하는 숫자로 되어있는 애들을 " "로 교체하라는 의미
gsub("^[1-9][0-9]*$", " ", c("08","1","19 189", "78")) 

# 소수점 넣는 방법
gsub("^[0-9]+(\\.[0-9]{1,2})?$",
     "zz",
     c("123","123.17","123.456","123.","12.79"))

# 블로거들이 추천하는 서울 명소 분석하기
# "seoul_go.txt" 파일을 사용하여 블로거들이 추천하는 서울 명소들을 워드 클라우드로 생성
# (서울 명소추가: 서울명소merge.txt)
# (제거단어 : 서울명소gsub.txt)

# setwd("c:\\r_temp")
# 필요 패키지를 설치하는데 이미 설치가 되어 있어서 경고가 나오니 무시하세요.
install.packages("KoNLP")
install.packages("wordcloud")
install.packages("stringr")

library(KoNLP)
library(wordcloud)
library(stringr)

useSejongDic()

# 사전에 추가시키려면 반드시 데이터프레임으로 되어있어야 한다.
# ncn은 형태소를 보면 위치값 key들이 다 들어 있다.(일반명사 들어가는 위치값, 고유명사 들어가는 위치값 등)
mergeUserDic(data.frame(readLines("./Data6_prj/서울명소merge.txt"),"ncn"))
txt <- readLines("./Data6_prj/seoul_go.txt")

place <- sapply(txt,extractNoun,USE.NAMES = F)

head(place,10)
head(unlist(place),30)

c <- unlist(place)
res <- str_replace_all(c, "[^[:alpha:]]", "") #알파벳으로 된 것들을 공백없는것으로 바꿔치기

txt <- readLines("./Data6_prj/서울명소gsub.txt")
txt
cnt_txt <- length(txt)
cnt_txt

for( i in 1:cnt_txt){
  res <- gsub((txt[i]),"",res)
}

res2 <- Filter(function(x) {nchar(x)>=2},res)
nrow(res2)

write(res2, "./result_files/seoul_go2.txt")

res3 <- read.table("./result_files/seoul_go2.txt")

wordcount <- table(res3)
head(sort(wordcount, decreasing = T),30)

library(RColorBrewer)
palete <- brewer.pal(8,"Set2")

wordcloud(names(wordcount),
          freq=wordcount,
          scale=c(3,1),
          rot.per = 0.25,
          min.freq = 5,
          random.order = F,
          random.color = T,
          colors = palete)

legend(0.3,
       1,
       "블로거 추천 서울 명소 분석",
       cex=0.6,
       fill=NA,
       border=NA,
       bg="white",
       text.col="red",
       text.font=2,
       box.col="red")

