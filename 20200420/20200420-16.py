# 16)QTextBrowser

# =============================================================================
# QTextBrowser 클래스는 하이퍼텍스트 내비게이션을 포함하는 리치 텍스트 (서식있는 텍스트) 브라우저를 제공합니다.
# 이 클래스는 읽기 전용이며, QTextEdit의 확장형으로서 하이퍼텍스트 문서의 링크들을 사용할 수 있습니다.
# 편집 가능한 리치 텍스트 편집기를 사용하기 위해서는 QTextEdit을 사용해야 합니다.
# 또한 하이퍼텍스트 네비게이션이 없는 텍스트 브라우저를 사용하기 위해서는
# QTextEdit을 setReadOnly()를 사용해서 편집이 불가능하도록 해줍니다.
# =============================================================================

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout)
#클래스명들이 길어서 줄을 바꿔야 할 경우에는 괄호로 묶어서 줄바꿈해주면 된다.
# 태그를 해석시켜서 출력시켜줄 다중 창(QTextBrowser)
# 텍스트 브라우저가 가진 내용을 전부 지워줄 버튼을 만들 QPushButton
# 위에서부터 아래쪽으로 순서대로 배치해 줄 QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit() # QLineEdit() : HTML 태그형태로 입력할 수 있는 한 줄 짜리 입력창
        self.le.returnPressed.connect(self.append_text) # 키보드에 엔터가 눌렸는지 안눌렸는지 알아내는 returnPressed.엔터를 누르면 값을 append_text로 전달

        self.tb = QTextBrowser() # 태그를 해석해서 출력시켜줄 텍스트브라우저 객체 생성
        self.tb.setAcceptRichText(True) # 텍스트 브라우저에 출력된 글씨들을 복사한다던지, 이와 같이 해당 글자를 접근 가능하게 할거면 True, 막을거면 False
        self.tb.setOpenExternalLinks(True) # 외부 브라우저로 접속해야 하기 때문에 외부링크 허용 True, 허용하지 않으면 False

        self.clear_btn = QPushButton('Clear') # 버튼 생성(버튼에 쓰일 값은 Clear)
        self.clear_btn.pressed.connect(self.clear_text) # 버튼이 눌려지면 clear_text 함수 호출

        vbox = QVBoxLayout() # 박스 객체 생성
        vbox.addWidget(self.le, 0) # 0행에 위젯 달기
        vbox.addWidget(self.tb, 1) # 1행에 위젯 달기
        vbox.addWidget(self.clear_btn, 2) # 2행에 버튼 달기

        self.setLayout(vbox)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def append_text(self): #텍스트 브라우저에 추가시킬 함수
        text = self.le.text() # 입력받은 self의 text값을 얻어내서 text 변수에 저장
        self.tb.append(text) # 텍스트박스에 append 시킨다.(text값을 append)
        self.le.clear() # 라인 데이터에 쓰여진 있는 값은 클리어시킨다.

    def clear_text(self): # 버튼눌렀을 때 모두 clear해줄 함수
        self.tb.clear() # tb, le 모두, te 에도 clear 함수가 있다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
