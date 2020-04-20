# 10) 프로그레스 바

# =============================================================================
# QProgressBar 위젯은 수평, 수직의 진행 표시줄을 제공합니다.
# setMinimum()과 setMaximum() 메서드로 진행 표시줄의 최소값과 최대값을 설정할 수 있으며,
# 또는 setRange() 메서드로 한 번에 범위를 설정할 수도 있습니다. 기본값은 0과 99입니다.
# setValue() 메서드로 진행 표시줄의 진행 상태를 특정 값으로 설정할 수 있고, reset() 메서드는 초기 상태로 되돌립니다.
# 진행 표시줄의 최소값과 최대값을 모두 0으로 설정하면, 진행 표시줄은 항상 진행 중인 상태로 표시됩니다.
# 이 기능은 다운로드하고 있는 파일의 용량을 알 수 없을 때 유용하게 사용할 수 있습니다.
# =============================================================================
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self) # 프로그레스 객체 생성
        self.pbar.setGeometry(30, 40, 200, 25) # 프로그레스(%) 진행 될 네모칸 만들기

        self.btn = QPushButton('Start', self) # 스타트버튼 만들기
        self.btn.move(40, 80) # 버튼 크기 결정
        self.btn.clicked.connect(self.doAction) # 클릭하면 액션 함수 실행하도록 만들기

        self.timer = QBasicTimer() # 타이머 객체 생성
        self.step = 0 # 스텝 변수에 기본값 0 할당(함수에 1씩 증가하도록 할 예정)

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e): # 위젯에 상속되어있는 함수를 수정한다.(timerEvent는 QObject에 상속되어있는 함수이다.)
        if self.step >= 100: # 만약 값이 100보다 같거나 커지면
            self.timer.stop() # 타이머를 정지시키고
            self.btn.setText('Finished') # 버튼에 써있는 값을 Finished로 변경
            return # 100보다 같거나 크지 않을경우에는 return 이 실행되지 않음

        self.step = self.step + 1 # if가 실행되지 않을 경우, 기존에 0으로 설정한 값을 1씩 더하면서 증가시킨다. 
        self.pbar.setValue(self.step) # 프로그레스 바를 step 값과 동일하게 변경해준다.(녹색 바의 위치를 지정해주는게 setValue 함수)

    def doAction(self): # Push버튼 눌렀을 때 호출하는 함수
        if self.timer.isActive(): # (timer.isActive() == True)일 때 실행(불린값으로 반환) - 만약 활성화 되어 있다면
            self.timer.stop() # 타이머를 스탑시키고
            self.btn.setText('Start') # 스타트 버튼을 누를 수 있다.
        else:
            self.timer.start(100, self) # 스타트 시키고
            self.btn.setText('Stop') # 스탑 버튼을 누를 수 있다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
    