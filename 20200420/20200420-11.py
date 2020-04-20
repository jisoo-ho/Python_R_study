# 11) QSlider & QDial(슬라이더, 다이얼)

# =============================================================================
# 슬라이더의 틱(tick)의 간격을 조절하기 위해서는 setTickInterval() 메서드, 틱(tick)의 위치를 조절하기 위해서는 setTickPosition() 메서드를 사용합니다.
# setTickInterval() 메서드의 입력값은 픽셀이 아니라 값을 의미합니다.

# ---------------------------setTickPosition() 메서드의 입력값과 기능---------------------------
#QSlider.NoTicks : (값 : 0, 틱을 표시하지 않습니다.)
#QSlider.TicksAbove : (값 :, 틱을 (수평) 슬라이더 위쪽에 표시합니다.)
#QSlider.TicksBelow : (값 :, 틱을 (수평) 슬라이더 아래쪽에 표시합니다.)
#QSlider.TicksBothSides : (값 : , 틱을 (수평) 슬라이더 양쪽에 표시합니다.)
#QSlider.TicksLeft : (값 : TicksAbove, 틱을 (수직) 슬라이더 왼쪽에 표시합니다.)
#QSlider.TicksRight : (값 : TicksBelow, 틱을 (수직) 슬라이더 오른쪽에 표시합니다.)
# ---------------------------------------------------------------------------------------------

# QDial은 슬라이더를 둥근 형태로 표현한 다이얼 위젯이며, 기본적으로 같은 시그널과 슬롯, 메서드들을 공유
# 다이얼 위젯에 노치(notch)를 표시하기 위해서는 setNotchesVisible() 메서드를 사용합니다.
# True로 설정하면 둥근 다이얼을 따라서 노치들이 표시됩니다. 기본적으로 노치는 표시되지 않도록 설정되어 있습니다.

# ---------------------------QSlider과 QDial 위젯에서 가장 자주 쓰이는 시그널---------------------------
#valueChanged() : 슬라이더의 값이 변할 때 발생합니다.
#sliderPressed() : 사용자가 슬라이더를 움직이기 시작할 때 발생합니다.
#sliderMoved() : 사용자가 슬라이더를 움직이면 발생합니다.
#sliderReleased() : 사용자가 슬라이더를 놓을 때 발생합니다.
# =============================================================================

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self) # 슬라이더 객체 생성(가로로 만들기), 수평으로 만들건지 수직으로 만들건지 내장 [상수]로 보내준다.
        # 상수는 대부분 Qt가 가지고 있기 때문에 값을 Qt에서 꺼내온다.(Qt.Horizontal / Qt.Vertical)
        self.slider.move(30, 30) # 위치 설정
        self.slider.setRange(0, 50) # 슬라이더의 min, max값 설정
        self.slider.setSingleStep(2) # 한 번 이동시 이동할 틱 값 설정

        self.dial = QDial(self) # 다이얼 객체 생성
        self.dial.move(30, 50) # 다이얼 위치 설정
        self.dial.setRange(0, 50) # 다이얼의 min, Max값 설정

        btn = QPushButton('Default', self) # Default 라고 쓰여진 버튼 생성 
        btn.move(35, 160) # 버튼 위치 선정

        #slider 따로 dial 따로 하면 아래 3줄은 필요 없음
        self.slider.valueChanged.connect(self.dial.setValue)  # 슬라이더의 값에 변화가 일어나면 그 값을 dial.setValue로 보낸다.
        self.dial.valueChanged.connect(self.slider.setValue) # 다이얼의 값이 변했을 때 그 값을 slider.setValue로 보낸다.
        btn.clicked.connect(self.button_clicked) # 버튼이 클릭되었을 때 그 값을 button_clicked로 보내준다.(사용자가 만드는 함수)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def button_clicked(self):
        self.slider.setValue(0) # 슬라이더의 값을 0으로 설정
        self.dial.setValue(0) # 다이얼의 값을 0으로 설정


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())