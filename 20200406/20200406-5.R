library(KoNLP)
library(wordcloud)
library(stringr)
# 야구 선수별 연봉 대비 출루율 분석(밥값여부 계산)
# R을 활용한 데이터 시각화
kbo <- read.csv("./Data6_prj/야구성적.csv", header=T)
head(kbo)
View(kbo)

riceprice <- kbo[1:25,21]
View(riceprice)
name <- kbo$선수명

########
dev.new()


ricevalue <- barplot(as.matrix(riceprice),
                   main="밥값현황",
                   beside=T,
                   axes=F,
                   ylab="연봉대비출루율(%)",
                   xlab="",
                   cex.names=0.85,
                   las=2,
                   ylim=c(0,55),
                   col=rainbow(8),
                   border="white",
                   names.arg=name)

axis(2,ylim=seq(0,50,10)) #y축 생성
abline(h=seq(0,50,5),lty=2) # base line 생성

text(x = ricevalue,
     y = riceprice * 1.05,
     labels = paste("(",riceprice,"%",")"),
     col = "black",
     cex = 0.7)
