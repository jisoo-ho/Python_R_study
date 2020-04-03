# 데이터 로드
twitter <- read.csv("C:/rStudy/20200403/twitter.csv",
                    header=T,
                    stringsAsFactors = F,
                    fileEncoding = "UTF-8")
head(twitter)
dim(twitter) # 3743 5
class(twitter) #data.frame"
summary(twitter)

twitter <- rename(twitter,
                  no = 번호,
                  id = 계정이름,
                  date = 작성일,
                  tw = 내용)
head(twitter)
names(twitter)#[1] "X"    "no"   "id"   "date" "tw"  

# 특수문자 제거
twitter$tw <- str_replace_all(twitter$tw, "\\W", " ")
head(twitter$tw)

# 단어 빈도표 만들기
# 트윗에서 명사 추출
nouns <- extractNoun(twitter$tw)

class(nouns) # list
dim(nouns) # NULL
str(nouns)

# 단어 빈도표 만들기
# 트윗에서 명사 추출
nouns <- extractNoun(twitter$tw)
head(nouns)

# 추출한 명사 list를 문자열 벡터로 변환, 단어별 빈도표 생성
wordcount <- table(unlist(nouns))
head(wordcount)

# 데이터프레임으로 변환
df_word <- as.data.frame(wordcount, stringsAsFactors = F)
head(df_word)

names(df_word) # "Var1" "Freq"

####### 실습
# 변수명 수정
df_word <- rename(df_word,
                  word = Var1,
                  freq = Freq)

# 세 글자 이상 단어 추출
df_word <- filter(df_word, nchar(word) >= 3) # df_word 에서 word 컬럼 데이터 중에 글자의 개수가 3개 이상인 것만 filter로 걸러낸다.
class(df_word) # data.frame
dim(df_word)  # 4921 2
summary(df_word)


#빈도수를 기준으로 빈도수가 높은 상위 50개만 꺼내온다.(freq 컬럼을 이용해서 내림차순으로 정렬)
top_40 <- df_word %>% 
  arrange(desc(freq)) %>% 
  head(40)
class(top_40)
dim(top_40)
summary(top_40)
str(top_40)

# 패키지 준비하기
# 패키지 설치(로드 먼저 해보고 설치)
install.packages("wordcloud")

#패키지 로드
library(wordcloud)
library(RColorBrewer)

# 단어 색상 목록 만들기
pal <- brewer.pal(8, "Dark2") # Dar2 색상 목록에서 8개 색상 추출

set.seed(1234)                  #난수 고정
wordcloud(words= top_40$word,   # 단어
          freq = top_40$freq,   # 빈도
          min.freq = 2,         # 최소 단어 빈도
          max.words = 200,      # 표현 단어 수
          random.order = F,     # 고빈도 단어 중앙 배치
          rot.per = .1,         # 회전 단어 비율
          scale = c(4, 0.4),    # 단어 크기 범위
          colors = pal)         # 색상 목록


#단어 빈도 막대 그래프 만들기
library(ggplot2)

order <- arrange(top_40,freq)$word            #빈도 순서 변수 생성

ggplot(data = top_40,aes(x = word, y = freq))+
  ylim(0,1000)+
  geom_col()+
  coord_flip()+
  scale_x_discrete(limit = order)+          # 빈도 순서 변수 기준 막대 정렬
  geom_text(aes(label=freq),hjust = -0.3)   # 빈도 표시

################### 워드클라우드 2 사용
# 패키지 로드
library(devtools)
library(htmlwidgets)
library(htmltools)
library(jsonlite)
library(yaml)
library(base64enc)
library(tm)
install.packages("tm")
library(wordcloud2)
install.packages("wordcloud2")

# 특정 개수 이상 추출되는 글자만 색깔을 변경하여 나타나도록
# https://html-color-codes.info/Korean/

# 사이값 지정시 : (weight > 800 && weight < 1000)
# 100개 이상 검색될 시 노랑, 아니면 초록으로 표현
In_out_colors = "function(word, weight){
                    return (weight > 100) ? '#F3EF12' : '#1EC612'}"
# 여기서 쓰인 코드는 자바스크립트 코드임. function에서 word 랑 weight 라는 매개변수가 들어가 있는 것.
# 워드클라우드를 사용하려면 함수 자체를 변수에 대입시켜놔야 한다.
# 나중에 호출할 때는 In_out_colors 라는 함수를 호출하는 것

# 3. 워드 클라우드 그리기(기본)
wordcloud2(top_40)

# 3.1 wordcloud2 크기, 색 변경(size, color)
wordcloud2(top_40, size=0.5, col="random-dark")

# 3.2 키워드 회전 정도 조절(rotateRatio)
wordcloud2(top_40, size=0.5, col="random-dark", rotateRatio=0)

# 3.3 배경 색 검정(backgroundColor)
wordcloud2(top_40, size=0.5, col="random-light", backgroundColor = "black")

