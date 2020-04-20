# 1)창 띄우기
import sys
from PyQt5.QtWidgets import QApplication, QWidget
# 필요한 모듈들을 불러온다. 기본적인 UI구성요소를 제공하는 위젯(클래스)들은 PyQt5.QtWidgets 모듈에 포함되어 있습니다.
# QtWidgets 모듈에 포함된 모든 클래스들과 이에 대한 자세한 설명은 QtWidgets 공식문서에서 확인 가능

class MyApp(QWidget):#MyApp 클래스를 만드는데 QWidget 클래스를 상속받는다.
    def __init__(self): #파이썬의 생성자명은 __init__고정이다. 첫번째 고정값은 self로 들어가야한다.(인스턴스명이 self로 들어가야 함)
        super().__init__()
        
        self.initUI()
        
    def initUI(self): # 초기 UI함수 initUI로 이름을 정하고 객체를 인스턴스로 받아줄 self매개변수 지정
        
        self.setWindowTitle('My First Application')
        self.move(300,300)
        self.resize(400,200)
        self.show()

# 여기서 self는 MyApp 객체를 말한다.
# setWindowTitle() 메서드는 타이틀바에 나타나는 창의 제목을 설정
# move() 메서드는 위젯을 스크린의 x=300px, y=300px의 위치로 이동
# resize() 메서드는 위젯의 크기를 너비 400px, 높이 200px로 조절합니다.

if __name__ == '__main__':#py파일은 하나의 모듈형태로 만들어지기 때문에 누가 임포트하냐에 따라 __name__ 값이 달라진다.
    #자기가 직접 실행해야 실행된다. __name__(main) == __main__
    app = QApplication(sys.argv)
    ex = MyApp() # 생성자의 self는 ex를 전달받게 된다.
    sys.exit(app.exec_()) #app객체를 실행시키고, system 의 x버튼을 누르면 실행되고 있는 App을 종료시켜준다.

# =============================================================================
# 만약 파일명을 moduleA.py라고 만들면 이 파일을 직접 실행하면 __main__ 가 되고, 다른 파이썬 파일에서 가져오게 되면
# moduleA 라는 이름으로 전달된다.(__name__ == '__moduleA__')
# 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 한다.(app = QApplication(sys.argv)) -> 객체(인스턴스)명이 app 이 된 것
# =============================================================================
