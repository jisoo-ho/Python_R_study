# 8) 콤보박스
# =============================================================================
# QComboBox는 작은 공간을 차지하면서, 여러 옵션들을 제공하고 그 중 하나의 옵션을 선택할 수 있도록 해주는 위젯
# =============================================================================

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150) # 왼쪽에서 50, 위쪽에서 150 이동
        
        cb = QComboBox(self) # 콤보박스 객체 생성
        cb.addItem('Option1') # 어느 콤보박스에 아이템 추가
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50) # 왼쪽에서 50, 위쪽에서 50 이동
        
        cb.activated[str].connect(self.onActivated) # cb내부에 현재 활성화 된 아이템의 글[str]을 뽑아달라.connect(self.onActivated 라는 함수에 연결)
        
        self.setWindowTitle('QcomboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def onActivated(self, text): # 위에서 연결한 것은 두 번째 매개변수 text로 넘어간다
        self.lbl.setText(text) # 선택된 글자를 라벨의 글자로 설정
        self.lbl.adjustSize() # 전달된 글자에 맞춰서 라벨 사이즈를 자동으로 변경

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())