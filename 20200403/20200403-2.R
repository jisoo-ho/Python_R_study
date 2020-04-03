#패키지 설치
install.packages("rJava")
install.packages("memoise")
install.packages("KoNLP")
#########라이브러리 로드 해보고 없으면 인스톨

#패키지 로드
library(KoNLP)
library(dplyr)

#패키지 로드 에러 발생할 경우 - java 설치 경로 확인 후 경로 설정
# java 폴더 경로 설정
Sys.setenv(JAVA_HOME="C:/Program Files/Java/jdk1.8.0_171")

#사전 설정하기
useNIADic()

#데이터 준비
#데이터 불러오기
txt <- readLines("C:/rStudy/20200403/remake.txt")

head(txt)

#특수문자 제거
install.packages("stringr")

#일단 먼저 로드 해보고 없으면 인스톨 하기
library(stringr)

#특수문자 제거
txt <- str_replace_all(txt, "\\W", " ") # 모든 특수기호를 찾아서 공백 처리 # gsub 함수와 동일한 역할을 해준다.
head(txt)

class(txt) # character 문자열 확인
dim(txt) # NULL 확인

View(txt) 


#가장 많이 사용된 단어 알아보기

#고민글에서 명사추출
nouns <- extractNoun(txt)
class(nouns) # list
dim(nouns) # NULL
View(nouns)

# 추출한 명사 list를 문자열 벡터로 변환, 단어별 빈도표 생성
# 리스트타입은 테이블 함수 사용 못한다. 그래서 리스트를 풀어줘야 한다. 이 때, 사용하는 함수가 [unlist] 함수
wordcount <- table(unlist(nouns))
class(wordcount) # table

# 자주 사용된 단어 빈도표 만들기
df_word <- as.data.frame(wordcount, stringsAsFactors = F) # wordcount(스트링)의 팩터값을 없앤다, 데이터프레임으로 변환한다.
class(df_word) # data.frame
dim(df_word) 
summary(df_word)

# 변수명 수정
df_word <- rename(df_word,
                  word = Var1,
                  freq = Freq)

# 두 글자 이상 단어 추출
df_word <- filter(df_word, nchar(word) >= 2) # df_word 에서 word 컬럼 데이터 중에 글자의 개수가 2개 이상인 것만 filter로 걸러낸다.
class(df_word) # data.frame
dim(df_word) 
summary(df_word)


#빈도수를 기준으로 빈도수가 높은 상위 50개만 꺼내온다.(freq 컬럼을 이용해서 내림차순으로 정렬)
top_50 <- df_word %>% 
  arrange(desc(freq)) %>% 
  head(50)
class(top_50)
dim(top_50)
summary(top_50)
str(top_50)

# 패키지 준비하기
# 패키지 설치(로드 먼저 해보고 설치)
install.packages("wordcloud")

#패키지 로드
library(wordcloud)
library(RColorBrewer)

# 단어 색상 목록 만들기
pal <- brewer.pal(8, "Dark2") # Dar2 색상 목록에서 8개 색상 추출

set.seed(1234)                  #난수 고정
wordcloud(words= df_word$word,   # 단어
          freq = df_word$freq,   # 빈도
          min.freq = 2,         # 최소 단어 빈도
          max.words = 200,      # 표현 단어 수
          random.order = F,     # 고빈도 단어 중앙 배치
          rot.per = .1,         # 회전 단어 비율
          scale = c(4, 0.5),    # 단어 크기 범위
          colors = pal)         # 색상 목록
