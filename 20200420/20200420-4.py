# 4) 박스 레이아웃

# =============================================================================
# 박스 레이아웃 클래스를 이용하면 훨씬 유연하고 실용적인 레이아웃을 할 수 있습니다.
# QHBoxLayout, QVBoxLayout 으로 가로, 세로를 구별해서 사용한다.(여러 위젯을 수평으로 정렬하는 레이아웃 클래스)
# QHBoxLayout, QVBoxLayout 생성자는 수평, 수직의 박스를 하나 만드는데, 다른 레이아웃 박스를 넣을 수도 있고, 위젯을 배치할 수도 있습니다.
# 예제 코드에서 위젯의 가운데 아래 부분에 두 개의 버튼을 배치하기 위해 수평, 수직의 박스를 하나씩 사용합니다.
# =============================================================================

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        okButton = QPushButton('OK') # QPushButton 으로 OK 버튼과 Cancel 버튼을 만들어 놓는다.(아직 배치가 안된 상태)
        cancleButton = QPushButton('Cancel')
        
        hbox = QHBoxLayout() # 수평 박스 레이아웃(가로로 긴 네모박스가 하나 만들어진다.HLayout)
        hbox.addStretch(1) # 위젯은 레이아웃에 나타나게 하려면 반드시 add가 되어있어야 한다.
        hbox.addWidget(okButton) # 왼쪽에 OK,
        hbox.addWidget(cancleButton) # OK버튼 옆에 Cancel 버튼을 배치한다.
        hbox.addStretch(1) # Stretch 값이 없으면 전체 창의 반반씩 균등 분할된다.(양 옆의 빈 공간을 1 대 1로 만들어 놓으라는 의미(위에서 1 아래에서 1))
        
        vbox = QVBoxLayout() # 수직 박스 레이아웃(세로로 긴 네모박스가 하나 만들어진다.)
        vbox.addStretch(3) # 위에서 3 비율만큼 띄워놓는다.
        vbox.addLayout(hbox) # 위에서 만들어놓은 hbox 를 배치한다.(OK, Cancel 버튼까지 배치해놓은 것)
        vbox.addStretch(1) # 아래에서 1 비율만큼 띄워놓는다.
        
        self.setLayout(vbox) # setLayout으로 vbox를 생성, 전체화면을 하더라도 상하좌우의 비율이 설정한대로 그대로 유지된다.(위젯의 크기는 별도로 지정해야 한다.)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())