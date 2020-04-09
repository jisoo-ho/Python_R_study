
# 1. 어떤 사람이 다음 주식 100주와 네이버 주식 20주를 가지고 있을 때
#그 사람이 가지고 있는 주식의 총액을 계산하는 프로그램을 작성하세요. 
daum = 89000 * 20
naver = 751000 * 20

a = daum+naver

print("이 사람이 가진 주식은",a,"입니다")


# 2. 주식 총액에서 다음(89000)과 네이버(751000)의 주가가  각각 5%, 10% 하락한 경우에 손실액을 구하는 프로그램을 작성하세요.
daum_loss = daum*0.95
naver_loss = naver*0.9

print("5%, 10%씩 손실된 금액은 Daum : ",daum_loss,", Naver : ",naver_loss,"입니다.")

# 3. 이 공식을 사용해 화씨 온도가 50일 때의 섭씨 온도를 계산해 보세요.
f = 100
c = (f-32)/1.8
print(c)

# 4. 화면에 "pizza" 10번 출력하는 프로그램을 작성하세요.
for i in range(10):
    print(" pizza",i, end="")
    

# 5. 월요일에 네이버의 주가가 100만 원으로 시작해  3일 연속으로 하한가(-30%)를 기록했을 때 수요일의 종가를 계산해 보세요.
naver = 1000000

day1 = naver * 0.7
day2 = day1 * 0.7
day3 = day2 * 0.7

print("3일 연속 하락한 네이버의 주가는 ",day3,"입니다")

# 6. 이름, 생년월일, 주민등록번호를 출력하는 프로그램을 작성해 보세요.
# 이름: 파이썬 생년월일: 2014년 12월 12일 주민등록번호: 20141212-1623210

name = input("이름입력: ")
birth = input("생년월일 입력: ")
idnum = input("주민번호입력: ")


print("이름 :",name)
print("생년월일 :",birth)
print("주민번호 :",idnum)




# 7. s라는 변수에 'Daum KaKao'라는 문자열이 바인딩돼 있다고 했을 때
# 문자열의 슬라이싱 기능과 연결하기를 이용해 s의 값을
# 'KaKao Daum'으로 변경해 보세요. 
s = ["Daum","KaKao"]
s2 =s[0]+" "+s[1]

print(s2)

# 8. a라는 변수에 'hello world'라는 문자열이 바인딩돼 있다고 했을 때
# a의 값을 'hi world'로 변경해 보세요.

a = "hello world"
b = a.replace("hello","hi")

print(b)



# 9. x 라는 변수에 'abcdef'라는 문자열이 바인딩돼 있다고 했을 때
# x 의 값을 'bcdefa'로 변경해 보세요.
x = 'abcdef'
print(x[1:]+x[0])






