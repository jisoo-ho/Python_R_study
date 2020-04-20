# 5) 그리드 레이아웃
# =============================================================================
# 가장 일반적인 레이아웃 클래스는 '그리드 레이아웃(grid layout)'입니다. 이 레이아웃 클래스는 위젯의 공간을 행 (row)과 열 (column)로 구분합니다.
# 그리드 레이아웃을 생성하기 위해 QGridLayout 클래스를 사용합니다.
# =============================================================================

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)
# 제목 타이틀 만들어주는 QLabel
# 글자를 여러줄로 입력해주는 QTextEdit
# 한줄을 입력해주는 QLineEdit
# HTML 에서 여러줄 입력받을 때 쓰는 태그가 textarea

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout() # 배치하기 위한 그리드 레이아웃 생성
        self.setLayout(grid) # 어플리케이션에 레이아웃 셋팅시켜야 한다.(이 셋팅코드는 맨 아래쪽에 써도 된다. - 객체 생성만 되어있으면 된다.)

        grid.addWidget(QLabel('Title:'), 0, 0) # 그리드 레이아웃에 위젯을 추가하겠다. (라벨객체를 추가하겠다, 0행, 0열에 추가)
        grid.addWidget(QLabel('Author:'), 1, 0) # 작성자 라는 라벨 객체를 만들고, 1행, 0열에 추가
        grid.addWidget(QLabel('Review:'), 2, 0) # 리뷰라는 라벨 객체를 만들고, 2행, 0열에 추가

        grid.addWidget(QLineEdit(), 0, 1) # 한 줄 짜리 입력받는 칸 0행 1열
        grid.addWidget(QLineEdit(), 1, 1) # 한 줄 짜리 입력받는 칸 1행 1열
        grid.addWidget(QTextEdit(), 2, 1) # 여러 줄 입력받는 칸 2행 1열

        self.setWindowTitle('QGridLayout') # 윈도우 제목 설정
        self.setGeometry(300, 300, 300, 200) # 생성할 창의 위치 왼쪽에서 떨어진 값, 위쪽에서 떨어진 값, 창의 크기 가로, 창의 크기 세로
        self.show() # 창 보여주기


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())