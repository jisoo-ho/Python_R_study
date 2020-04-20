# 3) 절대적 배치

# =============================================================================
# 절대적 배치(Absolute positioning) 방식은 각 위젯의 위치와 크기를 픽셀 단위로 설정해서 배치합니다.
# 개발자가 마음대로 변화시킬 수 있는 Absolute
# 창의 크기를 조절해도 위젯의 크기와 위치는 변하지 않는다.
# 다양한 플랫폼에서 어플리케이션이 다르게 보일 수 있다.
# 어플리케이션의 폰트를 바꾸면 레이아웃이 망가질 수 있다.
# 레이아웃을 바꾸고 싶다면 완전히 새로 고쳐야 하며, 이는 매우 번거롭다.
# =============================================================================

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)
        
        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)
        
        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
        
# =============================================================================
# 버튼에 move 함수라던지, 라벨의 move 함수는 창의 왼쪽 상단이 0,0 으로 기준이 된다.
# 창의 위치는 모니터를 기준으로 모니터 전체의 좌측 상단이 기준이 된다.
# 열린 창의 크기를 변화시켜도 라벨과 버튼의 위치는 변하지 않는다.
# 다양한 사이즈의 디바이스에서 사용할 경우엔 Absolute 는 좋지 않은 방식이다.(절대값으로 위치를 잡아주기 때문에 좋지 않다.)
# =============================================================================
