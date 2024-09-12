# ch 4. 2. 1 main.py
import sys # 시스템 제어 관련 모듈(여기서는 프로그램 종료 위해 사용)

# 위젯 : GUI 프로그램에서 구성요소를 뜻하는 용어(세부모듈인 QtWidgets으로부터 사용)
from PyQt5.QtWidgets import QApplication, QWidget

#나는 계산기 유형을 직접 정의한다! 이때, QWidget에 기반을 둔다
class Calculator(QWidget) :

    def __init__(self) :
        super().__init__() # (규칙)뭔가(QWidget)에 기반을 둘 경우 써줘야 하는 코드
        self.initUI() # 생성자에서 호출한다
    
    # 초기화 한다
    def initUI(self) :
        self.setWindowTitle('Calculator')
        self.resize(256,256)
        self.show()

# 클래스를 정의했으니, 여기에서 실행하겠다... 라는 실행부임
# if __name__=='__main__' : 이 모듈이 직접 실행되는 경우
if __name__=='__main__' :
    app = QApplication(sys.argv) # Qt 프로그램 실행코드
    view = Calculator() # 내가 만든 계산기 GUI 생성 코드
    sys.exit(app.exec_()) # 계산기 종료 시 시스템 종료 명령
