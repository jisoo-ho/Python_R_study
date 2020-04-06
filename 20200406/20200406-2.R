###############################################################
# "제주도 여행코스 추천" 검색어 결과를 그래프로 표시
###############################################################
# 단어 추가(제주도여행지.txt)를 읽어들인 후, dataframe 으로 변경하여 기존 사전에 추가.
# 데이터 읽어오기 (jeju.txt)
# 한글 외 삭제, 영어
# 읽어들인 데이터로부터 제거할 단어 리스트 읽어오기(제주도 여행코스gsub.txt)
# 두 글자 이상인 단어만 추출
# 현재까지의 작업 파일을 파일로 저장 후, 저장된 파일 읽기
# 단어 빈도 수 구한 후, 워드 클라우드 작업
###############################################################
# 가장 추천 수가 많은 상위 10개를 골라서
# 1. pie 그래프로 출력
# 2. bar 형태의 그래프로 표시하기
# 3. 옆으로 누운 바 그래프 그리기
# 4. 3D Pie Chart 로 표현(plotrix 라는 패키지가 추가로 필요)

rm(list=ls()) # R 스튜디오에 있는 모든 변수를 제거하는 함수 remove 함수

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
mergeUserDic(data.frame(readLines("./Data6_prj/제주도여행지.txt"),"ncn"))

txt <- readLines("./Data6_prj/jeju.txt")
head(txt)

c <- unlist(place)
res <- str_replace_all(c, "[^[:alpha:]]", "") #알파벳으로 된 것들을 공백없는것으로 바꿔치기

place <- sapply(txt,extractNoun,USE.NAMES = F)
place <- gsub(" ","", place)

txt <- readLines("./Data6_prj/제주도여행코스gsub.txt")
txt
cnt_txt <- length(txt)
cnt_txt

for( i in 1:cnt_txt){
  res <- gsub((txt[i]),"",res)
}

res2 <- Filter(function(x) {nchar(x)>=2},res)
nrow(res2)

write(res2, "./result_files/jeju2.txt")

res3 <- read.table("./result_files/jeju2.txt")

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

#####################차트그리기
# head(상위 10개 추출) 여행지 탑텐 저장(df)
top10 <- head(sort(wordcount, decreasing = T),10) 

pie(top10, col=rainbow(10), radius=1, init.angle = 90, main = "여행 추천지 top 10")

# 수치값을 함께 출력하기
# 출력값 계산
pct <- round(top10/sum(top10) *100, 1)
names(top10)

# 지명과 계산 결과를 합하기
lab <- paste(names(top10), "\n", pct, "%")
# 퍼센트 값 붙은 파이차트 출력하기
pie(top10, col=rainbow(10), cex=0.8, labels=lab, init.angle = 90, main = "여행 추천지 top 10")

# bar 형태의 그래프 표시하기
bchart <- head(sort(wordcount, decreasing = T),10)
bchart

bp <- barplot(
  bchart,
  main="제주도 추천 여행 코스 TOP 10",
  col = rainbow(10),
  cex.names=0.7,
  las=2, # las : 라벨을 옆으로 눕혀주는 아이
  ylim=c(0,25)
)

# 출력값 계산
pct <- round(bchart/sum(bchart)*100, 1) # 1은 첫 번째 자리수 까지 출력 

# 수치값 출력하기(%)
text(x = bp,
     y = bchart * 1.05,
     labels = paste("(",pct,"%",")"),
     col = "black",
     cex = 0.7)

# 수치값 출력하기 (건)
text(x = bp,
     y = bchart*0.95,
     labels = paste(bchart, "건"),
     col = "black",
     cex = 0.7)

# 가로로 누워진 bchart
barplot(bchart,
        main="제주도 추천 여행 코스 TOP10",
        col = rainbow(10),
        xlim=c(0,25),
        cex.name=0.7,
        las=1,
        horiz=T)

# 수치값 출력하기 (%)
text(y = bp,
     x = bchart*1.15,
     labels = paste("(",pct,"%",")"),
     col="black",
     cex=0.7)

# 수치값 출력하기(건)
text(y = bp,
     x = bchart*0.9,
     labels = paste(bchart,"건"),
     col="black",
     cex=0.7)

# 3D Pie Chart 로 표현(plotrix 라는 패키지가 추가로 필요)
#
install.packages("plotrix")
library(plotrix)
#-----------------------------
# 수치값을 함께 출력하기
# 출력값 계산
th_pct <- round(bchart/sum(bchart)*100,1)

# 지명과 계산 결과를 합치기
th_names <- names(bchart)
th_labels <- paste(th_names,"\n","(", th_pct,")")

pie3D(bchart,
      main="제주도 추천 여행 코스 TOP 10",
      col=rainbow(10),
      cex=0.3,
      labels=th_labels,
      explode=0.05)

