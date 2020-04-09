# 1. 사용자한테 이름과 나이를 입력받고, 사용자의 나이가 100살이 되는 연도를 
name = input("이름을 입력하시오 :")
age = int(input("나이를 입력하시오 :"))
year = 2020-age+100
print(name,"님은",year,"년에 100살 이시네요!")

# 2. 사용자로부터 3개의 숫자를 받아서 평균을 계산하고, 결과를 출력하는 프로그램 완성.
v1 = float(input("첫 번째 숫자 입력 :"))
v2 = float(input("두 번째 숫자 입력 :"))
v3 = float(input("세 번째 숫자 입력 :"))
avg = (v1 + v2 + v3) / 3
print("입력한 세 수의 평균은" ,avg, "입니다.")

# 3. 사용자로부터 원의 반지름을 입력 받아서 원의 면적을 구하는 프로그램 완성
half = int(input("반지름을 입력하세요."))
face = 3.141592 * (half**2)
print("반지름이",half,"인 원의 넓이=",face)

# 4. radius 변수를 이용해서 각기 다른 원 3개 그리기
import turtle
radius=50

t=turtle.Turtle()

t.circle(radius)
t.up()
t.goto(100,0)
t.down()
t.circle(radius+20)
t.up()
t.goto(200,0)
t.down()
t.circle(radius+20+20)

# 5.  side 변수의 초기값은 100. side 변수를 이용하여 화면에 삼각형을 완성.
import turtle
side = 100
t=turtle.Turtle()
t.speed(100)
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)

# 6.  만약 삼각형 한변의 길이를 200으로 변경한다면 5번 코드에서 어디만 수정하면 되는가? 
# side = 200으로만 바꿔주면 된다.

# 7.  이 때 작은 사각형의 한 변의 길이는 side 변수에 저장하고, 거북이가 회전하는 각도는 angle 변수에 저장.
import turtle
side = 100
ang = 90
t=turtle.Turtle()

t.fd(side)
t.rt(ang)
t.fd(side)
t.rt(ang)
t.fd(side)
t.rt(ang)
t.fd(side)

t.fd(side)
t.rt(ang)
t.fd(side)
t.rt(ang)
t.fd(side)

t.fd(side)
t.lt(ang)
t.fd(side)
t.lt(ang)
t.fd(side)

t.fd(side)
t.lt(ang)
t.fd(side)
t.lt(ang)
t.fd(side)
t.lt(ang)
t.fd(side)
