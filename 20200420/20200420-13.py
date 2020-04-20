# QTabWidget

# =============================================================================
# 이러한 탭은 프로그램 안의 구성요소들이 많은 면적을 차지하지 않으면서,
# 그것들을 카테고리에 따라 분류할 수 있기 때문에 유용하게 사용될 수 있습니다.
# =============================================================================
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout


class MyApp(QWidget): # QWidget은 아무런 기능이 없음, 이 내부에 내가 원하는 위젯을 꾸밀 수 있다.

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        tab1 = QWidget() #각 탭에 들어갈 위젯 두 가지 설정
        tab2 = QWidget()

        tabs = QTabWidget() # 탭 위젯 객체 생성
        tabs.addTab(tab1, 'Tab1') # 탭 위젯에 addTab으로 추가될 위젯(tab1)을 추가하고, 쓰여질 글씨는 Tab1을 설정
        tabs.addTab(tab2, 'Tab2')

        vbox = QVBoxLayout() #Grid나 뭐 이거저거 사용해서 다중 위젯을 집어넣을 수 있다.
        vbox.addWidget(tabs) # Tab1, 2가 추가된 객체를 vbox 객체에 추가한다.

        self.setLayout(vbox) #윈도우에 셋팅

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())