# 기존 모형으로 wordcloud2 생성
# 모양 선택 : shape = 'circle', 'cardioid',
#                      'diamond', 'triangle-forward',
#                      'triangle', 'pentagon', 'star'

wordcloud2(df_word,
           shape='pentagon',
           size=0.8,
           color = htmlwidgets::JS(In_out_colors),
           backgroundColor = "black")

# 단계 구분도(Choropleth Map)
# - 지역별 통계치를 색깔의 차이로 표현한 지도
# - 인구나 소득 같은 특성이 지역별로 어람나 다른지 쉽게 이해할 수 있음

install.packages("ggiraphExtra")
library(ggiraphExtra)

str(USArrests)
head(USArrests)

library(tibble) # 행 이름을 변수로 바꿔 데이터 프레임 생성을 편하게 해주는 라이브러리

# 행 이름을 state 변수로 바꿔 데이터 프레임 생성
crime <- rownames_to_column(USArrests, var="state")
View(USArrests)
# 지도 데이터와 동일하게 맞추기 위해 state 의 값을 소문자로 수정
crime$state <- tolower(crime$state) # 주 이름들이 첫글자가 대문자로 되어있다.( 얘들을 전부 소문자로 바꾼다. ) 반대는 toupper()

# tibble(티블)은
# 행 이름을 가질 수 있지만(예: 일반 데이터 프레임에서 변환할 떄)
# [연산자로 서브 셋팅할 때 제거됩니다.]
# 
# NULL 이 아닌 행 이름을 티블에 지정하려고 하면 경고가 발생합니다
# 일반적으로 행 이름은 기본적으로 다른 모든 열과
# 의미가 다른 문자열이므로 행 이름을 사용하지 않는 것이 가장 좋습니다.
# 
# 이러한 함수를 사용하면
# 데이터프레임에 행 이름(has_rownames())이 있는지 감지하거나,
# 제거하거나(remove_rownames())
# 명시적 열(rownames_to_column()및 column_to_rownames()) 사이에서 앞뒤로 변환할 수 있습니다.
# rowid_to_column() 도 포함되어 있습니다.
# 
# 이것은 1부터 시작하여 순차적인 행 ID를 오름차순으로 하는 데이터 프레임의 시작 부분에 열을 추가합니다.
# 기존 행 이름이 제거됩니다.

#미국 주 지도 데이터 준비하기
library(ggplot2)
install.packages("maps")
states_map <- map_data("state")
str(states_map) # 해당 주에 대한 위도 경도값을 경계로 다 끊어놓음
# 불러들인 지도를 가지고 파트를 그려 나간다. 그 중 범죄에 해당하는 3개 컬럼을 사용(UrbanPop 은 경관 수)

install.packages("mapproj") #ggChoropleth 메소드 사용할 패키지 설치
ggChoropleth(data = crime,            # 지도에 표현할 데이터
             aes(fill=Murder,         # 색깔로 표현할 변수
                 map_id=state),       # 지역 기준 변수
             map=states_map)          # 지도 데이터

ggChoropleth(data = crime,            # 지도에 표현할 데이터
             aes(fill=Rape,           # 색깔로 표현할 변수
                 map_id=state),       # 지역 기준 변수
             map=states_map,          # 지도 데이터
             interactive = T)         # 인터랙티브


install.packages("stringi")

install.packages("devtools")
devtools::install_github("cardiomoon/kormaps2014")
library(kormaps2014)

str(changeCode(korpop1))

library(dplyr)
korpop1 <- rename(korpop1,
                  pop = 총인구_명,
                  name = 행정구역별_읍면동)
str(changeCode(kormap1))

# 단계 구분도만들기
ggChoropleth(data = korpop1,       # 지도에 표현할 데이터
             aes(fill = pop,       # 색깔로 표현할 변수
                 map_id = code,    # 지역 기준 변수
                 tooltip = name),  # 지도 위에 표시할 지역명
             map = kormap1,        # 지도 데이터
             interactive = T)      # 인터랙티브

#대한민국 시도별 결핵 환자 수 단계 구분도 만들기
str(changeCode(tbc))

#인터랙티브 단계 구분도 만들기
ggChoropleth(data= tbc,         # 지도에 표현할 데이터
             aes(fill=NewPts,   # 색깔로 표현할 변수
                 map_id=code,   # 지역기준 변수
                 tooltip=name), # 지도위에 표시할 지역명
             map=kormap1,       # 지도데이터
             interactive = T)   # 인터랙티브

# 패키지 설치 : 인터랙티브 그래프 만들기
install.packages("plotly")
library(plotly)

# ggplot 으로 그래프 만들기
library(ggplot2)
p <- ggplot(data = mpg, aes(x = displ, y = hwy, col = drv)) + geom_point()

# 인터랙티브 그래프 만들기
ggplotly(p)
# https://plotly.com/ : 패키지 설명 사이트

# 인터랙티브 막대 그래프 만들기
p <- ggplot(data = diamonds, aes(x=cut, fill = clarity))+
  geom_bar(position = "dodge")

