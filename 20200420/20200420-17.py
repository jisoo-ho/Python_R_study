# 17) QTextEdit

# =============================================================================
# QTextEdit 클래스는 플레인 텍스트 (plain text)와 리치 텍스트 (rich text)를 모두 편집하고 표시할 수 있는 편집기를 제공
# =============================================================================

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('Enter your sentence:') # 라벨에 텍스트 입력 요청값 넣기
        self.te = QTextEdit() # te에 QTextEdit 객체 생성
        self.te.setAcceptRichText(False) # te객체에 입력되는 해당텍스트를 접근 가능하도록 하지 않는다(False)
        self.lbl2 = QLabel('The number of words is 0') # 단어가 입력되지 않았을 경우 초기 라벨값 설정

        self.te.textChanged.connect(self.text_changed) # 텍스트에 변화가 일어나면 텍스트 체인이 함수 호출

        vbox = QVBoxLayout() # 박스 객체 생성
        vbox.addWidget(self.lbl1) # 1번 라벨값
        vbox.addWidget(self.te) # te객체(텍스트 입력받을 박스)
        vbox.addWidget(self.lbl2) # 2번 라벨값
        vbox.addStretch() # 스트레치 비율 설정

        self.setLayout(vbox)

        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def text_changed(self):
        text = self.te.toPlainText() # TextEdit에 쓰여있는 글자를 가져온다.
        self.lbl2.setText('The number of words is ' + str(len(text.split()))) # 입력된 글자를 쪼개고 그 문자(단어)의 갯수를 str로 반환
        #TextEdit에 RichText 형식의 글을 입력합니다. Parameter에는 TextEdit에 표시할 글자가 들어갑니다.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())