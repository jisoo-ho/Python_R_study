# 7) 라디오 버튼
# =============================================================================
# 라디오 버튼은 단일 선택
# 한 위젯 안에 여러 라디오 버튼은 기본적으로 autoExclusive로 설정되어 있습니다. 하나의 버튼을 선택하면 나머지 버튼들은 선택 해제가 됩니다.
# 파이썬은 기본값이 단일선택이기 때문에 name 속성을 똑같이 쓰지 않아도 된다.

# ----------------------자주 쓰이는 메서드----------------------
#text() : 버튼의 텍스트를 반환합니다.
#setText() : 라벨에 들어갈 텍스트를 설정합니다.
#setChecked() : 버튼의 선택 여부를 설정합니다.
#isChecked() : 버튼의 선택 여부를 반환합니다.
#toggle() : 버튼의 상태를 변경합니다.

# ----------------------자주 쓰이는 시그널----------------------
#pressed() : 버튼을 누를 때 신호를 발생합니다.
#released()	: 버튼에서 뗄 때 신호를 발생합니다. 
#clicked() : 버튼을 클릭할 때 신호를 발생합니다.
#toggled() : 버튼의 상태가 바뀔 때 신호를 발생합니다.
 
# =============================================================================
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        rbtn1 = QRadioButton('First Button', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True) # 기본선택값을 rbtn1번으로 지정(True)
        # 파이썬의 불린값은 첫 글자만 대문자, 자바나 자바스크립티는 올 소문자, R 은 올 대문자

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())