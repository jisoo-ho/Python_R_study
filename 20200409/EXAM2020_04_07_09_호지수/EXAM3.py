# 1. 사용자로부터 두 개의 정수를 입력 받아서 정수의
# 합, 차, 곱, 평균, 큰 수, 작은 수를 계산하여
#  화면에 출력하는 프로그램을 작성.
# 파이썬이 제공하는 max(x, y) / min(x, y) 함수를 사용. 

x = int(input("1. 정수를 입력하세요."))
y = int(input("2. 정수를 입력하세요."))

print("합 : ",x+y)
print("차 : ",x-y)
print("곱 : ",x*y)
print("평균 : ",(x+y)/2)
print("큰 수 : ",max(x,y))
print("작은 수 : ",min(x,y))

# 2. 원기둥의 부피를 계산하는 프로그램을 작성.
half = float(input("반지름입력 : "))
height = float(input("원기둥 높이 입력: "))
cylinder = 3.141592 * (half**2) * height
print("입력한 값으로 구한 원기둥의 부피 : ",cylinder)


# 3. 정수의 자리수의 합을 계산하는 프로그램 작성.
number = int(input("숫자를 입력하세요. "))

result = 0

for i in str(number):
    result = result + int(i)

print("결과는",result,"입니다.")



# 4. 두 점 사이의 거리를 계산하는 프로그램 완성.
x1 = float(input("1차 x값을 입력하세요."))
y1 = float(input("1차 y값을 입력하세요."))

x2 = float(input("2차 x값을 입력하세요."))
y2 = float(input("2차 y값을 입력하세요."))

dist = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
print("요청한 좌표의 거리값은", dist,"입니다.")

# 5. 4번 문제에 대한 답을 TURTLE 로 확인
import turtle

t=turtle.Turtle()
t.lt(45)
t.fd(141)
t.up()
t.goto(0,0)

t.rt(45)
t.down()
t.fd(100)
t.lt(90)
t.fd(100)


# 6. 사용자로부터 두 점을 입력 받아서 터틀 그래픽을 이용하여 두 점을 연결하는 직선을 그리고,
#  직선의 끝점에 직선의 길이를 계산하여 출력.
import math
x1 = float(input("1차 x값을 입력하세요."))
y1 = float(input("1차 y값을 입력하세요."))

x2 = float(input("2차 x값을 입력하세요."))
y2 = float(input("2차 y값을 입력하세요."))

dist = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
print("요청한 좌표의 거리값은", dist,"입니다.")

import turtle
t=turtle.Turtle()

t.up()
t.goto(x1,y1)
t.down()
t.fd(dist)

