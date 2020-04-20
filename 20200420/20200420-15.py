# 15) QCalendarWidget

# =============================================================================
# QCalendarWidget을 이용해서 사용자가 날짜를 선택할 수 있도록 달력을 표시할 수 있습니다.
# 달력은 월 단위로 표시되고, 처음 실행될 때 현재의 연도, 월, 날짜로 선택되어 있습니다.
# =============================================================================

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self) # 기본값은 현재 날짜, 캘린더 객체 생성
        cal.setGridVisible(True) # 날짜와 날짜 사이에 가로선 세로선을 만들어 준다(True), False면 나타나지 않음
        cal.clicked[QDate].connect(self.showDate) # 해당 날짜를 클릭했을 때 QDate 객체를 전달해준다.(showDate 함수로 전달)

        self.lbl = QLabel(self) # 라벨 객체 생성
        date = cal.selectedDate() # 선택된 날짜를 얻어내서 date 변수에 저장
        self.lbl.setText(date.toString()) # 선택된 date를 str값으로 바꿔서 라벨에 저장

        vbox = QVBoxLayout() # 수직 박스 생성
        vbox.addWidget(cal) # 캘린더 위젯 add(위에는 캘린더)
        vbox.addWidget(self.lbl) # 선택된 날짜가 부여된 라벨 add(아래는 라벨)

        self.setLayout(vbox) # 박스 셋팅

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date): #클릭 시그널이 호출했을 때 실행될 함수
        self.lbl.setText(date.toString()) # QDate를 date가 받는다. 받은 데이트 값을 str으로 변환하여 lbl에 부여


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())