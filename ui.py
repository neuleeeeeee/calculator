# ch 5. 2. 1 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox, QPlainTextEdit, QHBoxLayout)
from PyQt5.QtGui import QIcon # 아이콘을 추가하기 위한 라이브러리

#나는 뷰 유형을 직접 정의한다! 이때, QWidget에 기반을 둔다
class View(QWidget) :

    def __init__(self) :

        super().__init__()
        self.initUI()

    # 초기화 한다
    def initUI(self) :
        
        self.te1=QPlainTextEdit() 
        self.te1.setReadOnly(True)
        
        # 버튼 1 추가
        self.btn1=QPushButton('Message', self) 
        self.btn2=QPushButton('Clear', self) 

        hbox = QHBoxLayout() # 수평(H) 레이아웃을 추가하고 버튼1, 2 추가
        hbox.addStretch(1)
        hbox.addWidget(self.btn1) # 버튼 1 배치
        hbox.addWidget(self.btn2) # 버튼 2 배치

        vbox=QVBoxLayout() # 수직(V) 레이아웃 위젯 생성
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox) # btn1 위치에 hbox를 배치
        vbox.addStretch(1) # 빈(Stretch)공간

        self.setLayout(vbox) # 빈공간 - 버튼 - 빈공간 순으로 수직 배치된 레이아웃 설정(set) 적용

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png')) # 윈도창에 아이콘 추가
        self.resize(256,256)
        self.show()
    
    def activateMessage(self) : # 버튼을 클릭할 때 동작하는 함수 : 메세지 박스 출력
        # QMessageBox.information(self, "information", "버튼 클릭!")
        self.te1.appendPlainText("Button clicked!")
    
    def clearMessage(self) : # 버튼 2 핸들러 함수 정의
        self.te1.clear()
