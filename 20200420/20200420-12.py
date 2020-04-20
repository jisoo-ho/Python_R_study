# 12) QSplitter
# https://wikidocs.net/32154
# =============================================================================
# 스플리터 (splitter)는 경계를 드래그해서 자식 위젯의 크기를 조절할 수 있도록 합니다.
# =============================================================================

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter # QFrame 은 구분선 만들어주는 클래스, QSplitter는 드래그해서 사이즈 변경
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self): #생성자
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout() # 가로 박스 객체 생성

        top = QFrame() # 상단에 배치할 프레임
        top.setFrameShape(QFrame.Box) 

        midleft = QFrame() # 가운데 왼쪽에 배치할 프레임
        midleft.setFrameShape(QFrame.StyledPanel) # 각각의 프레임 형태는 2번 라인 사이트 참조

        midright = QFrame() # 가운데 오른쪽에 배치할 프레임
        midright.setFrameShape(QFrame.Panel)

        bottom = QFrame() # 아래쪽에 배치할 프레임
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken) # 그림자 처리해줄때 shadow 사용(음각 박스)

        splitter1 = QSplitter(Qt.Horizontal) # 쪼개지는 방향성을 의미한다. (가로로 쪼갠다.) -> 방향으로 가운데를 쪼갠다(좌, 우로 나뉨)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)

        splitter2 = QSplitter(Qt.Vertical) # 쪼개지는 방향성을 의미한다. (세로로 쪼갠다.) -> ↓ 방향으로 쪼갠다.(상중하 3단계로 쪼갬)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2) # 전체 내용을 hbox에 전달한다
        self.setLayout(hbox) # hbox를 윈도우에 셋팅한다

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())