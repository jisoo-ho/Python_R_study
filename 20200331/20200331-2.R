#연설문의 단어에 대한 워드 클라우드 만들기
install.packages("KoNLP")
install.packages("RColorBrewer")
install.packages("wordcloud")

library(KoNLP)
library(RColorBrewer)
library(wordcloud)

useSejongDic()

pal2 <- brewer.pal(8, "Dark2")

text <- readLines(file.choose()) # 문서를 줄단위로 읽어주는 함수 : readLines() 엔터친 위치를 기준으로 줄단위로 읽어오는 함수
text # 줄단위로 읽은 벡터를 텍스트에 집어넣고
# 리스트 타입의 데이터를 factor 형태로 반환하기가 힘들다. 그래서 
# extractNoun 이 명사를 찾아서 추출하는 역할(띄어쓰기도 있으면 띄어쓰기도 다 구분한다.), 그 결과를 sapply가 list형태로 반환
# text :  벡터가 가진 것들 중에서 , USE.NAMES : extractNoun 을 통해서 USE.NAMES를 실행
noun <- sapply(text, extractNoun, USE.NAMES = F) 
noun

# list 타입의 데이터를 수치형으로 변환
noun2 <- unlist(noun)
noun2

# p.221
word_count <- table(noun2) # 테이블을 하면 팩터로 바꿔준다. # 쪼개진 단어들의 갯수를 파악하여 테이블로 반환
word_count # 단어의 빈도수를 가지고 있음.

head(sort(word_count, decreasing = TRUE), 10) #정렬해주고 상위 10개만 꺼내온다.

wordcloud(names(word_count), # names 라는 함수를 이용해서 단어를 꺼내고
          freq=word_count,  # freq  옵션을 이용해서 글자나 숫자를 꺼낼 수 있다.
          scale=c(6,0.3),  # 가장 큰값을 6, 가장 작은 값을  0.3의 비율로 맞춘다.
          min.freq=3,      # 최소 빈도수를 3 이상으로 잡는다.(1이나 2는 표기하지않는다.)
          random.order = F, # 실행할때마다 위치 변경
          rot.per = .1,     # 회전 각도값을 0.1 비율로 회전시킨다.
          colors=pal2)      # 글자 색 변경



