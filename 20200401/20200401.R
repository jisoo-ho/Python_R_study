install.packages("ggplot2")
library(ggplot2)

x <- c("a", "a", "b", "c") 
qplot(x) 

qplot(data = mpg, x = hwy)
head(mpg)

qplot(data = mpg, x = drv, y = hwy) 

# x 축 drv, y 축 hwy, 선 그래프 형태
qplot(data = mpg, x = drv, y = hwy, geom = "line") 

str(x)

exam <- read.csv(file.choose(), header=T)
head(exam, 10)

mpg <- as.data.frame(ggplot2::mpg)

install.packages("dplyr")  # dplyr 설치
library(dplyr)             # dplyr 로드

df_raw <- data.frame(var1 = c(1, 2, 1),
                     var2 = c(2, 3, 2)) 
df_raw 

df_new <- df_raw  # 복사본 생성
df_new            # 출력

df_new <- rename(df_new, v2 = var2)  # var2 를 v2 로 수정

table(mpg$test)  
library(ggplot2)
qplot(mpg$test)

mpg$grade <- ifelse(mpg$total >= 30, "A",ifelse(mpg$total >= 20, "B", "C")) 


midwest <- as.data.frame(ggplot2::midwest)
midwestNew <- midwest
head(midwestNew)
str(midwestNew)
dim(midwestNew) # 437  28
summary(midwestNew)
names(midwestNew)
midwestNew <- rename(midwestNew, c(total  = poptotal,asian   = popasian))
names(midwestNew) # total, asian 변경완료 확인

midwestNew$asian_rate <- midwestNew$asian / midwestNew$total # ? *100왜안먹힘
midwestNew$asian_rate <- midwestNew$asian_rate*100
head(midwestNew$asian_rate) # 아시아인 인구 비율 확인

hist(midwestNew$asian_rate) # 히스토그램 생성
asian_mean <- mean(midwestNew$asian_rate) # 아시아 인구 백분율 평균 : 48.72%

midwestNew$test <- ifelse(midwestNew$asian_rate > asian_mean, "large", "small") # 조건문에 맞는 파생변수 삽입

library(ggplot2)  #라이브러리 로드
table(midwestNew$test) # large 119, small 318
qplot(midwestNew$test)


library(dplyr) 
exam <- read.csv(file.choose(), header = T) 
exam_new <-  exam

# exam 에서 class 가 1 인 경우만 추출하여 출력
exam %>% filter(class == 1) 

# 1반이 아닌 학생
exam %>% filter(class != 1)

# 수학 점수가 50 점을 초과한 경우
exam %>% filter(math > 50)

# 1 반 이면서 수학 점수가 50 점 이상인 경우
exam %>% filter(class == 1 & math >= 50) 


# 중간고사 데이터 생성
test1 <- data.frame(id = c(1, 2, 3, 4, 5),
                    midterm = c(60, 80, 70, 90, 85)) 

# 기말고사 데이터 생성
test2 <- data.frame(id = c(1, 2, 3, 4, 5),
                    final = c(70, 83, 65, 95, 80))

total <- left_join(test1, test2, by = "id")

name <- data.frame(class = c(1, 2, 3, 4, 5),
                   teacher = c("kim", "lee", "park", "choi", "jung"))

exam_new <- left_join(exam, name, by = "class") exam_new

group_a <- data.frame(id = c(1, 2, 3, 4, 5),
                      test = c(60, 80, 70, 90, 85)) 
group_b <- data.frame(id = c(6, 7, 8, 9, 10),
                      test = c(70, 83, 65, 95, 80))

# 세로로 합치기 
group_all <- bind_rows(group_a, group_b)  # 데이터 합쳐서 group_all 에 할당
group_all                                 # group_all 출력

df <- data.frame(sex = c("M", "F", NA, "M", "F"),
                 score = c(5, 4, 3, 4, NA))
is.na(df)         
table(is.na(df))  
library(ggplot2)
ggplot(data = mpg, aes(x = displ, y = hwy))
ggplot(data = mpg, aes(x = displ, y = hwy)) + geom_point()
ggplot(data = mpg, aes(x = displ, y = hwy)) +
  geom_point() +
  xlim(3, 6) +
  ylim(10, 30)

