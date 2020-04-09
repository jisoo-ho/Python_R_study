# 1.“환영합니다.” “파이썬의 세계에 오신 것을 환영합니다.” “파이썬은 강력합니다.” 를  화면에 출력하는 프로그램작성. 
print("환영합니다. 파이썬의 세계에 오신 것을 환영합니다. 파이썬은 강력합니다.")


# 2.다음 프로그램의 실행 결과를 쓰시오.
print("반갑습니다. 파이썬!!") # 반갑습니다. 파이썬!! 출력
print(2*3/10) # 결과 : 0.6 출력
print("Hello", "World", "!!!") # Hello World !!! 출력

# 3. 파이썬 쉘을 사용하여 한 주가 몇 시간에 해당하는 지를 계산 
day = 24
week = 7
print("한 주를 시간으로 환산하면",day * week,"시간 입니다")

# 4. 터틀 그래픽에서 거북이를 이동시켜서 다음과 같은 그림을 완성. 단, forward( ), right( ), left( ) 함수만을 사용
import turtle

t=turtle.Turtle()
t.shape("turtle")
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.clear()

# 5.  거북이를 이동하여 다음과 같이 두께가 10인 선을 완성.
t=turtle.Turtle()
t.shape("turtle")

t.width(10)
t.forward(100)
t.left(90)
t.forward(100)
t.clear()

# 6. 색상을 파랑색으로 변경하여 다음과 같이 길이가 100 pixel 인 선을 완성.

t=turtle.Turtle()
t.shape("turtle")

t.color("blue")
t.forward(100)
t.clear()

# 7. 사각형으로 변경하고 100 pixel 길이의 직선완성.

t=turtle.Turtle()
t.shape("square")
t.forward(100)
t.clear()

# 8. 원하는 위치에 선 두줄 긋기
t=turtle.Turtle()

t.shape("turtle")
t.forward(100)
t.up()
t.goto(0,100)
t.down()
t.forward(100)
t.clear()

# 9. 반지름이 100인 원이 그려진다.

t=turtle.Turtle()
t.shape("turtle")
t.speed(100)
t.circle(100)
t.up()
t.goto(100,0)
t.down()
t.circle(100)
t.up()
t.goto(200,0)
t.down()
t.circle(100)
t.up()
t.goto(80,-90)
t.down()
t.circle(100)
t.up()
t.goto(160,-90)
t.down()
t.circle(100)
