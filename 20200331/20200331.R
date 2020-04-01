as.Date("2020년 11월 1일", format="%Y년 %m월 %d일")
#[1] "2020-11-01"

x <- as.Date("01-11-2020",format="%d-%m-%Y")

as.Date("2014-11-30") - as.Date("2014-11-01") # Time difference of 29 days
as.Date("2014-11-01")+5 #[1] "2014-11-06"

x <- c(9, 15, 20, 6)
label <- c("영업 1팀","영업 2팀","영업 3팀","영업 4팀")
pie (x, labels = label, main = "부서별 영업 실적")

View(x) # 강제로 표 형식으로 보여주게 하는 방법

# 12시 방향을 기준으로 파이차트 재생성
pie(x, init.angle = 90, labels = label, main = "부서별 영업 실적")

#색과 라벨 수정
pct <- round(x/sum(x)*100) # x의 각 요소들 / x모두 더한 값 * 100 -> 반올림
label <- paste(label, pct) # paste 함수 : R에서 문자와 숫자를 연결시키려면 paste 함수로 연결시켜야 한다. # 영업 1팀 18
label <- paste(label,"%",sep="") # 각 '라벨+숫자'에 %를 붙여준다.(띄어쓰기 없게 붙인다.) # 영업 1팀 18%
pie(x,
    labels = label,
    init.angle = 90,
    col=rainbow(length(x)),
    main="부서별 영업 실적")

# 3D 파이 차트
install.packages("plotrix")
library(plotrix)

pie3D(x, labels=label, explode = 0.1,
      labelcex = 0.8, main="부서별 영업 실적") # 옵션 순서는 변경되어도 상관 없음(데이터 위치 제외)
# explode 는 쪼개지는 비율, labelcex 는 글자 크기에 대한 비율

#기본 바 차트 출력
height <- c(9, 15, 20, 6)
name <- c("영업 1팀", "영업 2팀", "영업 3팀", "영업 4팀")
barplot(height, names.arg = name, main="부서별 영업 실적") # 차트의 데이터값은 항상 제일 먼저 와야한다.

# 막대의 색 지정
barplot(height, names.arg = name, main = "부서별 영업 실적", col=rainbow(length(height)))

barplot(height, names.arg = name, main = "부서별 영업 실적", col=rainbow(length(height)),
        xlab="부서", ylab="영업 실적(억)", ylim=c(0,25))
# x, ylab : 축 이름, ylim : 축의 시작과 끝 지점 설정

#차트 위치에 데이터 값 할당하기(변수에 한번 저장해서 사용해야 한다.)
bp <- barplot(height, names.arg = name, main = "부서별 영업 실적적", col=rainbow(length(height)),
              xlab="부서", ylab="영업 실적(억)", ylim=c(0,25))
text(x=bp, y=height, labels = round(height, 0), pos=1)
# labels = round(height,0)은 소수점 밑 자리수 0자리까지 표시
# pos = 3 은 포지션의 약자

# 바 차트의 수평 회전(가로 막대)
barplot(height, names.arg =name, main="부서별 영업 실적", col=rainbow(length(height)),
        xlab="영업 실적(억)", ylab="부서", horiz=TRUE, width=50) # width 는 막대의 두께를 말한다.

  
# 스택형 바 차트 (Stacked Bar Chart)
height1 <- c(4, 18, 5, 8)
height2 <- c(9, 15, 20, 6)
height3 <- c(3, 10, 15, 8)
height <- rbind(height1, height2, height3) # rbind 행 묶기 -> 표 형태로 묶인다.
View(height) # Environment 에서 클릭하면 바로 View 형태로 보여지기 때문에 굳이 사용할 필요는 없다.

name <- c("영업 1팀","영업 2팀","영업 3팀","영업 4팀")
legend_lbl <- c("2014년", "2015년", "2016년") # 범례를 만들기 위한 라벨

barplot(height, # 입력될 데이터
        main="부서별 영업 실적", # 차트 제목
        names.arg=name, #막대별 이름 설정
        xlab="부서", ylab="영업 실적(억)", # 축 이름 설정
        col = c("darkblue", "red", "yellow"), # 바의 색상 지정
        legend.text=legend_lbl, # 범례지정 = 입력해놓은 라벨 할당
        ylim=c(0,50)) # y축에 대한 시작, 종료 값

# 그룹형 바 차트 (Grouped Bar Chart)
barplot(height, main="부서별 영업 실적",
        names.arg=name,
        xlab="부서", ylab="영업 실적(억)",
        col = c("darkblue", "red", "orange"),
        legend.text=legend_lbl,
        ylim=c(0,50),
        beside=TRUE,
        args.legend=list(x='topright')) # bottom, topleft 이런식으로 범례 위치 지정 가능

# 일반적인 X-Y 플로팅
View(women)

weight <- women$weight
plot(weight)

height <- women$height
plot(height, weight, xlab="키", ylab="몸무게")


# 일반적인 X-Y 플로팅
View(women)

weight <- women$weight
plot(weight)

height <- women$height
plot(height,weight,xlab="키",ylab="몸무게")