df_mpg <- mpg %>%                    # 데이터 프레임 mpg 로부터
  group_by(drv) %>%                   # 구동 방식을 그룹핑 시켰다
  summarise(mean_hwy = mean(hwy))    

ggplot(data = mpg, aes(x = reorder(drv, -mean_hwy), y = mean_hwy)) + geom_col()


ggplot(data = economics, aes(x = date, y = unemploy)) + geom_line()
ggplot(data = mpg, aes(x = drv, y = hwy)) + geom_boxplot()

################# 데이터 분석 프로젝트

install.packages("foreign") # foreign 패키지 설치
install.packages("readxl")
library(foreign)           # SPSS 파일 로드
library(dplyr)           # 전처리
library(ggplot2)           # 시각화
library(readxl)           # 엑셀파일 불러오기

raw_welfare <- read.spss(file = "C:/rStudy/20200401/Koweps_hpc10_2015_beta1.sav",
                         to.data.frame =T)

welfare <- raw_welfare # 복사본 만들기

dim(welfare) # 16664 행, 957 열

# 데이터 검토하기
head(welfare)
tail(welfare)
View(welfare)
str(welfare)
summary(welfare)

sum(is.na(welfare))


#변수명 바꾸기
welfare <- rename(welfare,
                  sex = h10_g3,            #성별
                  birth = h10_g4,          #태어난 연도
                  marrige = h10_g10,       # 혼인 상태
                  religion = h10_g11,      # 종교
                  income = p1002_8aq1,     # 월급
                  code_job = h10_eco9,     # 직종 코드
                  code_region = h10_reg7)  # 지역 코드

names(welfare)# 변경된 컬럼명 확인

class(welfare$sex) # numeric 타입 확인
table(welfare$sex) # 1: 7578, 2: 9086 확인(남녀 빈도수)

# 이상치 결측 처리
welfare$sex <- ifelse(welfare$sex == 0, NA, welfare$sex)

table(is.na(welfare$sex)) # False : 16664

#성별 항목 이름 부여
welfare$sex <- ifelse(welfare$sex ==1, "male", "female")
table(welfare$sex)

qplot(welfare$sex)

class(welfare$income)
summary(welfare$income)      

qplot(welfare$income)
qplot(welfare$incom) + xlim(0, 1000)
welfare$income <- ifelse(welfare$income %in% c(0, 9999), NA, welfare$income)
table(is.na(welfare$income)) # False : 4620, True : 12044

sex_income <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(sex) %>%
  summarise(mean_income = mean(income))

sex_income # female : 163, male : 312

ggplot(data = sex_income, aes(x=sex, y=mean_income)) + geom_col()
class(welfare$birth)
summary(welfare$birth)

qplot(welfare$birth)
summary(welfare$birth)
table(is.na(welfare$birth)) #False 16664
welfare$birth <- ifelse(welfare$birth == 9999, NA, welfare$birth)
table(is.na(welfare$birth))
welfare$age <- 2015 - welfare$birth +1
summary(welfare$age)

qplot(welfare$age)

age_income <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(age) %>%
  summarise(mean_income = mean(income))

head(age_income)

ggplot(data = age_income, aes(x=age, y=mean_income)) + geom_line()

welfare <- welfare %>%
  mutate(ageg = ifelse(age < 30, "young",
                       ifelse(age <= 59, "middle", "old")))

ageg_income <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(ageg) %>% 
  summarise(mean_income = mean(income))

table(welfare$ageg)
qplot(welfare$ageg)

ageg_income

ggplot(data = ageg_income, aes(x=ageg, y=mean_income)) + geom_col()

ggplot(data = ageg_income, aes(x = ageg, y= mean_income)) + geom_col() + scale_x_discrete(limits = c("young", "middle", "old"))

sex_income <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(ageg, sex) %>% 
  summarise(mean_income = mean(income))

ggplot(data = sex_income, aes(x = ageg, y=mean_income, fill=sex)) +
  geom_col() +
  scale_x_discrete(limits = c("young", "middle", "old"))

ggplot(data = sex_income, aes(x = ageg, y=mean_income, fill=sex)) +
  geom_col(position="dodge") +
  scale_x_discrete(limits = c("young", "middle", "old"))


sex_age <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age, sex) %>% 
  summarise(mean_income = mean(income))



ggplot(data = sex_age, aes(x=age, y=mean_income, col=sex)) + geom_line()













