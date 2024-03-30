from PyQt5.QtWidgets import*
from PyQt5 import uic
import sys
import serial
from time import localtime


class UI(QMainWindow):
    def __init__(self):
        t = localtime()
        super(UI,self).__init__()

        self.ardu = serial.Serial(port='COM5',baudrate='9600',)

        #UI파일 불러오기
        uic.loadUi("sf_ui.ui",self)

        #위젯 명시
            #dht 온습도
        self.DHT_p = self.findChild(QPushButton,"DHT_p")
        self.DHT_t = self.findChild(QLabel,"DHT_t")
            #물 높이
        self.WH1_p = self.findChild(QPushButton,"WH1_p")
        self.WH1_t = self.findChild(QLabel,"WH1_t")
        self.WH2_p = self.findChild(QPushButton,"WH2_p")
        self.WH2_t = self.findChild(QLabel,"WH2_t")
            #물 온도
        self.WT1_p = self.findChild(QPushButton,"WT1_p")
        self.WT1_t = self.findChild(QLabel,"WT1_t")
        self.WT2_p = self.findChild(QPushButton,"WT2_p")
        self.WT2_t = self.findChild(QLabel,"WT2_t")
            #양액 농도
        self.PF_p = self.findChild(QPushButton,"PF_p")
        self.PF_t = self.findChild(QLabel,"PF_t")
            #릴레이
        self.R_WM = self.findChild(QCheckBox,"R_WM_cb")
        self.R_PM = self.findChild(QCheckBox,"R_PF_cb")
        self.R_L1 = self.findChild(QCheckBox,"R_L1_cb")
        self.R_L2 = self.findChild(QCheckBox,"R_L2_cb")

        #위젯 역활
            #push버튼
        self.DHT_p.clicked.connect(lambda:self.clicker('a',self.DHT_t))
        self.WH1_p.clicked.connect(lambda:self.clicker('j',self.WH1_t))
        self.WH2_p.clicked.connect(lambda:self.clicker('k',self.WH2_t))
        self.WT1_p.clicked.connect(lambda:self.clicker('l',self.WT1_t))
        self.WT2_p.clicked.connect(lambda:self.clicker('m',self.WT2_t))
        self.PF_p.clicked.connect(lambda:self.clicker('n',self.PF_t))

            #check버튼(릴레이)
        self.R_WM.stateChanged.connect(self.checked('b','c',self.R_WM))
        self.R_PM.stateChanged.connect(self.checked('d','e',self.R_PM))
        self.R_L1.stateChanged.connect(self.checked('f','g',self.R_L1))
        self.R_L2.stateChanged.connect(self.checked('h','i',self.R_L2))
                    
        #App 불러오기
        self.show()

    # push 버튼 클릭 할시
    def clicker(self,x,a):
        response = self.ask(x)
        if response is not None:
            a.setText(response)
    
    #check 박스 역활
    def checked(self,x,y,z):
        if z.isChecked()==True:
            self.ask(x)
        else:
            self.ask(y)

    # 아두이노와 통신
    def ask(self,x):
        commend = x
        self.ardu.write(commend.encode())  #아두이노에게 보내는 언어 endoing

        if self.ardu.readable():
            answ = self.ardu.readline().decode()  #아두이노의 응답 decode
            print(answ)
            return answ.strip()
    


app = QApplication(sys.argv)
UIWindow = UI()