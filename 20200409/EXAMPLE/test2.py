x = int(input("첫 번째 정수 입력: "))
y = int(input("두 번째 정수 입력: "))
sum = x+y

name = input("이름 입력: ")
print(name, "씨 안녕?")
print("파이썬 오신 것 환영.")

# 사용자의 대답을 변수에 저장한다.
stadium = input("경기장은 어디입니까? ")
winner = input("이긴팀은 어디입니까? ")
loser = input("진 팀은 누구입니까? ")
vip = input("우수선수는 누구입니까? ")
score = input("스코어는 몇대몇입니까? ")

# 변수와 문자열을 연결하여 기사를 작성한다.
print("")
print("======================================")
print("오늘", stadium, "에서 야구 경기가 열렸습니다.")
print(winner,"과",loser,"은 치열한 공방전을 펼쳤습니다.")
print(vip, "이 맹활약을 하였습니다.")
print("결국",winner,"가", loser,"를", score,"로 이겼습니다.")
print("======================================")

