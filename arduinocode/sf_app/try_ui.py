from PyQt5.QtWidgets import*
from PyQt5 import uic
import sys
from time import localtime

class UI(QMainWindow):
    def __init__(self):
        t = localtime()
        super(UI,self).__init__()

        #UI파일 불러오기
        uic.loadUi("try.ui",self)

        #위젯 명시
        self.textlb = self.findChild(QLabel,"label_2")
        self.pushbt = self.findChild(QPushButton,"pushButton")
        self.checkbx = self.findChild(QCheckBox,"checkBox")

        #위젯 기능
        self.pushbt.clicked.connect(lambda: self.textlb.setText("push"))
        self.checkbx.stateChanged.connect(self.checked)

        #시작시
        self.pushbt.click()

        if t.tm_hour >= 21 or t.tm_hour <7:
            self.checkbx.setChecked(True)
        else:
            self.checkbx.setChecked(False)

        #위젯 실행
        self.show()

    def checked(self):
        if self.checkbx.isChecked()==True:
            self.textlb.setText("checked")
        else:
            self.textlb.setText("unchecked")

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()