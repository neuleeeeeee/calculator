# ch 5. 2. 1 main.py
import sys # 시스템 제어 관련 모듈(여기서는 프로그램 종료 위해 사용)

from ui import View
from ctrl import Control
from PyQt5.QtWidgets import QApplication

def main() :
    calc = QApplication(sys.argv)
    app=QApplication(sys.argv)
    view=View()
    Control(view=view)
    sys.exit(app.exec_())

if __name__=='__main__':
    main()