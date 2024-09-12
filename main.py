# ch 4. 2. 3 main.py
import sys # 시스템 제어 관련 모듈(여기서는 프로그램 종료 위해 사용)

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QIcon # 아이콘을 추가하기 위한 라이브러리

'''
# 위젯 : GUI 프로그램에서 구성요소를 뜻하는 용어(세부모듈인 QtWidgets으로부터 사용)
from PyQt5.QtWidgets import QApplication, QWidget
'''

#나는 계산기 유형을 직접 정의한다! 이때, QWidget에 기반을 둔다
class Calculator(QWidget) :

    def __init__(self) :
        super().__init__() # (규칙)뭔가(QWidget)에 기반을 둘 경우 써줘야 하는 코드
        self.initUI() # 생성자에서 호출한다
    
    # 초기화 한다
    def initUI(self) :

        # btn1속성으로 "message"버튼 추가(self = calculator)
        self.btn1=QPushButton('Message', self) 
        # 버튼 클릭 시 이벤트 핸들링(클릭했을 때, 뭐를 할거다! 라고 정의하는 것) 함수 연결
        self.btn1.clicked.connect(self.activateMessage) 

        vbox=QVBoxLayout() # 수직(V) 레이아웃 위젯 생성
        vbox.addStretch(1) # 빈(Stretch)공간
        vbox.addWidget(self.btn1) # 버튼 위치
        vbox.addStretch(1) # 빈(Stretch)공간

        self.setLayout(vbox) # 빈공간 - 버튼 - 빈공간 순으로 수직 배치된 레이아웃 설정(set) 적용

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png')) # 윈도창에 아이콘 추가
        self.resize(256,256)
        self.show()

    def activateMessage(self) : # 버튼을 클릭할 때 동작하는 함수 : 메세지 박스 출력
        QMessageBox.information(self, "information", "버튼 클릭!")


# 클래스를 정의했으니, 여기에서 실행하겠다... 라는 실행부임
# if __name__=='__main__' : 이 모듈이 직접 실행되는 경우
if __name__=='__main__' :
    app = QApplication(sys.argv) # Qt 프로그램 실행코드
    view = Calculator() # 내가 만든 계산기 GUI 생성 코드
    sys.exit(app.exec_()) # 계산기 종료 시 시스템 종료 명령
