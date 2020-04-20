# 14) QPixmap

# =============================================================================
# QPixmap은 이미지를 다룰 때 사용되는 위젯(only read 를 제외하고 모두 read/write 가능)
#bmp
#gif(only read)
#jpg
#jpeg
#png
#pbm(only read)
#pgm(only read)
#ppm
#xbm
#xpm
# =============================================================================
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('web.png') # 읽어들은 이미지파일이 객체로 만들어진다

        lbl_img = QLabel() # 라벨 객체 생성해서
        lbl_img.setPixmap(pixmap) # 그 내부에 이미지 객체를 출력해달라고 요청한다.
        lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height())) # 이미지를 출력할 때 가로/세로값을 얻을 수 있다.
        lbl_size.setAlignment(Qt.AlignCenter) # setAlignment함수를 이용해서 가운데로 정렬(Qt.AlignCenter)

        vbox = QVBoxLayout() # 세로박스 생성
        vbox.addWidget(lbl_img) # 위젯 달아주기
        vbox.addWidget(lbl_size)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.move(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())