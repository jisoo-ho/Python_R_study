# 9) 입력받은 text를 label로 출력
# =============================================================================
# QLineEdit은 한 줄의 문자열을 입력하고 수정할 수 있도록 하는 위젯입니다. 
# =============================================================================

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)
        
        qle = QLineEdit(self)
        qle.move(60, 100)
        qle.textChanged[str].connect(self.onChanged) # QLineEdit에 글자의 변화가 일어난 후, 글자[str]를 뽑아서 self.onChanged에 전달
        
        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def onChanged(self, text):
        self.lbl.setText(text) # 전달된 글자를 라벨에 새겨주고
        self.lbl.adjustSize() # 전달된 글자를 라벨 크기에 맞게 바꿔준다.
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())