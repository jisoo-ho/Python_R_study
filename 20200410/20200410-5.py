# 클래스 선언은 낙타표기법(첫 글자 대문자)
class BusinessCard:
    def __init__(self, name, email, addr): # 이렇게 만들면 객체가 생성될 때 값을 전달받도록 설정
        self.name = name 
        self.email = email 
        self.addr = addr

    def print_indo(self):
        print("--------------")
        print("Name:", self.name)
        print("E-mail:", self.email)
        print("Address:", self.addr)
        print("--------------")
#생성자를 만들던, 함수를 만들던 무조건 첫 번째는 self로 만들어야 한다.
    

# 파이썬에서는 self. 으로 하면 해당 변수를 자동으로 만들어준다.
# 오른쪽은 매개변수들
# 왼쪽은 self.를 통해 만들어지는 instance 변수들(변수객체들)
# self값은 객체명이 자동으로 넘어가는 변수명이기 때문에
# 값은 3개만 입력해야 한다.

"""
member1 = BusinessCard()
member1.set_info("Yuna Kim", "yunakim@naver.com", "Seoul") 

member2 = BusinessCard()
member2.set_info("Sarang Lee", "sarang.lee@naver.com", "Kyunggi")
"""

member1 = BusinessCard("hojisoo","1234@naver.com","Seoul")


class Foo:
    def func1():
        print("function1")

    def func2(self):
        print(id(self))
        print("function2")

"""
func1() 메서드의 첫 번째 인자가 self가 아님에도
클래스를 정의할 때 에러가 발생하지 않는다는 점
"""
f=Foo()

"""
Foo 클래스의 func2 메서드는
메서드의 인자가 self 뿐이므로
실제 메서드를 호출할 때는 인자를 전달할 필요가 없다.

func2 메서드의 첫 번째 인자를 self 지만
호출할 때는 아묵서도 전달하지 않는 이유는
첫 번째 인자인 self에 대한 값은
파이썬이 자동으로 넘겨주기 때문
"""
#f.func1()
f.func2()
print("f = Foo() => ", id(f))

"""
self의 정체를 좀 더 확실히 밝혀보기 위해
Foo 클래스를 수정하여 파이썬 내장 함수인 id()를 이용해
인스턴스가 메모리에 할당된 주소값을 확인
"""

"""
실행 결과를 살펴보면 42315162 라는 값이 출력됨을 확인할 수 있다.

Foo 클래스를 정의할 때 id(self)를 출력하게 했는데
id(self)의 값이 바로 61068096 인 것
"""

f2 = Foo()
print("f2 = Foo() =>" , id(f2))

f2.func2()

"""
f2를 통해 func2 메서드를 호출해보면 57730192가 출력됐습니다.
이 값은 바로 f2가 가리키고 있는 객체를 의미한다.
"""


"""
파이썬의 클래스는 그 자체가 하나의 네임스페이스이기 때문에
인스턴스 생성과 상관없이
클래스 내의 메서드를 직접 호출할 수 있다.

"""

Foo.func1()


"""
func1() 메서드를 호출했지만
앞서 인스턴스를 통해 메서드를 호출했던 것과는 달리
오류가 발생하지 않는다.

왜냐하면 인스턴스.메서드() 형태로 호출한 것과 달리
이번에는 클래스 이름.메서드() 형태로 호출했기 때문
"""

#Foo.func2() 로 호출하면 self값을 전달 못해서 에러 발생
"""
클래스 이름을 통해 func2() 메서드를 호출하려고 하면
self 위치에 인자를 전달해야 한다고 파이썬 인터프리터가 알려주낟.
>>> 모드에서 테스트

self 위치에 인자를 전달하지 않고 메서드를 호출하면 오류 발생

오류 메시지:
 func2() missing 1 required positional argument:'self'

오류 메시지를 확인하면
 func2()를 호출할 때 인자를 하나 빼먹읐음을 알 수 있다.
 즉, 인자를 하나 전달해야 하는데 전달하지 않아서 오류가 발생한 것.
"""
f3 = Foo()
print("f3 = Foo() =>", id(f3))

"""
func2 메서드는 인자를 하나 필요로하며, 해당 인자는 인스턴스여야 한다.

현재 f3은 새로 생성한 인스턴스를 바인딩하고 있으므로
func2 메서드의 인자로 f3을 전달해주면 된다.

"""
Foo.func2(f3)
f3.func2()
