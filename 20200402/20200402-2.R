install.packages("devtools")
library(devtools)
install_github("dkahle/ggmap")
library(ggmap)
install.packages("dplyr")
library(dplyr) 


crime_data <- read.csv("C:\\rStudy\\20200402\\Data3\\crime_in_Seoul.csv")
head(crime_data)
address_data <- read.csv("C:\\rStudy\\20200402\\Data3\\crime_in_Seoul_address.csv")
head(address_data)

names(crime_data) # "관서명"  "살인.발생" "살인.검거" "강도.발생" "강도.검거" "강간.발생" "강간.검거" "절도.발생" "절도.검거" "폭력.발생" "폭력.검거"
names(address_data) # "관서명" "주소"  
dim(crime_data) # 31, 11
dim(address_data)  # 31, 2

str(crime_data)
str(address_data)

c_data <- crime_data # 복사
add_data <- address_data #복사

sum(is.na(c_data)) # 널값 0 개 확인
sum(is.na(add_data)) # 널값 0 개 확인

police_code <- as.character(add_data$"주소")

googleAPIkey <- "AIzaSyDaqk0cpRrmBkT6-77TZLq2LUuml_mnro0"
register_google(googleAPIkey)

police_code <- geocode(police_code)

head(police_code)

police_code <- as.character(add_data$"주소") %>% enc2utf8() %>% geocode()

head(police_code)

police_code_final <- cbind(add_data, police_code)

head(police_code_final) # 관서명, 주소, 위경도 합친 값

c_data$절도.발생 <- gsub(",", "", c_data$절도.발생)
c_data$절도.검거 <- gsub(",", "", c_data$절도.검거)
c_data$폭력.발생 <- gsub(",", "", c_data$폭력.발생)
c_data$폭력.검거 <- gsub(",", "", c_data$폭력.검거)

head(c_data) # "," 찍힌부분 제거 완료
str(c_data) # chr 로 바뀐 것을 확인 가능 


c_data_occur <- c_data %>% 
  mutate(crime_sum = 살인.발생+강도.발생+강간.발생+ as.integer(c_data$절도.발생)+ as.integer(c_data$폭력.발생),
         catch_sum = 살인.검거+강도.검거+강간.검거+ as.integer(c_data$절도.검거)+ as.integer(c_data$폭력.검거),
         catch_ratio = (catch_sum/crime_sum)*100,
         )

head(c_data_occur) # 범죄건수, 검거건수, 검거율 확인

c_data_final <- cbind(as.data.frame(c_data_occur$관서명),c_data_occur$crime_sum, c_data_occur$catch_sum, round(c_data_occur$catch_ratio,1))

head(c_data_final)

c_data_final <- rename(c_data_final, "관서명"="c_data_occur$관서명",
                       "발생건수"= "c_data_occur$crime_sum",
                       "검거건수"="c_data_occur$catch_sum",
                       "검거율"="round(c_data_occur$catch_ratio, 1)")

str(c_data_final)

c_data_final$발생율 <- round((c_data_final$발생건수/(c_data_final$발생건수+c_data_final$검거건수))*100,1)

head(c_data_final) # 관서명, 발생건수, 검거건수, 검거율, 발생율

crime_data_final <- left_join(police_code_final,
                              c_data_final,
                              by="관서명") # 전체 데이터 정리(관서, 주소, 범죄, 검거, 검거율, 발생률)


seoul_map <- get_googlemap("seoulsi", 
                          maptype = "roadmap",
                          zoom=11)


ggmap(seoul_map) + # 지도를 먼저 그리고
  geom_point(data = police_code_final, # 빨간 점으로 위도경도값을 찍어주고
             aes(x=lon, y=lat),
             colour = "red",
             size=3) +
  geom_text(data = crime_data_final, # 그 위에다가 글씨를 쓰라는 의미
            aes(label = 관서명, vjust = -2.5),colour = "blue", size=5)+
  geom_text(data = crime_data_final,
            aes(label = 검거율, vjust = -2), size=3)+
  geom_text(data = crime_data_final,
            aes(label = 발생율, vjust = -1), size=3)