# 플로팅 문자의 출력
plot(height,weight,xlab="키",ylab="몸무게",pch=23,col="blue",bg="yellow",cex=1.5)

# 지진의 강도에 대한 히스토그램
head(quakes)

mag <- quakes$mag
mag

hist(mag,
     main="지진 발생 강도의 분포",
     xlab="지진 강도", ylab="발생 건수")


# 계급 구간과 색
colors <- c("red", "orange", "yellow", "green", "blue", "navy", "violet")

hist(mag,
     main = "지진 발생 강도의 분포",
     xlab = "지진 강도", ylab="발생 건수",
     col=colors,
     breaks=seq(4,6.5,by=0.5)) # 4부터 6.5까지 0.5단계별로 나눈다.

#확률 밀도
hist(mag,
     main = "지진 발생 강도의 분포",
     xlab = "지진 강도", ylab="확률밀도",
     col=colors,
     breaks=seq(4,6.5,by=0.5),
     freq=FALSE)

lines(density(mag)) # 확률 밀도 함수 : density 함수

#박스 플롯
mag <- quakes$mag
min(mag) # 4
max(mag) # 6.4
median(mag) # 4.6
quantile(mag, c(0.25, 0.5, 0.75)) # 4.3, 4.6, 4.9 (1,2,3분위수)

boxplot(mag,
       main = "지진 발생 강도의 분포",
       xlab = "지진 강도", ylab="확률밀도",
       col="red")
# 이상치는 결측값이지만 연산에 포함된다. na.rm=TRUE 을 해서 null값을 삭제해줘야 한다.(결측치 삭제, 결측값 삭제)


# 지역별 순이동에 따른 워드 클라우드 (실행 시킬 때, 따로따로 실행 시켜야 한다.) / install 끝난 후 라이브러리 실행
install.packages("wordcloud")
library(wordcloud)

word <- c("인천광역시", "강화군", "옹진군")
frequency <- c(651, 185, 61)

# 단어와 노출 빈도수를 임의로 설정하였다.
# 첫 번째 값은 표현할 단어들, 두 번째 값이 각 단어에 대한 노출 빈도 수, 나머지는 옵션
wordcloud(word, frequency, colors="blue")


#단어들의 색 변환
wordcloud(word,
          frequency,
          random.order = F,
          ramdom.color = F,
          colors = rainbow(length(word))
          )

#다양한 단어 색 출력을 위한 파레트 패키지의 활용
install.packages("RColorBrewer")
library(RColorBrewer)

pal2 <- brewer.pal(8, "Dark2")

word <- c("인천광역시", "강화군", "옹진군")
frequency <- c(651, 86, 61)
wordcloud(word, frequency, colors=pal2)


# 다운로드 사이트 : http://kostat.go.kr

# 작업 순서
# 1. 데이터 파일 읽기 : 6_101_DT_1B26001_A01_M.csv
# 2. '전국' 지역이 아닌 데이터만 추출
# 3. 행정구역 중 '구' 단위에 해당하는 행 번호 추출
# 4. '구' 지역 데이터 제외
# 5. 순이동 인구수가 0보다 큰지역 추출 
# 6. 단어(행정 구역) 할당
# 7. 워드클라우드 출력

# 1. 데이터 파일 읽기 : read.csv(file.choose(), header=T)
# 2. '전국' 지역이 아닌 데이터만 추출('전국' 지역 데이터 제외) : data[data$행정구역.시군구.별 != "전국", ]
# 3. 행정구역 중 '구' 단위에 해당하는 행 번호 추출 : grep("구$", data2$행정구역.시군구.별)
# 4. '구' 지역 데이터 제외 : <- data2[-c(x), ]
# 5. 순이동 인구수가 0보다 큰지역 추출 : data3[data3$순이동.명>0, ]
# 6. 단어(행정 구역) 할당 : data4$행정구역.시군구.별
# 7. 행정구역별 빈도 : data4$순이동.명
# 8. 워드클라우드 출력 : wordcloud()

data <- read.csv(file.choose(), header=T) # 모든 괄호가 .으로 변경된다.
View(data)
head(data) # read 가 끝나야 head를 사용할 수 있다.
names(data) # 데이터의 컬럼 확인

# ()가 R에서는 모두 .으로 바뀌어서 들어온다.
data2 <- data[data$행정구역.시군구.별 != "전국", ] # 전체 데이터$컬럼명 중에서 != "전국" 데이터가 아닌 것만 모두 선택
x <- grep("구$", data2$행정구역.시군구.별) # grep함수 : 지정 조건에 맞는 '행 번호'를 벡터로 반환(x: 구 관련 행번호만 저장)
data3 <- data2[-c(x), ] # '구' 지역 데이터 제외
head(data3)

data4 <- data3[data3$순이동.명>0, ] # data3중 순이동.명 컬럼 중 0보다 큰애들만 추출
head(data4)
word <- data4$행정구역.시군구.별 # 워드클라우드작업을 위한 글자 데이터만 추출
frequency <- data4$순이동.명 # 숫자값으로 작업할 숫자 데이터만 추출

library(wordcloud)
library(RColorBrewer)

pal2 <- brewer.pal(8, "Dark2")
wordcloud(word,frequency, colors=pal2)



