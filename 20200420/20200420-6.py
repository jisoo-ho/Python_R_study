# 6) 체크박스
# =============================================================================
# QCheckBox 위젯은 on(체크됨)/off(체크안됨)의 두 상태를 갖는 버튼을 제공합니다. 이 위젯은 하나의 텍스트 라벨과 함께 체크 박스를 제공합니다. 
# 체크 박스가 선택되거나 해제될 때, stateChanged() 시그널을 발생합니다. 체크 박스의 상태가 변할 때마다 어떠한 동작을 발생시키고 싶을 때,
# 이 시그널을 특정 슬롯에 연결할 수 있습니다.
# 또한 체크 박스의 선택 여부를 확인하기 위해서, isChecked() 메서드를 사용할 수 있습니다. 선택 여부에 따라 boolean 값을 반환합니다.
# 일반적인 체크 박스는 선택/해제 상태만을 갖지만, setTristate() 메서드를 사용하면 '변경 없음(no change)' 상태를 가질 수 있습니다.
# 이 체크 박스는 사용자에게 선택하거나 선택하지 않을 옵션을 줄 때 유용합니다.
# 세 가지 상태를 갖는 체크 박스의 상태를 얻기 위해서는 checkState() 메서드를 사용합니다. 선택/변경 없음/해제 여부에 따라 각각 2/1/0 값을 반환합니다.
# QButtonGroup 클래스를 사용하면 여러 개의 버튼을 묶어서 exclusive/non-exclusive 버튼 그룹을 만들 수 있습니다.
# exclusive 버튼 그룹은 여러 개 중 하나의 버튼만 선택할 수 있습니다.

# -------------------QCheckBox 위젯과 함께 자주 쓰이는 메서드-------------------
#text() : 체크 박스의 라벨 텍스트를 반환합니다.
#setText() : 체크 박스의 라벨 텍스트를 설정합니다.
#isChecked() : 체크 박스의 상태를 반환합니다. (True/False)
#checkState() : 체크 박스의 상태를 반환합니다. (2/1/0)
#toggle() : 체크 박스의 상태를 변경합니다.(on/off 기능)

# -------------------자주 쓰이는 시그널-------------------
#pressed() : 체크 박스를 누를 때 신호를 발생합니다.
#released() : 체크 박스에서 뗄 때 신호를 발생합니다.
#clicked() : 체크 박스를 클릭할 때 신호를 발생합니다.
#stateChanged() ★: 체크 박스의 상태가 바뀔 때 신호를 발생합니다.
# =============================================================================

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt
# 체크가 반환하는 상수값이 반환하는 모듈 Qt 

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI() # 기본 UI함수를 만들고

    def initUI(self):
        cb = QCheckBox('Show title', self) # 체크박스 객체 생성 (첫 번째 값은 라벨값, 두 번째 값 어디에)
        cb.move(20, 20) #위치 지정
        cb.toggle() # 온오프 기능을 부여한다
        cb.stateChanged.connect(self.changeTitle) # 체크박스객체에서.상태변화 변화 시그널 발생(이벤트 발생).이벤트가 발생되면 connect로 해당 함수에 연결(self.changeTitle)
        #반드시 상태변화가 일어나야 한다.
        
        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state): # 파이썬의 모든 함수는 첫 번째 매개변수가 무조건 self, 커넥트 함수를 통해서 연결시키면 현재 상수값이 자동으로 전달받음(이걸 받는 매개변수:state)
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
        # 전달받는 상수값에 따라서 Title을 '보여주겠다/보여주지않겠다'를 선택한다.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())