ggplotly(p)


install.packages("dygraphs")
library(dygraphs)

# 데이터 준비하기 ( 인구대비 실업률 )
economics <- ggplot2::economics
head(economics)


library(xts)
eco <- xts(economics$unemploy, order.by = economics$date)  # 실업자수를 정렬시키겠다. 날짜컬럼을 기준으로
head(eco)

#그래프 생성
dygraph(eco)

# 날짜 범위 선택 기능
dygraph(eco) %>% dyRangeSelector()


# 여러 값 표현하기
# 저축률
eco_a <- xts(economics$psavert, order.by = economics$date)

# 실업자 수
eco_b <- xts(economics$unemploy/1000, order.by = economics$date)

# 합치기
eco2 <- cbind(eco_a, eco_b)                   # 데이터 결합합
colnames(eco2) <- c("psavert", "unemploy")    # 변수명 바꾸기
head(eco2)


# 그래프 만들기
# https://dygraphs.com/ : 패키지 제작 사이트
dygraph(eco2) %>% dyRangeSelector()


mpg <- as.data.frame(ggplot2::mpg)
str(mpg)

library(dplyr)

mpg_diff <- mpg %>% 
  select(class, cty) %>%  #select : 전체 데이터를 갖고 있는 mpg를 이용하여 두가지 컬럼 값을 선택
  filter(class %in% c("compact","suv")) #filter : 행 선택 // %in% : 값 매칭 추출해주는 연산

head(mpg_diff)


# t-test
t.test(data=mpg_diff, cty~class, var.equal=T)

#p-value : 유의확률값
#mean in group compact : compact 에 대한 평균값
#mean in group suv : suv에 대한 평균값
#alternative hypothesis: true difference in means is not equal to 0
# : 대립가설이 0과 같지 않다면 평균값 신뢰 불가
#95 percent confidence interval : 유의한 값 / 신뢰기간이 5.525180~7.730139
# 일반 휘발유와 고급 휘발유의 도시 연시 t 검정

# 데이터 준비
mpg_diff2 <- mpg %>%
  select(fl, cty) %>% #휘발유 컬럼과 도시연비를 뽑아냄
  filter(fl %in% c("r","p")) #r:regular(일반휘발유), p:premium(고급휘발유)

table(mpg_diff2$fl)

# 일반휘발유 : 168, 고급휘발유 : 52
t.test(data=mpg_diff2, cty~fl, var.equal = T)


# 상관분석 - 두 변수의 관계성 분석 (변수 : R에서는 컬럼명)
# 상관분석(Correlation Analysis)
#- 두 연속 변수가 서로 관련이 있는지 검정하는 통계 분석 기법
#- 상관계수(Correlation Coefficient)
# --> 두 변수가 얼마나 관련되어 있는지, 관련성의 정도를 나타내는 값
# --> 0~1 사이의 값을 지니고 1에 가까울수록 관련성이 크다는 의미
# --> 상관계수가 양수면 정비례, 음수면 반비례 관계

# 상관관계 예시
# cctv와 범죄발생율 상관관계
# 복지 패널 데이터를 이용해 급여와 우리 삶에 관한 상관관계
# 종교와 이혼율에 상관관계

#실업자 수와 개인 소비 지출의 상관관계

#데이터 준비
economics <- as.data.frame(ggplot2::economics)

#상관분석
cor.test(economics$unemploy, economics$pce) #unemploy : 실업자수와 pce : 개인소비지출의 상관관계

head(mtcars)


#상관행렬 만들기 ★★★ 이 내용을 잘 알고 있어야 파이썬 딥러닝에서 image 분석이 들어감 - 텐서플로우
car_cor <- cor(mtcars) #상관행렬 생성
head(car_cor) #먼저 데이터 확인 후 round 작업 해주기

round(car_cor, 2) #소수점 셋째 자리에서 반올림해서 출력

install.packages("corrplot")
library(corrplot)

corrplot(car_cor)

#원 대신 상관계수 표시 / 원이 아닌 숫자값으로 출력하고 싶을시
corrplot(car_cor, method="number")

#다양한 파라미터 지정하기 / 원도 상관계수도 아닌, 색상으로 네모칸 채우고 싶을 때
col <- colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))

#색상 팔레트로 색상 직접 지정 / 색상 팔레트 만들시 색상 하나는 있어야함
#얘네가 만들어낸 다섯가지 색상을 지정해주고 그 사이사이는 200가지 색상이 들어감


corrplot(car_cor,
         method="color", #색깔로 표현
         col = col(200), #색상 200개 선정
         type="lower", #왼쪽 아래 행렬만 표시
         order = "hclust", #유사한 상관계수끼리 군집화
         addCoef.col="black", #상관계수 색깔
         tl.col="black", #변수명 색깔
         tl.srt=45, #변수명 45도 기울임
         diag=F) #대각 행렬 제외
